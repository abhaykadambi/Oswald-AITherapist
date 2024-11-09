import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert voice to text
def voice_to_text() -> str:
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
       
        print("Listening... Speak now!")
        # Capture the audio from the microphone
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google's speech recognition service
            print("Recognizing your speech...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Run the function
if __name__ == "__main__":
    voice_to_text()