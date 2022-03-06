from lib.plan.Planner import Planner
from lib.plan.probmod.PlanProblem import PlanProblem


class PlanPee(Planner):

    def __init__(self, search_engine):
        self.__search_engine = search_engine
        self.__plan = None

    def plan(self, world_model, initial_state, objective):
        operators = world_model.get_operators()

        problem = PlanProblem(initial_state, objective, operators)
        solution = self.__search_engine.solve(problem=problem)

        solution.set_path([i for i in solution.get_path() if i.get_operator() is not None])

        self.__plan = solution
        return solution

    def finish_plan(self):
        self.__plan = None

    def pending_plan(self):
        return self.__plan

    def get_operator(self):
        if len(self.__plan.get_path()) != 0:
            return self.__plan.get_path().pop(0).get_operator()
        return None
