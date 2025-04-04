import uuid

def get_new_uuid():
    return str(uuid.uuid4())

def obj_is_action(obj):
    required = ["action_name", "action_description", "action_payload"]
    return all(item in obj.keys() for item in required)