import speech_recognition as sr


def perintah():
   
    recognizer = sr.Recognizer()
    microphone = sr.Microphone() 
    
    with microphone as source:
        print('Mendengar...')
        suara = recognizer.listen(source, phrase_time_limit=5)

        try:
            print('Diterima...')
            dengar = recognizer.recognize_google(suara, language='id-ID')
            return dengar
        except:
            pass
        return ''

def run_kona():
    Layanan = perintah()
    print(Layanan)


if __name__ == '__main__':
    run_kona()
