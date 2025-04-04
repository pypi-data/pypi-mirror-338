import json, os, queue, threading
import requests

from .utils import get_new_uuid, obj_is_action
from .encryption import (
    generate_x25519_keypair,
    private_key_from_string,
    public_key_from_string,
    derive_symmetric_key,
    encrypt_aes_gcm,
    decrypt_aes_gcm,
    private_key_to_string,
    public_key_to_string,
    decrypt_str,
    encrypt_str,
)


class Node:
    def __init__(self):
        self.data = {}
        self.actions = {}
        self.data_file = None
        self.default_ntfy_host = "https://ntfy.sh/"
        self.ntfy_host = self.default_ntfy_host

    def generate_keys(self):
        # refresh data if needed
        self.__load_data()

        # check if keys already exist
        if "priv_key" in self.data.keys() and "pub_key" in self.data.keys():
            return

        # generate keys
        priv_key, pub_key = generate_x25519_keypair()
        self.set_data("priv_key", private_key_to_string(priv_key))
        self.set_data("pub_key", public_key_to_string(pub_key))

    def set_ntfy_host(self, _ntfy_host):
        self.ntfy_host = _ntfy_host

    def set_default_ntfy_host(self):
        self.ntfy_host = self.default_ntfy_host

    def generate_uuid(self):
        # refresh data if needed
        self.__load_data()

        # check if uuid already exists
        if "uuid" in self.data.keys():
            return

        # generate uuid
        self.set_data("uuid", get_new_uuid())

    def set_data_file(self, data_file):
        """Assign a data file for this node. Will override values set before this."""
        self.data_file = data_file
        self.__load_data()

    def __load_data(self):
        if self.data_file:
            # if the file exists, info is loaded from it
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as f:
                    self.data = json.load(f)
            # if not, file is created and data object is initialized
            else:
                with open(self.data_file, "w") as f:
                    f.write("{}")
                    self.data = {
                        "neighbors": [],
                        "mailbox": {},
                        "actions": {},
                    }

    def __update_mailbox(self):
        mailbox = {
            "name": self.get_data("name"),
            "uuid": self.get_data("uuid"),
            "pub_key": self.get_data("pub_key"),
        }

        self.data["mailbox"] = mailbox
        self.__dump_data()

    def __dump_data(self):
        if self.data_file:
            with open(self.data_file, "w") as f:
                json.dump(self.data, f, indent=4)

    def set_data(self, key, value):
        """Set an item in the data dict of the node. Will write to data_file if set."""
        self.__load_data()
        self.data[key] = value

        if self.data_file:
            self.__dump_data()
            self.__update_mailbox()

    def add_neighbor(self, neighbor_mailbox):
        self.__load_data()

        if "neighbors" not in self.data.keys():
            self.data["neighbors"] = []

        serialized_mailbox = neighbor_mailbox.serialize()

        if serialized_mailbox in self.data["neighbors"]:
            return

        self.data["neighbors"].append(serialized_mailbox)

        if self.data_file:
            self.__dump_data()

    def get_data(self, key):
        self.__load_data()
        return self.data.get(key)

    def delete_data(self, key):
        """Delete an item in the data dict of the node. Will write to data_file if set."""
        self.__load_data()
        del self.data[key]

        if self.data_file:
            self.__dump_data()

    def save_mailbox(self, filename):
        with open(filename, "w") as f:
            json.dump(self.data["mailbox"], f, indent=4)

    def listen_for_events(self):
        """
        Base listener for all events. Is a generator, and returns all events.
        This is a low level function for custom implementations;
        most use cases should use the higher-level `listen()` function.
        """
        uuid = self.get_data("uuid")
        if not uuid:
            raise Exception(
                "Node UUID not set. Run `generate_uuid()` or load data_file."
            )

        if not self.get_data("priv_key"):
            raise Exception(
                "Node private key not set. Run `generate_keys()` or load data_file."
            )

        if not self.get_data("pub_key"):
            raise Exception(
                "Node public key not set. Run `generate_keys()` or load data_file"
            )

        if not self.get_data("name"):
            raise Exception(
                "Node name not set. Run `set_data('name', 'YOUR_NODE_NAME')` or load data_file."
            )
        
        url = f"{self.ntfy_host}{uuid}/json"
        resp = requests.get(url, stream=True)
        for line in resp.iter_lines():
            if line:
                yield line

    def __get_neighbor_pub_key(self, uuid):
        for neighbor in self.data["neighbors"]:
            if neighbor["uuid"] == uuid:
                return neighbor["pub_key"]

        return None

    def __decrypt_obj(self, obj, sender_uuid):
        nonce, ciphertext, tag = obj["nonce"], obj["ciphertext"], obj["tag"]
        private_key_str = self.get_data("priv_key")
        public_key_str = self.__get_neighbor_pub_key(sender_uuid)

        return decrypt_str(nonce, ciphertext, tag, private_key_str, public_key_str)

    def add_action(self, actiondict):
        self.__load_data()

        if "actions" not in self.data.keys():
            self.set_data("actions", {})

        self.data["actions"][actiondict["action_name"]] = {
            "action_payload": actiondict["action_payload"],
            "action_description": actiondict["action_description"],
        }

        if self.data_file:
            self.__dump_data()

    def register_action(self, action_name, func):
        self.__load_data()

        if action_name not in self.data["actions"].keys():
            raise Exception(
                f"Action {action_name} must be added before registering. Run `add_action()` first."
            )

        self.actions[action_name] = func

    def __is_action(self, obj):
        required = ["action_name", "action_payload"]
        return all(item in obj.keys() for item in required)

    def __check_and_run_action(self, obj, sender_uuid, message_id):
        try:
            self.__load_data()

            action_name = obj["action_name"]
            action_payload = obj["action_payload"]

            if action_name not in self.actions.keys():
                return

            # run the action
            result = self.actions[action_name](**action_payload)
            sender_mailbox = self.__get_mailbox_from_uuid(sender_uuid)
            n = Neighbor()
            n.from_mailbox_str(json.dumps(sender_mailbox))

            resultobj = {
                "result": result if result else "Executed",
                "message_id": message_id,
            }

            n.send_object(resultobj, self)

        except Exception as e:
            raise Exception(f"Error running action: {e}")

    def __send_recieved_confirmation(self, obj, sender_uuid, message_id):
        try:
            sender_mailbox = self.__get_mailbox_from_uuid(sender_uuid)
            n = Neighbor()
            n.set_ntfy_host(self.ntfy_host)
            n.from_mailbox_str(json.dumps(sender_mailbox))

            confirmationobj = {"msg": "Recieved", "message_id": message_id}

            n.send_object(confirmationobj, self)

        except Exception as e:
            raise Exception(f"Error sending confirmation: {e}")

    def __get_mailbox_from_uuid(self, uuid):
        self.__load_data()

        for neighbor in self.data["neighbors"]:
            if neighbor["uuid"] == uuid:
                return neighbor

    def __get_object_from_event(self, event):
        self.__load_data()
        event_obj = dict()
        demex_obj = dict()

        if "neighbors" not in self.data.keys():
            self.set_data("neighbors", [])

        neighbor_uuids = [d["uuid"] for d in self.data["neighbors"]]

        try:
            # try decoding event
            event_obj = json.loads(event.decode(encoding="utf-8"))

            # if the event has a message,
            if "message" in event_obj.keys():
                # try decoding the message
                # will be ignored if not a valid json
                demex_obj = json.loads(event_obj["message"])

                if "sender_uuid" not in demex_obj.keys():
                    return None
                sender_uuid = demex_obj["sender_uuid"]

                # check if sender is in list of neighbors
                if sender_uuid not in neighbor_uuids:
                    return None

                # decrypt object
                decrypted_obj_str = self.__decrypt_obj(demex_obj, sender_uuid)

                # create object if everything's okay
                messagedict = json.loads(decrypted_obj_str)

                # run action if needed
                if self.__is_action(messagedict):
                    self.__check_and_run_action(
                        messagedict, sender_uuid, demex_obj["message_id"]
                    )
                else:
                    self.__send_recieved_confirmation(
                        messagedict, sender_uuid, demex_obj["message_id"]
                    )

                # return message object to code
                return messagedict

        except Exception as e:
            print(e)
            return None

    def listen(self, type=None):
        """
        Listens for objects coming from the node. Yields python dicts.
        If type is specified, only objects matching the type's schema will be yielded.
        If type is None, all objects recieved will be yielded.
        """
        for event in self.listen_for_events():
            event_obj = self.__get_object_from_event(event)
            if event_obj is None:
                continue

            yield event_obj


