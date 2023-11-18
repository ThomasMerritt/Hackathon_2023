#imports
import speech_recognition
import pyttsx3
from whisper_mic import WhisperMic
import sendMail
import db_extraction

badwords = []
listOfBadSites = []
recognizer = speech_recognition.Recognizer()

#defs
def main(name, lastName, email):
    timesSworn = 0
    firstPass = True
    with open("badwords.txt", "r") as nono:
        lines = nono.readlines()
        badwords.extend([word.strip().lower() for line in lines for word in line.split("\n") if word.strip()])

    userName = name
    userLastName = lastName
    userEmail = email
    result = ""
    mic = WhisperMic()

    while True:
        temp = 0
        result = mic.listen().lower()
        # if any(result in badwords for word in result.split()):
        #     timesSworn += 1
        #     sendMail.sendSpam(userName, userLastName, userEmail, timesSworn)
        #     print("THAT'S A BAD WORD!")
        #     result = ""
        firstPass = True
        for word in badwords:
            temp = result.lower().count(word)
            if temp > 0:
                listOfBadSites = db_extraction.getTruth()
                if firstPass:
                    timesSworn += 1
                    firstPass = False
                else:
                    timesSworn += 0
                sendMail.sendSpam(userName, userLastName, userEmail, timesSworn, word, listOfBadSites)
                print("THAT'S A BAD WORD!")
                result = ""
        print(result)
        result = ""

if __name__ == "__main__":
    main()