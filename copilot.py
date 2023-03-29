import os
import json
from dotenv import load_dotenv
import openai

class Copilot:

    def clear_text(self, text):
        a = text.replace("\n", " ")
        b = a.split()
        c = " ".join(b)

        return c

    def get_answer(self, question):
        prompt = question
        
        load_dotenv()

        openai.api_key = os.getenv("chat_gpt_key")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            temperature=0.1,
        )

        cleared_text = self.clear_text(response.choices[0]["text"])+"\n\n end" ####################################
        
        return cleared_text

# a = Copilot().get_answer("как создать ветку y от ветки x в консоли для git")
# print(a)



