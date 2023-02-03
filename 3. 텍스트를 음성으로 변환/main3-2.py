from gtts import gTTS #google Text to Speach
from playsound import playsound #playsound 모듈로부터 playsound 불러오기
import os # os 라이브러리 불러오기

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요. 파이썬과 40개의 작품들 입니다"

tts = gTTS(text=text, lang = 'ko')
tts.save("hi.mp3")

playsound("hi.mp3")

