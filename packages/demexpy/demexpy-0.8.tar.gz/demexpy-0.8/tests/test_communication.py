import unittest, threading, queue, os, time, logging

from demexpy import Node, Neighbor


class TestCommunication(unittest.TestCase):
    def tearDown(self):
        files = ["alice.json", "bob.json", "alice_mailbox.json", "bob_mailbox.json"]

        for f in files:
            if os.path.exists(f):
                os.remove(f)

    def get_alice(self):
        alice = Node()
        alice.set_data_file("alice.json")

        # setup alice
        alice.generate_uuid()
        alice.generate_keys()
        alice.set_data("name", "Alice")
        alice.save_mailbox("alice_mailbox.json")

        return alice

    def get_bob(self):
        bob = Node()
        bob.set_data_file("bob.json")

        # setup bob
        bob.generate_uuid()
        bob.generate_keys()
        bob.set_data("name", "Bob")
        bob.save_mailbox("bob_mailbox.json")

        return bob

    def get_alice_neighbor(self):
        alice_neighbor = Neighbor()
        alice_neighbor.from_mailbox_file("alice_mailbox.json")

        return alice_neighbor

    def get_bob_neighbor(self):
        bob_neighbor = Neighbor()
        bob_neighbor.from_mailbox_file("bob_mailbox.json")

        return bob_neighbor

    def test_send_object(self):

        # message
        msg_to_send = {"message": "Hello, world!"}

        # create alice
        alice = self.get_alice()

        # create bob
        bob = self.get_bob()

        # create neighbor objects
        alice_neighbor = self.get_alice_neighbor()
        bob_neighbor = self.get_bob_neighbor()

        # add neighbors
        bob.add_neighbor(alice_neighbor)
        alice.add_neighbor(bob_neighbor)

        # queue
        msg_queue = queue.Queue()

        # listen to bob
        def listen_to_bob():
            for msg in bob.listen():
                msg_queue.put(msg)
                break

        bob_thread = threading.Thread(target=listen_to_bob, daemon=True)
        bob_thread.start()

        # wait
        time.sleep(1)

        # send a message
        bob_neighbor.send_object(msg_to_send, alice)

        # wait for bob to get the message
        bob_thread.join(timeout=2)
        if bob_thread.is_alive():
            self.assertEqual(True, False)

        # retrieve message from queue
        recieved_msg = msg_queue.get()

        # compare
        self.assertEqual(str(msg_to_send), str(recieved_msg))

    def test_send_object_duplex(self):

        # message
        msg_to_send = {"message": "Hello, world!"}

        # create alice
        alice = self.get_alice()

        # create bob
        bob = self.get_bob()

        # create neighbor objects
        alice_neighbor = self.get_alice_neighbor()
        bob_neighbor = self.get_bob_neighbor()

        # add neighbors
        bob.add_neighbor(alice_neighbor)
        alice.add_neighbor(bob_neighbor)

        # queue
        msg_queue = queue.Queue()

        # listen to bob
        def listen_to_bob():
            for msg in bob.listen():
                msg_queue.put(msg)
                break

        bob_thread = threading.Thread(target=listen_to_bob, daemon=True)
        bob_thread.start()

        # wait
        time.sleep(1)

        # send a message
        resp = bob_neighbor.send_object_duplex(msg_to_send, alice)

        # wait for bob to get the message
        bob_thread.join(timeout=2)
        if bob_thread.is_alive():
            self.assertEqual(True, False)

        # retrieve message from queue
        recieved_msg = msg_queue.get()

        # compare
        self.assertEqual(str(msg_to_send), str(recieved_msg))

        self.assertEqual(resp["msg"], "Recieved")

    def test_run_action(self):

        # create the objects
        alice = self.get_alice()
        bob = self.get_bob()

        alice_neighbor = self.get_alice_neighbor()
        bob_neighbor = self.get_bob_neighbor()

        alice.add_neighbor(bob_neighbor)
        bob.add_neighbor(alice_neighbor)

        # create the action
        def ping():
            return "Pong"

        bob.add_action(
            {"action_name": "ping", "action_payload": {}, "action_description": "Ping"}
        )

        bob.register_action("ping", ping)

        # recieved msg queue
        msg_queue = queue.Queue()

        # listen to bob
        def listen_to_bob():
            for msg in bob.listen():
                msg_queue.put(msg)
                break

        bob_thread = threading.Thread(target=listen_to_bob, daemon=True)
        bob_thread.start()

        # wait
        time.sleep(1)

        # send a message
        resp = bob_neighbor.send_object_duplex(
            {"action_name": "ping", "action_payload": {}}, alice
        )

        # wait for bob to get the message
        bob_thread.join(timeout=2)
        if bob_thread.is_alive():
            self.assertEqual(True, False)

        # retrieve message from queue
        recieved_msg = msg_queue.get()

        # check
        self.assertEqual(resp["result"], "Pong")

    def test_run_action_with_payload(self):

        # define action
        def say_hello(name):
            return f"Hello, {name}!"

        action_obj = {
            "action_name": "say_hello",
            "action_payload": {"name": "Abdullah"},
            "action_description": "Say hello to the world",
        }

        # create the objects
        alice = self.get_alice()
        bob = self.get_bob()

        alice_neighbor = self.get_alice_neighbor()
        bob_neighbor = self.get_bob_neighbor()

        alice.add_neighbor(bob_neighbor)
        bob.add_neighbor(alice_neighbor)

        bob.add_action(action_obj)
        bob.register_action("say_hello", say_hello)

        # recieved message queue
        msg_queue = queue.Queue()

        # listen to bob
        def listen_to_bob():
            for msg in bob.listen():
                msg_queue.put(msg)
                break

        bob_thread = threading.Thread(target=listen_to_bob, daemon=True)
        bob_thread.start()

        # wait
        time.sleep(1)

        # send a message
        resp = bob_neighbor.send_object_duplex(action_obj, alice)

        # wait for bob to get the message
        bob_thread.join(timeout=2)
        if bob_thread.is_alive():
            self.assertEqual(True, False)

        # retrieve message from queue
        recieved_msg = msg_queue.get()

        # check
        self.assertEqual(resp["result"], "Hello, Abdullah!")

    def test_run_action_timeout(self):
        # create actors
        alice = self.get_alice()
        bob = self.get_bob()

        # create neighbors
        alice_neighbor = self.get_alice_neighbor()
        bob_neighbor = self.get_bob_neighbor()

        # add neighbors
        bob.add_neighbor(alice_neighbor)
        alice.add_neighbor(bob_neighbor)

        # define actions
        def ping():
            return "Pong"

        # add the actions
        bob.add_action(
            {"action_name": "ping", "action_payload": {}, "action_description": "Ping"}
        )

        bob.register_action("ping", ping)

        # wait
        time.sleep(1)

        # send the message
        resp = bob_neighbor.send_object_duplex(
            {"action_name": "ping", "action_payload": {}}, alice, timeout=1
        )

        # should timeout since bob isn't listening
        self.assertEqual(resp["result"], "Timeout")

    def test_alternate_ntfy_host(self):
        # message
        msg_to_send = {"message": "Hello, world!"}

        # create alice
        alice = self.get_alice()
        alice.set_ntfy_host("https://ntfy.tedomum.net/")

        # create bob
        bob = self.get_bob()
        bob.set_ntfy_host("https://ntfy.tedomum.net/")

        # create neighbor objects
        alice_neighbor = self.get_alice_neighbor()
        alice_neighbor.set_ntfy_host("https://ntfy.tedomum.net/")

        bob_neighbor = self.get_bob_neighbor()
        bob_neighbor.set_ntfy_host("https://ntfy.tedomum.net/")

        # add neighbors
        bob.add_neighbor(alice_neighbor)
        alice.add_neighbor(bob_neighbor)

        # queue
        msg_queue = queue.Queue()

        # listen to bob
        def listen_to_bob():
            for msg in bob.listen():
                msg_queue.put(msg)
                break

        bob_thread = threading.Thread(target=listen_to_bob, daemon=True)
        bob_thread.start()

        # wait
        time.sleep(1)

        # send a message
        bob_neighbor.send_object(msg_to_send, alice)

        # wait for bob to get the message
        bob_thread.join(timeout=2)
        if bob_thread.is_alive():
            self.assertEqual(True, False)

        # retrieve message from queue
        recieved_msg = msg_queue.get()

        # compare
        self.assertEqual(str(msg_to_send), str(recieved_msg))

if __name__ == "__main__":
    unittest.main()
