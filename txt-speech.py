#coding: utf-8
import whisper
import os

model = whisper.load_model("base")


for i in os.listdir(): #Listing the directory 
    if os.path.isdir(i): #Verifying if the object is a directory
        for j in os.listdir(i): #Listing the directory
            if j.endswith('.opus') or j.endswith('.mp3'): #Selecting audio files with .opus and .mp3 extension
                answer = model.transcribe(f'{i}/{j}')
                archieve = open(f'{i}/{j}.txt', 'w')
                archieve.write(answer["text"])
                archieve.close()
                