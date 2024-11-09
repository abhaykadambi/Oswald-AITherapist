
from speech import*
import speech_recognition as sr
from openai import OpenAI


PROXY_ENDPOINT = "https://nova-litellm-proxy.onrender.com/"
TEAM_API_KEY = "sk-na910fed2Ths7GhP9U7yjQ"

def example_chat(model_name: str, stream: bool = True):

    """

    Examples of chat completions from the proxy

    """

    client = OpenAI(

        api_key=TEAM_API_KEY, # set this!!!

        base_url=PROXY_ENDPOINT # and this!!!

    )

    messages = []
    while True:
        user_input = voice_to_text()
        if user_input == '':
            break
        messages.append({"role": "user", "content":user_input})
        response = client.chat.completions.create(

            model=model_name,

            messages = messages,

            stream=stream

        )
        messages.append({"role":"assistant", "content":response.choices[0].message.content})
        print(response.choices[0].message.content)


        
    # for chunk in response:
    #     for choice in chunk.choices:
    #         print(choice)
        # print(chunk.message.content)

if __name__ == "__main__":

    example_chat("openai/gpt-4o", stream=False)