class Neighbor:
    def __init__(self):
        self.uuid = None
        self.name = None
        self.pub_key = None
        self.default_ntfy_host = "https://ntfy.sh/"
        self.ntfy_host = self.default_ntfy_host

    def from_mailbox_str(self, mailbox_str):
        mailbox = json.loads(mailbox_str)

        self.uuid = mailbox["uuid"]
        self.name = mailbox["name"]
        self.pub_key = mailbox["pub_key"]

    def set_ntfy_host(self, _ntfy_host):
        self.ntfy_host = _ntfy_host

    def set_default_ntfy_host(self):
        self.ntfy_host = self.default_ntfy_host

    def serialize(self):
        return {"uuid": self.uuid, "name": self.name, "pub_key": self.pub_key}

    def from_mailbox_file(self, filepath):
        with open(filepath, "r") as f:
            mailbox_str = f.read()
            self.from_mailbox_str(mailbox_str)

    def set_uuid(self, uuid):
        self.uuid = uuid

    def __encrypt_obj(self, obj, sender):
        try:
            obj_str = json.dumps(obj).encode(encoding="utf-8")
            private_key_str = sender.get_data("priv_key")
            public_key_str = self.pub_key

            return encrypt_str(obj_str, private_key_str, public_key_str)
        except Exception as e:
            raise Exception(f"Error encrypting object: {e}")

    def send_object(self, obj, sender):
        """
        Send an object to the node - will be converted to json and sent as a string.
        Sender must be a Node object.
        """

        # initialize vars
        sender_uuid = None
        sender_priv_key = None
        message_id = get_new_uuid()

        # make sure obj is a dict
        if type(obj) != dict:
            raise Exception("Object must be a dict.")

        # make sure sender has uuid
        try:
            sender_uuid = sender.get_data("uuid")
        except Exception as e:
            raise Exception("Sender must be a Node object.")

        # make sure sender has private key
        try:
            sender_priv_key = sender.get_data("priv_key")
        except Exception as e:
            raise Exception("Sender must be a Node object.")

        # make sure this neighbor has public key
        if not self.pub_key:
            raise Exception("Neighbor must have public key.")

        # encrypt object
        encrypted_obj = self.__encrypt_obj(obj, sender)

        # attach metadata
        encrypted_obj["sender_uuid"] = sender_uuid
        encrypted_obj["message_id"] = message_id

        resp = requests.post(
            f"{self.ntfy_host}{self.uuid}",
            data=json.dumps(encrypted_obj).encode(encoding="utf-8"),
        )

        return {"http_response": resp, "message_id": message_id}

    def send_object_duplex(self, obj, sender, timeout=5):

        recieved_msg_queue = queue.Queue()
        message_id = None
        response_message = None

        lock = threading.Lock()

        # function to listen for messages
        def listen_to_sender():
            for msg in sender.listen():
                recieved_msg_queue.put(msg)

        # function to check if a matching message for found
        def check_for_matching_message():
            nonlocal message_id, response_message
            while True:
                msg = recieved_msg_queue.get()
                with lock:
                    if msg["message_id"] != message_id:
                        continue
                response_message = msg
                break

        # start listening for responses
        collector_thread = threading.Thread(target=listen_to_sender, daemon=True)
        collector_thread.start()

        # send the request and add the message_id in the queue
        res = self.send_object(obj, sender)
        with lock:
            message_id = res["message_id"]

        checker_thread = threading.Thread(
            target=check_for_matching_message, daemon=True
        )
        checker_thread.start()

        # wait for the thread to catch a response
        checker_thread.join(timeout=timeout)

        if checker_thread.is_alive():
            return {"result": "Timeout", "message_id": message_id}

        # return the response
        return response_message
