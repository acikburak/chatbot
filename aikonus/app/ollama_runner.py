import subprocess
import json
import tempfile

def call_ollama(conversation):
    # Konuşma geçmişini JSONL (JSON satırları) formatına dönüştür
    formatted_prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])

    # ✅ DEBUG: Ollama'ya gönderilecek prompt
    print("\n🛨️ [OLLAMA GİDEN PROMPT]:\n" + "-"*40)
    print(formatted_prompt)
    print("-"*40 + "\n")

    try:
        # Prompt'u geçici dosyaya yaz (gerekirse debug/test amacıyla kullanılabilir)
        with tempfile.NamedTemporaryFile("w+", delete=False) as temp_file:
            temp_file.write(formatted_prompt)
            temp_file.flush()

            # Ollama ile mistral modelini çalıştır
            result = subprocess.run(
                ["ollama", "run", "mistral"],
                input=formatted_prompt,
                capture_output=True,
                text=True
            )

        # ✅ DEBUG: Ollama'dan gelen ham cevap
        print("🤖 [OLLAMA GELEN CEVAP]:\n" + "-"*40)
        print(result.stdout.strip())
        print("-"*40 + "\n")

        return result.stdout.strip()

    except Exception as e:
        print(f"[HATA] Ollama çağrısı başarısız: {e}")
        return f"[Hata] Ollama çalıştırılamadı: {e}"
