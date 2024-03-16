from email.mime import audio
import speech_recognition as sr

r = sr.Recognizer()

# 마이크로부터 음성 듣기
with sr.Microphone() as source:
    print("듣고 있어요.")

    audio = r.listen(source)

try:
    # 구글 API로 인식 (하루 50회)
    # 영어 문장
    # text = r.recognize_google(audio, language = "en-US")

    # print(text)

    # 한국어
    text = r.recognize_google(audio, language = "ko")

    print(text)
except sr.UnknownValueError:
    # 음성 인식 실패한 경우
    print("인식 실패")
except sr.RequestError as e:
    # API Key 오류, 또는 네트워크 단절 등
    print("요창 실패 : {0}".format(e))