from lib.agent.control.control import Control
from lib.plan.probmod.WorldModel import WorldModel


class DeliberativeControl(Control):

    def __init__(self, planner):
        self.__planner = planner
        self.finished = False

        self.__world_model = WorldModel()
        self.__objective = None

    def __reconsider(self):
        if self.__objective is None \
                or self.__planner.pending_plan() is None:
            return True
        return False

    def __plan(self, view):
        # print("-> Planning...", end=" ")
        if self.__objective is not None:
            # print("planned")
            self.__planner.plan(self.__world_model, self.__world_model.state, self.__objective)
            view.show_plan(self.__planner.pending_plan())
            # print("> Planner", self.__planner.pending_plan())
        else:
            # print("no objective, plan finished")
            self.__planner.finish_plan()

    def __execute(self):
        # print("-> Executing...", end=" ")
        operator = self.__planner.get_operator()
        if operator is not None:
            # print("Operator =", operator)
            return operator
        # print("Operator does not exist")
        return None

    def __deliberate(self):
        self.__objective = self.__world_model.get_objective()
        # print("-> Deliberating... objective =", self.__objective)

    def __assimilate(self, perception):
        # print("-> Assimilating...")
        self.__world_model.update_world(perception)
        if self.__world_model.get_objective() is None:
            self.finished = True

    def process(self, perception, view):
        self.__assimilate(perception)
        if self.__reconsider():
            self.__deliberate()
            self.__plan(view)

        operator = self.__execute()
        return operator
