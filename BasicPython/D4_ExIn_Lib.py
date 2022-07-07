from gtts import gTTS  
import os  
mytext = input("Enter text to sppech :") 
language = 'en'
output= gTTS(text=mytext,lang=language,slow=False)
output.save("speech.mp3")
os.system("start speech.mp3")