from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class exampleState(BaseModel):
    count: int = 5
    message: str=""

class stateExampleFlow(Flow[exampleState]):
    @start()
    def FirstMethod(s):
        s.state.count += 1
        s.state.message = "'Hello' from first method!"
    
    @listen(FirstMethod)
    def SecondMethod(self):
        self.state.count += self.state.count
        self.state.message = " -- updated from second method!"
        return self.state.message

flow = stateExampleFlow()
flow.plot("My-Plot")
final_output = flow.kickoff()
print(f"Final output-- {final_output}")
print(f"final state: {flow.state}")


