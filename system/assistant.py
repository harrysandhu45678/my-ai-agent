class Assistant:

    def __init__(self):
        self.awake = True
        self.busy = False

    def sleep(self):
        self.awake = False
        return "Going to sleep."

    def wake(self):
        self.awake = True
        return "I'm awake."

    def is_awake(self):
        return self.awake

    def is_busy(self):
        return self.busy

    def set_busy(self, value):
        self.busy = value

    def status(self):
        if self.awake:
            return "Awake"

        return "Sleeping"