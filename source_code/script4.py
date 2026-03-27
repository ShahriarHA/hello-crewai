# generate a random city and create a fun fact about that city.
from crewai.flow.flow import Flow, start, listen
from crewai import LLM
from dotenv import load_dotenv
from litellm import completion


class ExampleFlow(Flow):
    # model_ = LLM(model="ollama/llama3.2:3b",base_url="http://localhost:11434")
    model_name = "ollama/llama3.2:3b"

    @start()
    def generate_random_city(self):
        print(f"Starting Flow")
        print(f"Flow state ID: {self.state['id']}")

        response = completion(
            model=self.model_name,
            messages=[
                {
                    "role":"system",
                    "content": "You give only one word."
                },
                {
                    "role":"user",
                    "content":"Return ONLY the name of a random city. Do not explain. Do not write code. Just one city name."
                },

            ],
            base_url="http://localhost:11434"
        )

        random_city = response["choices"][0]["message"]["content"]
        self.state["city"] = random_city
        print(f"random city: {random_city}")
        return random_city
    
    @listen(generate_random_city)
    def generate_fun_fact(self,random_city):
        print(f"flow state id: {self.state['id']}")

        response = completion(
            model=self.model_name,
            messages=[
                {
                    "role":"user",
                    "content": f"tell me a fun fact about {random_city}"
                }
            ],
            base_url="http://localhost:11434"
        )

        fun_fact = response["choices"][0]["message"]["content"]

        self.state['fun_fact'] = fun_fact
        return fun_fact

flow = ExampleFlow()
flow.plot()
result = flow.kickoff()

print(result)






