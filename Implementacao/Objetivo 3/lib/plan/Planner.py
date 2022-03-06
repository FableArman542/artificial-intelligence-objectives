

class Planner:

    def plan(self, world_model, initial_state, objective):
        raise NotImplementedError("Interface")

    def finish_plan(self):
        raise NotImplementedError("Interface")

    def pending_plan(self):
        raise NotImplementedError("Interface")

    def get_operator(self):
        raise NotImplementedError("Interface")
