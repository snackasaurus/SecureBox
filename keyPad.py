
class KeyPad:
    def __init__(self, message_queue, secret_code):
        self.message_queue = message_queue

    def wait_for_secret_code_match(self, secret_code):
        print('Waiting for secret code')