import os
from openai import OpenAI
from config import OPENAI_API_KEY
# Əgər engine qovluğun yoxdursa, SuggestionEngine hardadırsa importu ona uyğun düzəlt
from engine.suggestion_engine import SuggestionEngine 

def run_ab_test():
    print("Qiymətləndirmə (Eval) ssenarisi işə salınır...\n")
    
    user_task = "FastAPI ilə user tapılmadıqda 404 xətası qaytaran endpoint yaz."
    
    print("--- TEST A: Yaddaşsız LLM (Baseline) ---")
    client = OpenAI(api_key=OPENAI_API_KEY)
    baseline_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sən bir AI proqramçısan."},
            {"role": "user", "content": user_task}
        ],
        temperature=0.2
    )
    print(baseline_response.choices[0].message.content)
    print("\n" + "="*50 + "\n")
    
    print("--- TEST B: Yaddaşlı AI Pair-Programmer ---")
    engine = SuggestionEngine()
    memory_response = engine.generate_suggestion(current_code="", user_prompt=user_task)
    print(memory_response)

if __name__ == "__main__":
    run_ab_test()