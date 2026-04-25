import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field, create_model
from prompt import prompts  



def clean_json(raw_text: str) -> str:
    """Remove ```json and ``` fences if present."""
    return raw_text.replace("```json", "").replace("```", "").strip()

class QuoteGenerator:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.prompts = prompts()  

    def generate_quote(self, category: str, number: int):
        """Generate multiple inspirational quotes following a given category using their given prompt strictly(using yield)."""

        if category.lower() == "fitness":
            custom_prompt = self.prompts.fitness_prompt()
        elif category.lower() == "career":
            custom_prompt = self.prompts.career_prompt()
        elif category.lower() == "business":
            custom_prompt = self.prompts.business_prompt()
        elif category.lower() == "mindset":
            custom_prompt = self.prompts.mindset_prompt()
        elif category.lower() == "discipline":
            custom_prompt = self.prompts.discipline_prompt()
        else:
            custom_prompt = f"Generate a motivational quote for {category} strictly follwoing those category prompt."

        DynamicQuoteModel = create_model(
            "DynamicQuoteModel",
            **{
                category: (str, Field(..., description="The motivational quote")),
                "author": (str, Field("ai-generated", description="Author is always ai-generated"))
            }
        )

        for _ in range(number):
            prompt = f"""
                {custom_prompt}

                Strict rules:
                - The quote must be in English but in short not too long.
                - The quote must be **inspirational** and strictly related to the {category} category.
                - The quote must follow **strictness** and given **prompt** to the {category} category.
                - Follow this exact JSON format:

                Example output:
                {{
                    "{category}": "quote",
                    "author": "author name"
                }}

                Now, provide one valid quote for the {category} category:
            """

            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful nut a strict assistant that generates inspirational strict no mercy showing types quotes based on the categories."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=50,
                    temperature=1.0
                )

                raw_text = response.choices[0].message.content.strip()
                cleaned_text = clean_json(raw_text)

                
                data = json.loads(cleaned_text)

                validated = DynamicQuoteModel.model_validate(data)

                yield validated.model_dump()


            except json.JSONDecodeError as e:
                yield {"error": "Invalid JSON from model", "raw": cleaned_text, "details": str(e)}
            except Exception as e:
                yield {"error": "Unexpected error", "details": str(e), "raw": raw_text if 'raw_text' in locals() else None}



if __name__ == "__main__":
    quote_generator = QuoteGenerator()
    category = "fitness_prompt"  #career_prompt fitness_prompt business_prompt mindset_prompt discipline_prompt
    number = 3

    for quote in quote_generator.generate_quote(category, number):
        print(quote)




