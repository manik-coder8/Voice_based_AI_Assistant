import requests

def get_response(prompt: str) -> str:
    if not prompt.strip():
        return "I'm sorry, I didn't catch that. Could you please repeat?"

    # Helpful context to make Mistral act as a voice assistant
    system_prompt = (
        "You are a helpful and friendly voice assistant. Keep your answers short, informative, and conversational, "
        "around 3 to 5 seconds when spoken. Respond naturally to user input.\n\n"
        "User: What's the weather like?\n"
        "AI: It's sunny and warm today. A perfect day to be outside!\n\n"
        "User: Tell me a joke\n"
        "AI: Why don't scientists trust atoms? Because they make up everything!\n\n"
        "User: How are you?\n"
        "AI: I'm doing great, thanks for asking! How about you?\n\n"
    )

    # Merge system prompt with user prompt
    full_prompt = f"{system_prompt}User: {prompt}\nAI:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral:latest",  # ✅ Important: specify version
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "num_predict": 100
                }
            },
            timeout=30
        )

        data = response.json()

        # Debug line (you can comment this later)
        print("[DEBUG] Ollama returned:", data)

        if "response" not in data:
            return "I'm sorry, something went wrong on the server."

        # Clean and return only 1-line response
        reply = data["response"].strip().split("\n")[0]

        return reply if reply else "I'm sorry, I didn't catch that."

    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return "I'm having trouble responding right now."