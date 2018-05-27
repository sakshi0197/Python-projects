'''from gtts import gTTS
import os

mytext = raw_input("Enter the msg :")
language='en'

myobj = gtts(text=mytext , lang=language ,slow=False)

myobj.save("audio.mp3")

os.system("ad audio.mp3")
'''

import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
print("Press 'q to exit.'")
inn=()

while True:
     if(inn != 'q' ): 
              inn = input("Plz Enter something :") 
              engine.say(inn)
              engine.runAndWait()

     else:
          exit()

