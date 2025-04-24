import sounddevice as sd
import scipy.io.wavfile as wav
import time

#Recording for 5 seconds, mentioned in duration
def record_audio(filename=None, duration=5, fs=44100):
    if filename is None:
        timestamp = int(time.time())
        filename = f"input_{timestamp}.wav"
    
    print("Speak now...")
    print("Recording for", duration, "seconds....")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, audio)
    print("Recording Complete and Audio recorded as", filename)
    return filename  # ✅ Returning path for next step
