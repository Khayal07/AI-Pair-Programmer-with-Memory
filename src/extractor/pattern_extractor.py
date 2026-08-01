import os
from typing import List
from pydantic import BaseModel
from openai import OpenAI

# Faza 2-də yaratdığımız schema-nı import edirik
from src.memory.schemas import MemoryPattern

class ExtractionResult(BaseModel):
    patterns: List[MemoryPattern]

class PatternExtractor:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

    def extract_from_diff(self, diff_text: str) -> List[MemoryPattern]:
        """
        Git diff mətnini oxuyur və LLM vasitəsilə proqramlaşdırma vərdişlərini çıxarır.
        """
        if not diff_text.strip():
            return []

        prompt = (
            "Sən bir AI Pair-Programmer assistentisən. "
            "Aşağıdakı Git diff mətnini (kod dəyişikliklərini) analiz et. "
            "Məqsəd proqramçının yazma tərzini, adlandırma qaydalarını (naming conventions), "
            "error handling üslubunu və ya spesifik asılılıq/kitabxana istifadəsini öyrənməkdir.\n\n"
            "Əgər təkrar istifadə edilə bilən, spesifik bir pattern və ya üslub görsən, "
            "onu çıxar. Əgər sıradan bir dəyişiklikdirsə, məhəl qoyma.\n\n"
            f"Git Diff:\n{diff_text}"
        )

        try:
            # OpenAI Structured Outputs (beta.chat.completions.parse) istifadə edərək 
            # nəticəni birbaşa Pydantic modeli formatında alırıq.
            response = self.client.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Sən kod diff-lərindən proqramlaşdırma pattern-lərini çıxaran təcrübəli AI-san."},
                    {"role": "user", "content": prompt}
                ],
                response_format=ExtractionResult,
            )
            
            extracted_data = response.choices[0].message.parsed
            return extracted_data.patterns if extracted_data else []
            
        except Exception as e:
            print(f"Pattern çıxarılarkən xəta baş verdi: {e}")
            return []