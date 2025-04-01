class Resource(object):
    def __init__(self, resource):
        self.resource = resource

    def exists(self):
        return True if self.resource else False

    @property
    def get(self):
        return self.resource