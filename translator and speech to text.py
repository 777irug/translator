from googletrans import Translator,LANGUAGES
from googletrans.models import Translated
import speech_recognition as sr

choise=int(input("1.translator \n2.speech to text"))

if choise=='1':
		
	lang = list(LANGUAGES.values())
	print("Welcome to language Translate")
	input_text = input("Please Enter Your Text in 	english:\n")
	outputlang = input("Please enter output language name (ex.-hindi,gujarat,japanese:\n ").lower()
	if outputlang not in lang:
		print ("Sorry language not avaiable")
	else:
	       translator = Translator()
	       translated = translator.translate(text=input_text, src="english",dest=out_lang)
	       translated = str(translated).split(", ")
	       converted = translated[2]
	       pro = translated[3]
	       print(converted)
	       print(pro)
  	
else:
	import speech_recognition as sr

	r = sr.Recognizer()
	with sr.Microphone() as source:
	   print("Speak Anything :")
	   audio = r.listen(source)
	   try:
	       text = r.recognize_google(audio)
	       print("You said : {}".format(text))
	   except:
	   	print("Sorry could not recognize what you said")