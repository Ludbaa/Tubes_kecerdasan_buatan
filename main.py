import speech_recognition as sr
from gtts import gTTS
import pyttsx3 as pyt
import pywhatkit
import os
import subprocess
import wikipedia

wikipedia.set_lang("id")

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
        except sr.UnknownValueError:
            print("Maaf, saya tidak mengerti apa yang Anda katakan.")
        except sr.RequestError:
            print("Maaf, ada masalah dengan permintaan Anda.")
        
        return ''

def bicara(teks):
    if not teks:
        return

  
    tts = gTTS(text=teks, lang='id', slow=False)
    filename = 'bicara.mp3'
    tts.save(filename)

    print('Memutar suara...')
    if os.name == 'nt':  
        os.system(f'start {filename}')
    
 
    engine = pyt.init()
    engine.say(teks)
    engine.runAndWait()

def cari_di_wikipedia(kueri):
    try:
        hasil = wikipedia.summary(kueri, sentences=2)
        print(hasil)
        bicara(hasil)
    except wikipedia.exceptions.DisambiguationError as e:
        bicara("Topik terlalu banyak. Mohon lebih spesifik.")
    except wikipedia.exceptions.PageError:
        bicara("Tidak menemukan informasi mengenai topik tersebut.")

def jalankan_perintah(teks):
    if "putar musik" in teks.lower():
        pywhatkit.playonyt("Lagu favorit Anda")
    elif "buka notepad" in teks.lower():
        subprocess.run(['notepad.exe'])
    elif "buka kalkulator" in teks.lower():
        subprocess.run(['calc.exe'])
    elif "cari" in teks.lower():
        kueri = teks.lower().replace("cari", "").strip()
        cari_di_wikipedia(kueri)
    elif "penemu bahasa python" in teks.lower():
        cari_di_wikipedia("Guido van Rossum")
    else:
        bicara("Perintah tidak dikenal.")

def run_kona():
    Layanan = perintah()
    if Layanan:
        bicara(Layanan)
        jalankan_perintah(Layanan)

if __name__ == '__main__':
    run_kona()
