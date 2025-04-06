from .send_request import send_request, send_stream_request

def process_queue_sync():
    body = {
        "action": "process_queue"
    }
    return send_request(body)

def process_queue():
    """Process queue with streaming response"""
    body = {
        "action": "process_queue"
    }
    return send_stream_request(body) 