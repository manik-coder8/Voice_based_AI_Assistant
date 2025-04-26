# from transformers import pipeline

# # You can change model_name to something like "mistralai/Mistral-7B-Instruct-v0.1" later
# def get_response(prompt, model_name="gpt2"):
#     print("[Generating Response] from LLM...")
#     generator = pipeline("text-generation", model=model_name)
#     result = generator(prompt, max_length=100, do_sample=True)
#     reply = result[0]['generated_text']
#     print("[LLM Response]", reply)
#     return reply
# llm_response.py

from transformers import pipeline, set_seed

# Initialize the GPT-2 model
generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def get_response(prompt: str) -> str:
    # Structure the prompt to guide GPT-2 better
    system_propmt = (
        "You are a helpful and friendly voice assistant. Keep your answers short, informative, and conversational, "
        "around 3 to 5 seconds when spoken. Respond naturally to user input.\n\n"
        "User: What's the weather like?\n"
        "AI: It's sunny and warm today. A perfect day to be outside!\n\n"
        "User: Tell me a joke\n"
        "AI: Why don't scientists trust atoms? Because they make up everything!\n\n"
        "User: How are you?\n"
        "AI: I'm doing great, thanks for asking! How about you?\n\n"
    )
    formatted_prompt = system_propmt +  f"User: {prompt}\nAI:"

    try:
        # Generate text with controlled length and no repetition
        generated = generator(
        formatted_prompt,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1,
        pad_token_id=50256  # To suppress warning about padding
        )

        # Extract only the AI's response part after "AI:"
        output_text = generated[0]["generated_text"]
        response_part = output_text.split("AI:")[-1].strip()

        # If there's a second dialogue turn, cut it
        response_lines = response_part.split("\n")
        clean_response = response_lines[0].strip()

        if not clean_response:
            return "I'm sorry, I didn't catch that. Could you please say it again?"

        return clean_response
    
    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return "Something went wrong generating the response."
    

