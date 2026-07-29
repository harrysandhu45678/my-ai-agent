class Assistant:
    def __init__(self):
        self.awake = True

    def is_awake(self):
        return self.awake

    def sleep(self):
        self.awake = False
        return "Going to sleep."

    def wake(self):
        self.awake = True
        return "I'm awake now."

    def status(self):
        if self.awake:
            return "I'm awake."
        return "I'm sleeping."