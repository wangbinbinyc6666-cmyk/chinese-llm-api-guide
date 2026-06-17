"""
Advanced usage examples for Chinese LLM API
"""

import openai
from openai import OpenAI

# ============================================
# 1. Basic Chat Completion
# ============================================

def basic_chat():
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://api.your-domain.com/v1"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )

    return response.choices[0].message.content


# ============================================
# 2. Streaming Response
# ============================================

def streaming_chat():
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://api.your-domain.com/v1"
    )

    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": "Write a short story about a cat."}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


# ============================================
# 3. Multi-turn Conversation
# ============================================

def multi_turn_conversation():
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://api.your-domain.com/v1"
    )

    messages = [
        {"role": "system", "content": "You are a Python programming expert."},
        {"role": "user", "content": "How do I reverse a list in Python?"}
    ]

    # First response
    response1 = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    # Add assistant response to history
    messages.append({
        "role": "assistant",
        "content": response1.choices[0].message.content
    })

    # Follow-up question
    messages.append({
        "role": "user",
        "content": "Can you show me an example?"
    })

    response2 = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    return response2.choices[0].message.content


# ============================================
# 4. Function Calling
# ============================================

def function_calling():
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://api.your-domain.com/v1"
    )

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA"
                        }
                    },
                    "required": ["location"]
                }
            }
        }
    ]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": "What's the weather like in Beijing?"}
        ],
        tools=tools,
        tool_choice="auto"
    )

    return response.choices[0].message.tool_calls


# ============================================
# 5. Embeddings
# ============================================

def get_embeddings():
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://api.your-domain.com/v1"
    )

    response = client.embeddings.create(
        model="text-embedding-v3",
        input="Hello, world!"
    )

    return response.data[0].embedding


# ============================================
# 6. Error Handling
# ============================================

def safe_api_call():
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://api.your-domain.com/v1"
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": "Hello!"}]
        )
        return response.choices[0].message.content

    except openai.AuthenticationError:
        return "Error: Invalid API key"
    except openai.RateLimitError:
        return "Error: Rate limit exceeded"
    except openai.APIError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


# ============================================
# Run Examples
# ============================================

if __name__ == "__main__":
    print("=== Basic Chat ===")
    print(basic_chat())

    print("\n=== Embeddings ===")
    embeddings = get_embeddings()
    print(f"Embedding dimensions: {len(embeddings)}")

    print("\n=== Error Handling ===")
    print(safe_api_call())
