import speech_recognition as sr

def test_microphone():
    recognizer = sr.Recognizer()

    # Print the list of available microphones
    microphones = sr.Microphone.list_microphone_names()
    print("Available microphones:")
    for i, mic in enumerate(microphones):
        print(f"{i + 1}. {mic}")

    # Ask the user to select a microphone
    mic_index = int(input("Select a microphone (enter the corresponding number): ")) - 1

    # Use the selected microphone for recognition
    with sr.Microphone(device_index=mic_index) as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Speak something...")

        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected within the specified time.")
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")

if __name__ == "__main__":
    test_microphone()
