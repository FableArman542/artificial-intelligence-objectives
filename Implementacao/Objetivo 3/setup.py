from lib.agent.control.controls.learn_ref_control import LearnRefControl
from lib.pee.bestfirst.AASearch import AASearch
from lib.plan.plan_pee.PlanPee import PlanPee
from lib.plan.plan_rtaa.PlanRTAA import PlanRTAA
from lib.agent.control.controls.deliberative_control import DeliberativeControl
from lib.agent.agents.ProspectorAgent import ProspectorAgent
from lib.display.display import Simulation
from lib.plan.plan_wavefront.PlanWavefront import PlanWavefront
from maps.generator.map_generator import generate_map

# Escolher o mapa a utilizar
# real_world = generate_map("map1.txt")
real_world = generate_map("map2.txt")

def RTAA():
    planner = PlanRTAA(lookahead=16)
    control = DeliberativeControl(planner)
    agent = ProspectorAgent(control, real_world)
    simulation = Simulation(real_world, agent)
    simulation.run()

def Wavefront():
    planner = PlanWavefront()
    control = DeliberativeControl(planner)
    agent = ProspectorAgent(control, real_world)
    simulation = Simulation(real_world, agent)
    simulation.run()

def DynaQ():
    control = LearnRefControl()
    agent = ProspectorAgent(control, real_world)
    simulation = Simulation(real_world, agent)
    simulation.run()

# RTAA()
# Wavefront()
DynaQ()
