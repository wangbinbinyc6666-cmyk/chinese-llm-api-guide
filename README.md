# Chinese LLM API Access Guide

> Access DeepSeek V3.2, Qwen 3.5, GLM-5 from anywhere in the world.
> No Chinese phone number. No real-name verification. One API key.

## Why Chinese Models?

Chinese LLMs now dominate OpenRouter. 6 of Top 10 models are from China.
DeepSeek V3.2 matches GPT-4o on 80% of tasks at **1/30th the cost**.

## Price Comparison

| Model | Output (1M tokens) | vs GPT-4o |
|-------|:-:|:-:|
| DeepSeek V3.2 | $0.63 | **96% cheaper** |
| Qwen 3.5 Plus | $1.00 | **93% cheaper** |
| GLM-5 | $3.22 | **79% cheaper** |

## Quick Start (30 seconds)

```python
import openai

client = openai.OpenAI(
    api_key="your-key-here",
    base_url="https://api.bridgeapi.io/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

It's a drop-in replacement for OpenAI, just change base_url.

## Get API Access

| Plan | Price | Link |
|------|-------|------|
| **Starter** | $5 | [Get $5 Credits](https://www.creem.io/test/payment/prod_2YG0Vqr3ST0TcXJQlsTFFb) |
| **Popular** | $10 | [Get $10 Credits](https://www.creem.io/test/payment/prod_3onzrx6BoVhSd250HF3sOQ) |
| **Pro** | $20 | [Get $20 Credits](https://www.creem.io/test/payment/prod_4kU1KrfBjrVSI0jVeWj8UO) |

No monthly fee. Pay only for what you use. Instant delivery.

## Supported Models

- **DeepSeek V3.2** by DeepSeek, 128K context, best for general purpose and coding
- **Qwen 3.5 Plus** by Alibaba, 1M context, best for long documents and RAG
- **GLM-5** by Zhipu AI, 200K context, best for programming and agents

## Documentation

- [Cost Comparison](docs/cost-comparison.md)
- [Python Examples](examples/python/basic_chat.py)
- [Node.js Examples](examples/nodejs/basic_chat.js)

## License

MIT

---

Built with love for developers who want affordable AI.
