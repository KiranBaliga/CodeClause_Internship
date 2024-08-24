import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

def listen_to_me():
    talker = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="I'm all ears...")
        root.update()
        sound = talker.listen(source)
        try:
            command = talker.recognize_google(sound)
            output_text.insert(tk.END, f"Command Heard: {command}\n")
            status_label.config(text="Processing...")
            root.update()
            process_command(command)
        except sr.UnknownValueError:
            status_label.config(text="Oops, didn't catch that.")
        except sr.RequestError:
            status_label.config(text="Uh-oh, there's a problem with the service.")
        finally:
            status_label.config(text="Ready to listen!")

def process_command(command):
    response = f"Got it! You said: {command}"
    output_text.insert(tk.END, f"Assistant Says: {response}\n")
    talk_back(response)

def talk_back(response_text):
    tts = gTTS(text=response_text, lang='en')
    temp_file = tempfile.NamedTemporaryFile(delete=True)
    tts.save(temp_file.name)
    os.system(f"start {temp_file.name}")

# Create the GUI
root = tk.Tk()
root.title("Chatty Assistant")

frame = tk.Frame(root)
frame.pack(pady=10)

speak_button = tk.Button(frame, text="🎤 Talk to Me", command=listen_to_me, height=2, width=12)
speak_button.pack()

status_label = tk.Label(frame, text="Ready to chat!", font=("Comic Sans MS", 12))
status_label.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack(pady=10)

root.mainloop()
