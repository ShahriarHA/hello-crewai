# router decoratior
from crewai.flow.flow import Flow, start, listen, router
import random
from pydantic import BaseModel

class Example_State(BaseModel):
    success_flag: bool=False

class Flow_Router(Flow[Example_State]):

    @start()
    def startMethod(self):
        print("Started Method has started")
        random_state = random.choice([True,False])
        self.state.success_flag = random_state
    
    @router(startMethod)
    def secondMethod(self):
        if self.state.success_flag:
            return "success"
        else:
            return "failed"
    @listen("success")
    def thirdMethod(self):
        print("Third method running")
    
    @listen("failed")
    def fourthMethod(self):
        print("Fourth method running")

flow = Flow_Router()
flow.plot()
flow.kickoff()


