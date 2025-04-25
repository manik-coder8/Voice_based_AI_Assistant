import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("[Listening] Reading audio file...")
        audio = recognizer.record(source)

    try:
        print("[Transcribing] Using Google Web Speech API...")
        text = recognizer.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("[Error] Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"[Error] API request failed: {e}")
        return ""