import simpleaudio as sa

def play_audio1(file_path):
    try:
        print("[Audio] Playing response...")
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until playback is finished
    except Exception as e:
        print("[Audio ERROR]", e)