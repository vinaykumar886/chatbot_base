from dotenv import load_dotenv
import os
import anthropic
from halo import Halo
import pprint

load_dotenv()

pp=pprint.PrettyPrinter(indent=4)

def generate_function(user_text):
    spinner = Halo(text="loading...",spinner="dots")
    spinner.start()

    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_KEY"))
    response=client.messages.create(
        model=os.getenv("MODEL_NAME"),

        max_tokens=500,
        temperature=0.5,
        system="Respond in short and clear sentences.",
        messages=[
            {
                "role":"user",
                "content": user_text
            }
        ]
    )

    spinner.stop()

    print("request")
    pp.pprint(user_text)
    print("response")
    pp.pprint(response.content)

    return response.content

def main():

    while True:

        input_text = input("you:")
        
        if input_text.lower() == "quit":
            break

        response = generate_function(input_text)
        
        print(f"claude {response}")

if __name__ == "__main__":
    main()      