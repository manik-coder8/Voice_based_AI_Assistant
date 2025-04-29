# removing unnecessary warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import time
from audio_utils import record_audio  
from speech_to_text import transcribe_audio 
from llm_response import get_response  
from text_to_speech import initialize_tts_model, speak_text  

# Initialize TTS model
tts_model = initialize_tts_model()
if not tts_model:
    print("TTS model is not loaded.")
    exit()

# Function to run the voice assistant
def voice_assistant():

    print("Your Voice Assistant is running, please say something....")
    print("Say 'exit' to stop..\n")

    while True:
        # Step 1: Record user audio
        audio_file = record_audio()  # This will save the audio as input1.wav (you can dynamically name this if required)

        # Step 2: Transcribe the audio to text
        transcription = transcribe_audio(audio_file)

        # to stop Voice Assistant
        if transcription.lower() in ["exit", "quit", "stop"]:
            print("Exiting! See you next time...")
            break

        # Step 3: Generate LLM response
        print("[Generating Response] from LLM...")
        response = get_response(transcription)
        print(f"[LLM Response] {response}")

        # Step 4: Convert LLM response to speech (TTS)
        print("[Speaking] AI response...")
        speak_text(response, tts_model)  # This will convert the text response to speech

        # Wait for a 2 seconds before listening again
        time.sleep(2) 

if __name__ == "__main__":
    voice_assistant()  # Start the voice assistant loop