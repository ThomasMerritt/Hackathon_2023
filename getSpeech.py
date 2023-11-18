#imports
import speech_recognition
import pyttsx3
from whisper_mic import WhisperMic
import sendMail

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

    userName = input("What is your name? ")
    userEmail = input("What is your email? ")
    result = ""
    mic = WhisperMic()

    while True:
        while result.find("thomas")==-1:
            result = mic.listen().lower()
            print(result)
        sendMail.sendSpam(userName, userEmail)
        result = ""

if __name__ == "__main__":
    main()