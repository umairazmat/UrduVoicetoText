from pydub import AudioSegment
import speech_recognition as sr

def main():
    # Load the audio file
    audio_file = AudioSegment.from_wav("second.wav")

    # Split the audio file into smaller chunks
    chunk_length_ms = 30000 # 30 seconds
    chunks = make_chunks(audio_file, chunk_length_ms)

    # Initialize a recognizer object
    recognizer = sr.Recognizer()

    # Transcribe each chunk to text
    transcribed_text = ""
    for chunk in chunks:
        audio_data = sr.AudioData(chunk.raw_data, chunk.frame_rate, chunk.sample_width)
        text = recognizer.recognize_google(audio_data, language="ur-PK")
        transcribed_text += text

    # Print the transcribed text
    print(transcribed_text)

def make_chunks(audio_segment, chunk_length):
    chunks = []
    chunk_start = 0
    while chunk_start < len(audio_segment):
        chunk_end = chunk_start + chunk_length
        chunks.append(audio_segment[chunk_start:chunk_end])
        chunk_start = chunk_end
    return chunks

if __name__ == "__main__":
    main()
