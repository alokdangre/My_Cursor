import speech_recognition as sr
import os
import asyncio
from .graph import graph
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

messages = []

openai = AsyncOpenAI()

async def speak(text: str):
    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=text,
        instructions="Speak in angry and rude tone",
        response_format="pcm"
    ) as response:
        await LocalAudioPlayer().play(response)
        

def main():
    # Converts Speech to text
    r = sr.Recognizer()
    
    mic_idx = int(os.environ.get("MIC_DEVICE_INDEX", "0")) 

    # Microphone access
    with sr.Microphone(device_index=mic_idx) as source:
        r.adjust_for_ambient_noise(source) # for noise cancellation
        r.pause_threshold = 2

        while True:
            # print("Speak something...")
            # audio = r.listen(source)

            # print("Processing Audio.. (STT)")
            # stt = r.recognize_google(audio)
            stt = input("enter the query:")

            print("You said:", stt)
            messages.append({ "role": "user", "content": stt})

            for event in graph.stream({ "messages": messages}, stream_mode="values"):
                if "messages" in event:
                    messages.append({"role": "assitant", "content": event["messages"][-1].content})
                    event["messages"][-1].pretty_print()
                    asyncio.run(speak(text=["messages"][-1].content))

main()
