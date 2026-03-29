from crewai.flow.flow import Flow, listen, start, or_, and_


# class Flow_control_or(Flow):
#     @start()
#     def startMethod(self):
#         return "Hello from start method"
    
#     @listen(startMethod)
#     def secondMethod(self):
#         return "Hello2 from second Method"
    
#     @listen(or_(startMethod,secondMethod))
#     def logger(self,result):
#         print(result)
    
# flow = Flow_control_or()
# flow.plot()
# flow.kickoff()

class Flow_Control_and(Flow):
    @start()
    def startMethod(self):
        # return "Hello from start method"
        self.state["Greeting"] = "Hello from start method"
    
    @listen(startMethod)
    def secondMethod(self):
        # return "Hello2 from second Method"
        self.state["joke"] = "What do computers eat? Microchips."
    
    @listen(and_(startMethod,secondMethod))
    def logger(self):
        print(self.state)

f1 = Flow_Control_and()
f1.plot()
f1.kickoff()