from gtts import gTTS  
from playsound import playsound  

text1 = input("Enter value for speech : ")
language = 'en'  
obj = gTTS(text=text1, lang=language, slow=False)  
obj.save("test.mp3")  
playsound("test.mp3")  