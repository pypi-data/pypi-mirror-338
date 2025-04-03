import os
import json
import time
import re
import numpy as np
from typing import Tuple, Dict
from groq import Groq
from openai import OpenAI 
import random
from .client import techvai_client
from dotenv import load_dotenv
load_dotenv()

def load_model_config():
    file_path = os.getenv("FILE_PATH")
    if not file_path:
        # print("Error: FILE_PATH environment variable is not set.")
        return {}

    try:
        with open(file_path, "r") as f:
            models = json.load(f)
            # print("Loaded Model Config:", json.dumps(models, indent=4))
            return models
    except Exception as e:
        print(f"Error loading model config: {e}")
        return {}

# Query Complexity Scoring Class

class query_complexity_score:
    def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
        self.client = techvai_client(api_key=api_key).get_client()
        self.model = model
 
    def get_scores(self, question: str) -> Tuple[float, float, float]:
        prompt = f"""You are an AI system trained to assess the complexity of a given question. 
                    Evaluate the following question and distribute a probability score across three categories: 
                    Simple, Moderate, and Complex.
                    Question: {question}
                    Scoring Guidelines:
                    - Assign values between 0 and 1 to each category.
                    - Ensure the sum of all values is exactly 1.
                    - Respond strictly in the format: Simple: <number>, Moderate: <number>, Complex: <number>.
                """
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                model=self.model,
                temperature=0.1,
                max_completion_tokens=50
            )

            model_response = chat_completion.choices[0].message.content
            print(f"[DEBUG] Raw Groq Response: {model_response}")  

            scores = re.findall(r"(?:Simple|Moderate|Complex):\s*(\d*\.?\d+)", model_response)
            
            if len(scores) != 3:
                raise ValueError(f"Invalid Groq response format: {model_response}")  

            return tuple(float(score) for score in scores)

        except Exception as e:
            print(f"[ERROR] Error during scoring: {e}")
            return (0.0, 0.0, 1.0)  

# Query Router Class
class query_router:
    def __init__(self, api_key: str, models: Dict[str, Dict[str, Dict[str, float]]]):
        self.models = models
        self.client = techvai_client(api_key=api_key).get_client()

        self.chat_histories = {}  # Store chat history per session

        # Initialize query complexity scorer internally
        self.complexity_scorer = query_complexity_score(api_key)

    def softmax(self, x: np.ndarray) -> np.ndarray:
        """Compute softmax for an array."""
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()

    def generate_answer(self, question: str, model: str, user_id: str = "session_1",
                        purpose: str = None, logging: bool = False, is_openai: bool = False, cached: bool = False) -> Dict:
        """Generates an answer based on the selected model."""
        print(f"[DEBUG] Generating answer with Model: {model}")

        try:
            start_time = time.time()

            # Retrieve or initialize chat history
            if user_id not in self.chat_histories:
                self.chat_histories[user_id] = []

            chat_history = self.chat_histories[user_id]
            chat_history.append({"role": "user", "content": question})

            # Call OpenAI or Groq API based on the model selection
            if is_openai:
                chat_completion = self.openai_client.chat.completions.create(
                    model=model,
                    messages=[{"role": "system", "content": f"Purpose: {purpose}"} if purpose else {}, *chat_history],
                    temperature=0.6,
                    max_tokens=4096
                )
            else:
                chat_completion = self.client.chat.completions.create(
                    messages=chat_history,
                    model=model,
                    temperature=0.6,
                    max_completion_tokens=4096
                )

            response_text = chat_completion.choices[0].message.content.strip() if chat_completion.choices else ""

            if not response_text:
                print("[ERROR] Model generated an empty response.")
                return {"error": "Empty response from model."}

            # Append assistant response to chat history
            chat_history.append({"role": "assistant", "content": response_text})
            self.chat_histories[user_id] = chat_history  # Update history

            # Token & Speed Calculation
            end_time = time.time()
            response_time = round(end_time - start_time, 3)
            total_tokens = getattr(chat_completion.usage, 'total_tokens', 0)
            prompt_tokens = getattr(chat_completion.usage, 'prompt_tokens', 0)
            completion_tokens = getattr(chat_completion.usage, 'completion_tokens', 0)
            tps = total_tokens / response_time if response_time > 0 else 0

            result = {
                "model": model,
                "response": response_text,
                "tokens_used": total_tokens,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "response_time": response_time,
                "tokens_per_second": round(tps, 2),
                "chat_history": chat_history
            }

            print(f"[DEBUG] Generated Response: {result}")
            return result

        except Exception as e:
            print(f"[ERROR] Exception in generate_answer(): {str(e)}")
            return {"error": "Error generating response. Please try again later."}

    def select_best_model(self, query_complexity_score: tuple, allowed_categories: list, k=3) -> str:
        """Selects the best model based on query complexity and cost/speed trade-offs."""
        simple_score, moderate_score, complex_score = query_complexity_score

        if "simple" in allowed_categories and simple_score > max(moderate_score, complex_score):
            category = "simple"
            speed_weight, cost_weight = 0.5, 0.5
        elif "moderate" in allowed_categories and moderate_score > max(simple_score, complex_score):
            category = "moderate"
            speed_weight, cost_weight = 0.4, 0.6
        else:
            category = "complex"
            speed_weight, cost_weight = 0.25, 0.75

        models = self.models[category]
        model_names = list(models.keys())
        speeds = np.array([models[m]["tokens_per_second"] for m in model_names])
        costs = np.array([models[m]["input_cost_per_million"] for m in model_names])
        speed_probs = self.softmax(speeds)
        cost_probs = self.softmax(-costs)
        final_probs = speed_weight * speed_probs + cost_weight * cost_probs

        final_probs /= final_probs.sum()
        selected_model = random.choices(model_names, weights=final_probs, k=1)[0]
        print(f"[INFO] Selected Model: {selected_model}")
        return selected_model

    def route_query(self, question: str) -> Dict:
        """Routes a query automatically without requiring extra parameters."""
        complexity_scores = self.complexity_scorer.get_scores(question)
        allowed_categories = ["simple" if complexity_scores[0] > max(complexity_scores[1:]) else 
                              "moderate" if complexity_scores[1] > max(complexity_scores[0], complexity_scores[2]) 
                              else "complex"]

        selected_model = self.select_best_model(complexity_scores, allowed_categories)
        response = self.generate_answer(question, selected_model)

        response.update({
            "allowed_categories": allowed_categories,
            "complexity_scores": complexity_scores,
            "selected_model": selected_model
        })

        return response


# Initialize Router
def initialize_router(api_key: str):
    models = load_model_config()
    return query_router(api_key=api_key, models=models)



