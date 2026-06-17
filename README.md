# 🚀 Chinese LLM API Access Guide

> **Access DeepSeek, Qwen, GLM from anywhere in the world.**
> No Chinese phone number. No real-name verification. One API key.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![API](https://img.shields.io/badge/API-OpenAI-Compatible-green.svg)](https://platform.openai.com/docs/api-reference)

---

## 🌟 Why Chinese Models?

Chinese LLMs now dominate OpenRouter. **6 of Top 10 models are from China.**

| Model | Performance | Cost | Availability |
|-------|-------------|------|--------------|
| DeepSeek V3.2 | Matches GPT-4o | **97% cheaper** | ✅ Global |
| Qwen 3.5 Plus | Best in class | **93% cheaper** | ✅ Global |
| GLM-5 | Strong reasoning | **79% cheaper** | ✅ Global |

---

## 💰 Price Comparison

| Model | Input (1M tokens) | Output (1M tokens) | vs GPT-4o |
|-------|:-:|:-:|:-:|
| **DeepSeek V3.2** | $0.42 | $0.63 | **96% cheaper** |
| **Qwen 3.5 Plus** | $0.22 | $1.00 | **93% cheaper** |
| **GLM-5** | $0.72 | $3.22 | **79% cheaper** |
| GPT-4o | $2.50 | $10.00 | Baseline |

---

## 🚀 Quick Start (30 seconds)

### Python

```python
import openai

client = openai.OpenAI(
    api_key="your-api-key",
    base_url="https://api.your-domain.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

### Node.js

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'your-api-key',
  baseURL: 'https://api.your-domain.com/v1'
});

const response = await client.chat.completions.create({
  model: 'deepseek-chat',
  messages: [
    { role: 'user', content: 'Hello!' }
  ]
});

console.log(response.choices[0].message.content);
```

### cURL

```bash
curl https://api.your-domain.com/v1/chat/completions \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

## 📚 Available Models

### Chat Models

| Model | Best For | Price | Speed |
|-------|----------|-------|-------|
| `deepseek-chat` | General purpose | $0.42/1M | ⚡ Fast |
| `deepseek-reasoner` | Complex reasoning | $0.55/1M |  Medium |
| `qwen-plus` | Cost-effective | $0.22/1M | ⚡ Fast |
| `glm-4` | Chinese content | $0.72/1M | ⚡ Fast |

### Embedding Models

| Model | Dimensions | Price |
|-------|------------|-------|
| `text-embedding-v3` | 1024 | $0.01/1M tokens |

---

## 🔧 Features

- ✅ **OpenAI Compatible** - Drop-in replacement for OpenAI API
- ✅ **No Chinese Phone** - Sign up with any email
- ✅ **Global Access** - Works from anywhere in the world
- ✅ **Pay per Use** - No monthly fees, pay only for what you use
- ✅ **Multiple Payment** - Stripe, PayPal, Crypto accepted
- ✅ **99.9% Uptime** - Enterprise-grade infrastructure

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [Quick Start](#-quick-start-30-seconds) | Get started in 30 seconds |
| [API Reference](docs/api-reference.md) | Complete API documentation |
| [Examples](examples/) | Code examples in Python, Node.js, Java |
| [Pricing](#-price-comparison) | Detailed pricing information |
| [FAQ](docs/faq.md) | Frequently asked questions |
| [Changelog](docs/changelog.md) | What's new |

---

## 🛡️ Security & Privacy

- 🔐 **Encrypted API Keys** - Your keys are encrypted at rest
- 🚫 **No Data Logging** - We never log your API requests
- 🌍 **GDPR Compliant** - Full compliance with data protection regulations
- 🔒 **HTTPS Only** - All connections are encrypted

---

## 🎯 Use Cases

### For Developers
- Build AI-powered applications at 97% lower cost
- Migrate from OpenAI with zero code changes
- Access cutting-edge models for research

### For Businesses
- Reduce AI costs by 90%+
- Scale without breaking the bank
- Enterprise-grade reliability

### For Researchers
- Access state-of-the-art models
- Run experiments at scale
- Compare model performance

---

## 📊 Performance Benchmarks

| Benchmark | DeepSeek V3 | GPT-4o | Improvement |
|-----------|-------------|--------|-------------|
| MMLU | 88.5 | 87.2 | +1.5% |
| HumanEval | 82.3 | 80.1 | +2.7% |
| MATH | 76.8 | 74.2 | +3.5% |

---

## 🚀 Getting Started

1. **Sign Up** - Create an account at [your-platform.com](#)
2. **Get API Key** - Generate your API key in the dashboard
3. **Start Building** - Use the code examples above

**Free Trial**: 500K tokens free to get started!

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact & Support

- **Email**: support@your-domain.com
- **Discord**: [Join our community](#)
- **Twitter**: [@your-handle](#)
- **GitHub Issues**: [Report a bug](#)

---

## ⭐ Star History

If you find this useful, please give us a ⭐!

---

**Made with ❤️ for the global AI community**
