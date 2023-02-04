import tkinter as tk
from pydub import AudioSegment
import speech_recognition as sr

def transcribe_audio():
    # Load the audio file
    audio_file = AudioSegment.from_wav("basic.wav")

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

    # Display the transcribed text in the GUI
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, transcribed_text)

def make_chunks(audio_segment, chunk_length):
    chunks = []
    chunk_start = 0
    while chunk_start < len(audio_segment):
        chunk_end = chunk_start + chunk_length
        chunks.append(audio_segment[chunk_start:chunk_end])
        chunk_start = chunk_end
    return chunks

root = tk.Tk()
root.title("Audio Transcription")

frame = tk.Frame(root)
frame.pack()

text_box = tk.Text(frame, height=20, width=50)
text_box.pack(side=tk.LEFT)

transcribe_button = tk.Button(frame, text="Translate", command=transcribe_audio)
transcribe_button.pack(side=tk.RIGHT)

root.mainloop()
