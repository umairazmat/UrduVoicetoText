import speech_recognition as sr

def main():
    # Load the audio file
    audio_file = sr.AudioFile("small.wav")

    # Initialize a recognizer object
    recognizer = sr.Recognizer()

    # Extract audio data from the file
    with audio_file as source:
        audio_data = recognizer.record(source)

    # Transcribe the audio data to text
    text = recognizer.recognize_google(audio_data, language="ur-PK")

    # Print the transcribed text
    print(text)

if __name__ == "__main__":
    main()
