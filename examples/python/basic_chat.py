"""
BridgeAPI - Chinese LLM API Examples
Basic chat completion with DeepSeek V3.2

Usage:
    pip install openai
    python basic_chat.py
"""

from openai import OpenAI

# Initialize client (replace with your API key and domain)
client = OpenAI(
    api_key="your-api-key-here",
    base_url="https://api.bridgeapi.io/v1"  # Replace with your domain
)

# Basic chat
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms"}
    ],
    temperature=0.7,
    max_tokens=1000
)

print(response.choices[0].message.content)

# Check token usage
print(f"\nTokens used: {response.usage.total_tokens}")
print(f"Estimated cost: ~${response.usage.total_tokens * 0.00000063:.4f}")
