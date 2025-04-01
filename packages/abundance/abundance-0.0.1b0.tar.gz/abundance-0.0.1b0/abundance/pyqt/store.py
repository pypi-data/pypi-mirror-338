# store.py
class Store:
    def __init__(self, name, params=None):
        if params is None:
            params = {}
        self.name = name
        self.state = params.get('state', {})
        self.actions = params.get('actions', {})
        self.mutations = params.get('mutations', {})

    def commit(self, mutation, payload=None):
        if mutation in self.mutations:
            self.mutations[mutation](self.state, payload)
        else: raise KeyError(f"Mutation {mutation} does not exist")

    def dispatch(self, action, payload=None):
        if action in self.actions:
            return self.actions[action](payload)
        else:
            raise KeyError(f"Action {action} does not exist")

    def get(self, key):
        return self.state.get(key)

    def set(self, key, value):
        self.state[key] = value

    def getState(self):
        return self.state

    def setState(self, value):
        self.state = value
