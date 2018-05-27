#!/usr/bin/python3

import speech_recognition as sr
r=sr.Recognizer()
mic=sr.Microphone(device_index=4)
#print(r.energy_threshold)
#r.energy_threshold=400
#r.dynamic_energy_threshold = False

with mic as source:
       r.adjust_for_ambient_noise(source) 
       print("say something!!!!")
       audio=r.listen(source,timeout=10)

text=r.recognize_google(audio)
print(text)


