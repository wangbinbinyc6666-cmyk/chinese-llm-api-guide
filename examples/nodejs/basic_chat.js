/**
 * BridgeAPI - Chinese LLM API Examples
 * Basic chat completion with DeepSeek V3.2
 *
 * Usage:
 *   npm install openai
 *   node basic_chat.js
 */

const OpenAI = require("openai");

// Initialize client (replace with your API key and domain)
const client = new OpenAI({
  apiKey: "your-api-key-here",
  baseURL: "https://api.bridgeapi.io/v1"  // Replace with your domain
});

async function main() {
  const response = await client.chat.completions.create({
    model: "deepseek-chat",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "Explain quantum computing in simple terms" }
    ],
    temperature: 0.7,
    max_tokens: 1000
  });

  console.log(response.choices[0].message.content);
  console.log(`\nTokens used: ${response.usage.total_tokens}`);
  console.log(`Estimated cost: ~$${(response.usage.total_tokens * 0.00000063).toFixed(4)}`);
}

main();
