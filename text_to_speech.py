from TTS.api import TTS
from play_audio import play_audio1
import time

def initialize_tts_model():
    try:
        print("[TTS] Initializing the TTS model...")
        # Initialize the TTS model (no need to initialize repeatedly, we can call this function once)
        tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
        print("[TTS] Model initialized successfully.\n")
        return tts
    except Exception as e:
        print("[TTS ERROR] Error initializing the TTS model:", e)
        return None

def speak_text(text, tts_model, output_path=None):
    try:
        if not text.strip():
            print("[TTS WARNING] No text provided to speak.")
            return
        
        print("[TTS] Generating speech from text...")
        if tts_model:
            if output_path is None:
                timestamp1 = int(time.time())
                output_path = f"response_{timestamp1}.wav"
            tts_model.tts_to_file(text=text, file_path=output_path)
            print("[TTS] Voice output saved as", output_path)

            # play the response 
            play_audio1(output_path)
            
        else:
            print("[TTS ERROR] TTS model is not initialized.")
    except Exception as e:
        print("[TTS ERROR]", e)
