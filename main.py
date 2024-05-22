import speech_recognition as sr
from gtts import gTTS
import os


def perintah():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print('Mendengar...')
        audio = recognizer.listen(source, phrase_time_limit=5)

        try:
            print('Diterima...')
            recognized_text = recognizer.recognize_google(audio, language='id-ID')
            return recognized_text
        except:
            pass
        return ''


def bicara(teks):
    if not teks:
        return

    tts = gTTS(text=teks, lang='id', slow=False)
    filename = 'bicara.mp3'
    tts.save(filename)

    print('Memutar suara...')
    os.system(f'start {filename}')
    


def run_kona():
    Layanan = perintah()
    if Layanan:
        bicara(Layanan)


if __name__ == '__main__':
    run_kona()
