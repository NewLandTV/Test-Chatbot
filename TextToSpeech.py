from fileinput import filename
from gtts import gTTS
from playsound import playsound

fileName = "Sample.mp3"

# 영어 문장
# text = "Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight."

# ttsEn = gTTS(text = text, lang = "en")

# ttsEn.save(fileName)

# .mp3 파일 재생
# playsound(fileName)

# 한국어
# text = "저는 기계입니다. 하지만 괜찮아 보이죠?"

# ttsKo = gTTS(text = text, lang = 'ko')

# ttsKo.save(fileName)

# .mp3 파일 재생
# playsound(fileName)

# 긴 문장 처리
with open("Sample.txt", "r", encoding = "utf8") as f:
    text = f.read()

ttsKo = gTTS(text = text, lang = "ko")

ttsKo.save(fileName)

playsound(fileName)