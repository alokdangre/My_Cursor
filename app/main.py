import speech_recognition as sr
import os

def main():
    # Converts Speech to text
    r = sr.Recognizer()
    
    mic_idx = int(os.environ.get("MIC_DEVICE_INDEX", "0")) 

    # Microphone access
    with sr.Microphone(device_index=mic_idx) as source:
        r.adjust_for_ambient_noise(source) # for noise cancellation
        r.pause_threshold = 2

        print("Speak something...")
        audio = r.listen(source)

        print("Processing Audio.. (STT)")
        stt = r.recognize_google(audio)

        print("You said:", stt)

main()
