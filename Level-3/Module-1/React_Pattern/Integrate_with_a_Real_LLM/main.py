import json
import os
import time


def local_response(prompt):
    return {"answer": f"Local fallback response for: {prompt}", "iterations": 1, "tokens": 0}


def ask(prompt, temperature):
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return local_response(prompt)
    try:
        from openai import OpenAI

        client = OpenAI(api_key=key, timeout=10.0, max_retries=2)
        started = time.perf_counter()
        result = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        usage = result.usage.total_tokens if result.usage else 0
        return {
            "answer": result.choices[0].message.content,
            "iterations": 1,
            "tokens": usage,
            "seconds": round(time.perf_counter() - started, 2),
        }
    except Exception as error:
        return {"answer": f"LLM unavailable: {error}", "iterations": 0, "tokens": 0}


def main():
    prompt = os.getenv("AGENT_PROMPT", "Convert 5 kilometers to miles and explain the result")
    for temperature in (0.0, 0.7):
        print(json.dumps({"temperature": temperature, **ask(prompt, temperature)}, indent=2))


if __name__ == "__main__":
    main()
