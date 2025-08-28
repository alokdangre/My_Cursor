import speech_recognition as sr

def main():
    # Converts Speech to text
    r = sr.Recognizer()

    # Microphone access
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # for noise cancellation
        r.pause_threshold = 2

        print("Speak something...")
        audio = r.listen(source)

        print("Processing Audio.. (STT)")
        stt = r.recognize_google(audio)

        print("You said:", stt)

main()
