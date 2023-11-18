#imports
import speech_recognition
import pyttsx3
from whisper_mic import WhisperMic

recognizer = speech_recognition.Recognizer()

#defs
def main():
    # while True:
    #     try:
    #         with speech_recognition.Microphone() as mic:
    #             recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
    #             audio = recognizer.listen(mic)

    #             text = recognizer.recognize_google(audio)
    #             text = text.lower()

    #             print(text)

    #     except:

    #         recognizer = speech_recognition.Recognizer()
    #         continue

    print("yahallo")

    mic = WhisperMic()
    result = mic.listen()
    print(result)

if __name__ == "__main__":
    main()