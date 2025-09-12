import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("API_KEY"),
    base_url="https://api.gilas.io/v1/"
)

def generate_text(prompt: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        generated_text = response.choices[0].message.content
        return {"success": True, "generated_text": generated_text}
    
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    test_prompt = "Explain the theory of relativity in simple terms."
    print(generate_text(test_prompt))