import time
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (듣기, STT)
def Listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language = "ko")

        print("[장경혁tv] " + text)
        Answer(text)
    except sr.UnknownValueError:
        # 음성 인식 실패한 경우
        print("인식 실패")
    except sr.RequestError as e:
        # API Key 오류, 또는 네트워크 단절 등
        print("요창 실패 : {0}".format(e))

# 대답
def Answer(inputText):
    answerText = ""    

    if "안녕" in inputText:
        answerText = "안녕하세요? 반갑습니다."
    elif "날씨" in inputText:
        answerText = "오늘의 기온은 17도입니다. 맑은 하늘이 예상됩니다."
    elif "환율" in inputText:
        answerText = "원 달러 환율은 1285원입니다."
    elif "고마워" in inputText:
        answerText = "별 말씀을요."
    elif "종료" in inputText:
        answerText = "다음에 또 만나요."

        # 더 이상 듣지 않음
        stopListening(wait_for_stop = False)
    else:
        answerText = "다시 한 번 말씀해주시겠어요?"

    Speak(answerText)

# 소리내어 읽기 (TTS)
def Speak(text):
    print("[Bot] " + text)

    fileName = "./Voice.mp3"

    tts = gTTS(text = text, lang = "ko")

    tts.save(fileName)

    playsound(fileName)

    # Voice.mp3 파일이 존재하면 삭제
    if os.path.exists(fileName):
        os.remove(fileName)

r = sr.Recognizer()
m = sr.Microphone()

Speak("무엇을 도와드릴까요?")

stopListening = r.listen_in_background(m, Listen)

# 더 이상 듣지 않음
# stopListening(wait_for_stop = False)

while True:
    time.sleep(0.1)