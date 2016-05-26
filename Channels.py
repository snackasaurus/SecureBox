#TODO import ROSpi

class Channels:
    def __init__(self):
        #TODO subscribe to channels
        self.open_box_channel = []
        self.close_box_channel = []
        self.secret_code_channel = []

    def should_open_box(self):
        #TODO
        return True

    def box_is_open(self):
        #TODO
        self.close_box_channel.append('done')

    def get_secret_code(self):
        return self.secret_code_channel.pop()



