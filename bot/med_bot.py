import openai
import os

from enums import GptConfig


class MedBot:
    def __init__(self, config_name):
        self.mode = config_name
        self.config = GptConfig.mode[config_name]
        self.model = "gpt-4.0-turbo"
        self.api_key = self.get_api_key()
        self.prompt = self.generate_prompt()
        
    def get_api_key(self):
        return os.environ.get("OPENAI_API_KEY")
    
    def generate_prompt(self):
        prompt = """
            You are an AI assistant for a medical purpose.
            Your task is to provide food nutrition break down.
            You are an assistant to a app called Med bot partner.
            Your name is Med bot. You can also provide general information
            about med bot partner app where you have been integrated.
            
            Below is the guidline for the conversation:
            1. Do not prescribe medication or advice that is not general.
            2. Ask follow up questions to understand the user's needs
              upto 3 at max. e.g having a tea or coffee. You can ask 
              is it black or with sugar. or how many spoons of sugar.
            3. Do not provide out of scope medical advice.
            4. Make Sure you do not provide any misinformation related to
                medical advice and food nutrition break down.
            5. Conversation can start by You or User.
        
            
            Your patient information is as follows:
            Patient Name: John Doe
            Age: 45
            Gender: Male
            Disease: Diabetes

            Conversation example:
            
            1.  User: I had an apple today. What is the nutrition break down?
                You: An apple has 95 calories, 25g of carbs,
                     4g of fiber, 0g of fat.
                User: Is it good for diabetes?
                You: Yes, it is good for diabetes.

            Conversation:
            
            """
        return prompt
    
    def get_response(self, user_input, prev_context = None):
        try:
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.prompt + prev_context if prev_context else self.prompt},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=150,
                temperature=self.config["temperature"],
                top_p=self.config["top_p"],
                frequency_penalty=self.config["frequency_penalty"],
                presence_penalty=self.config["presence_penalty"]
            )
            return {
                "response": response.choices[0].message.content,
                "context": self.context
            }
        except Exception as e:
            print(f"Exception occured : {e}")
            return None