import os
from openai import OpenAI
from src.memory.store import MemoryStore

class SuggestionEngine:
    def __init__(self, memory_store: MemoryStore = None):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.memory_store = memory_store or MemoryStore()

    def generate_suggestion(self, current_code: str, user_prompt: str) -> str:
        """
        Yaddaşdakı aktiv pattern-ləri kontekstə əlavə edərək fərdiləşdirilmiş kod təklifi verir.
        """
        # Kritik baldan yuxarı olan aktual vərdişləri alırıq
        active_patterns = self.memory_store.get_active_patterns(threshold=0.25)
        
        # Konteksti formalaşdırırıq
        memory_context = "İstifadəçinin keçmiş kodlama vərdişləri və üstünlükləri:\n"
        if not active_patterns:
            memory_context += "Məlumat yoxdur.\n"
        else:
            for item in active_patterns:
                p = item["pattern"]
                memory_context += f"- [{p.category}] {p.title}: {p.description}\n"
                if p.example_snippet:
                    memory_context += f"  Nümunə: {p.example_snippet}\n"

        system_prompt = (
            "Sən bir AI Pair-Programmer assistentisən. Sənin əsas fərqin "
            "istifadəçinin yazma tərzini bilməyin və ona uyğunlaşmağındır. "
            "Aşağıdakı vərdişləri nəzərə alaraq, təklif etdiyin kodu bu stildə yaz.\n\n"
            f"{memory_context}\n\n"
            "Əgər verilən vərdişlər tapşırığa aiddirsə, mütləq tətbiq et. "
            "Əgər aid deyilsə, standart ən yaxşı təcrübələrdən (best practices) istifadə et."
        )

        user_message = f"Tapşırıq/Sual: {user_prompt}\n\nCari Kod:\n{current_code}"

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.2, # Daha deterministik nəticələr üçün
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Təklif yaradılarkən xəta baş verdi: {e}"