# 🎙️ Voice-Based AI Assistant

A lightweight and efficient voice assistant built in Python that allows users to speak, transcribes their voice to text, generates a response using an LLM (like GPT-2), and replies with human-like speech using a TTS engine. Ideal for hobbyists, developers, and AI enthusiasts looking for a local voice-based interaction system.

---

## 🧠 Features

- 🎤 **Voice Input**: Captures audio from the user's microphone.
- 🗣️ **Speech Recognition**: Converts speech to text using Google Web Speech API.
- 🤖 **LLM-based Response**: Uses GPT-2 to generate natural and helpful replies.
- 🔊 **Text-to-Speech (TTS)**: Converts text response to speech using Coqui TTS.
- 🔁 **Continuous Interaction**: Loops until the user says "exit", "stop", or "quit".
- 💻 **Fully Local Execution** (except STT which uses Google API).

---

## 🛠️ Tech Stack

| Module | Description |
|--------|-------------|
| `sounddevice`, `scipy.io.wavfile` | Captures and saves audio from microphone |
| `speech_recognition` | Transcribes speech using Google Web Speech API |
| `transformers` | Leverages HuggingFace's GPT-2 for text generation |
| `TTS` (Coqui) | Converts generated text into speech |
| `playsound` / custom `play_audio1` | Plays the output audio response |

---

Note: Its working on gpt2 model. working on other model as well. STAY TUNED!!
