from gtts import gTTS
import playsound

filename = "temp.mp3"

mytext = 'హలో ఎలా వున్నారు'
language = 'te'


myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(filename)

playsound.playsound(filename)
os.remove(filename)
