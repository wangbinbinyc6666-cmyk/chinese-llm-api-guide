# API Reference

Complete documentation for the Chinese LLM API.

## 🔗 Base URL

```
https://api.your-domain.com/v1
```

## 🔐 Authentication

All API requests require authentication via Bearer token:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.your-domain.com/v1/...
```

---

## 💬 Chat Completions

### Create Chat Completion

**Endpoint**: `POST /v1/chat/completions`

Creates a model response for the given chat conversation.

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `model` | string | ✅ | Model ID to use |
| `messages` | array | ✅ | List of messages |
| `temperature` | number | ❌ | Sampling temperature (0-2) |
| `max_tokens` | integer | ❌ | Maximum tokens to generate |
| `stream` | boolean | ❌ | Enable streaming |

#### Example Request

```json
{
  "model": "deepseek-chat",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "temperature": 0.7,
  "max_tokens": 1000
}
```

#### Example Response

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 9,
    "total_tokens": 19
  }
}
```

---

## 📝 Embeddings

### Create Embedding

**Endpoint**: `POST /v1/embeddings`

Creates an embedding vector representing the input text.

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `model` | string | ✅ | Embedding model ID |
| `input` | string/array | ✅ | Text to embed |

#### Example Request

```json
{
  "model": "text-embedding-v3",
  "input": "The quick brown fox jumps over the lazy dog"
}
```

#### Example Response

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [0.0023, -0.0091, ...],
      "index": 0
    }
  ],
  "model": "text-embedding-v3",
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 8
  }
}
```

---

## 📊 Models

### List Models

**Endpoint**: `GET /v1/models`

Returns a list of available models.

#### Example Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "deepseek-chat",
      "object": "model",
      "created": 1677610602,
      "owned_by": "deepseek"
    },
    {
      "id": "qwen-plus",
      "object": "model",
      "created": 1677610602,
      "owned_by": "alibaba"
    }
  ]
}
```

### Retrieve Model

**Endpoint**: `GET /v1/models/{model_id}`

Retrieves a specific model by ID.

#### Example Response

```json
{
  "id": "deepseek-chat",
  "object": "model",
  "created": 1677610602,
  "owned_by": "deepseek",
  "permission": [],
  "root": "deepseek-chat",
  "parent": null
}
```

---

## 📁 Files

### Upload File

**Endpoint**: `POST /v1/files`

Upload a file for use with various endpoints.

#### Request

```bash
curl -X POST https://api.your-domain.com/v1/files \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@myfile.jsonl" \
  -F "purpose=fine-tune"
```

### List Files

**Endpoint**: `GET /v1/files`

Returns a list of files.

### Delete File

**Endpoint**: `DELETE /v1/files/{file_id}`

Deletes a file.

---

## ⚙️ Configuration Parameters

### Chat Completion Parameters

| Parameter | Type | Default | Description |
|-----------|------|:-------:|-------------|
| `temperature` | number | 1.0 | Sampling temperature (0-2). Higher = more random |
| `top_p` | number | 1.0 | Nucleus sampling threshold |
| `max_tokens` | integer | model max | Maximum tokens to generate |
| `stream` | boolean | false | Enable streaming responses |
| `stop` | string/array | null | Stop sequences |
| `presence_penalty` | number | 0 | Penalty for new topics (-2 to 2) |
| `frequency_penalty` | number | 0 | Penalty for repetition (-2 to 2) |

### Model-Specific Limits

| Model | Max Context | Max Output | Price/1M Tokens |
|-------|-------------|------------|-----------------|
| deepseek-chat | 64K | 8K | $0.42 |
| deepseek-reasoner | 64K | 8K | $0.55 |
| qwen-plus | 128K | 8K | $0.22 |
| glm-4 | 128K | 4K | $0.72 |

---

## ⚠️ Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| 400 | Bad Request | Check request parameters |
| 401 | Unauthorized | Verify API key |
| 403 | Forbidden | Check permissions |
| 429 | Rate Limit Exceeded | Wait and retry |
| 500 | Internal Server Error | Contact support |

### Error Response Format

```json
{
  "error": {
    "message": "Invalid API key",
    "type": "authentication_error",
    "code": "invalid_api_key"
  }
}
```

---

## 📈 Rate Limits

| Tier | Requests/Minute | Tokens/Minute |
|------|-----------------|---------------|
| Free | 10 | 100,000 |
| Pro | 60 | 1,000,000 |
| Enterprise | 600 | 10,000,000 |

---

## 🔒 Security Best Practices

1. **Never expose API keys** in client-side code
2. **Use environment variables** for API keys
3. **Implement rate limiting** in your application
4. **Monitor usage** to detect anomalies
5. **Rotate keys** periodically

---

## 📞 Support

- **Documentation**: [Full API Docs](#)
- **Email**: api-support@your-domain.com
- **Discord**: [Join Community](#)
- **Status Page**: [status.your-domain.com](#)

---

**Last Updated**: 2026-06-16
