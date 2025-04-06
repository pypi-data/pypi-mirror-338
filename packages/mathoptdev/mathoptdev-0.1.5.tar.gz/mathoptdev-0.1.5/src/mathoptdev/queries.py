from .send_request import send_request

def get_instances():
    body = {
        "action": "get_instances"
    }
    return send_request(body)

def get_strategies():
    body = {
        "action": "get_strategies"
    }
    return send_request(body)

def get_jobs():
    body = {
        "action": "get_jobs"
    }
    return send_request(body)

def get_user():
    body = {
        "action": "get_user"
    }
    return send_request(body)   

def get_solutions():
    body = {
        "action": "get_solutions"
    }
    return send_request(body)