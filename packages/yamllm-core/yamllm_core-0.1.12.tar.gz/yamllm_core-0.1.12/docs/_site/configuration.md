# Configuration Guide

## Overview

YAMLLM requires a YAML configuration file with specific sections to define LLM settings and behaviors. This guide details all required configuration sections and their options.

## Required Configuration Sections

A complete YAMLLM configuration must include these sections:

```yaml
# LLM Provider Settings
provider:
  name: "mistralai"  # Required: openai, google, deepseek, or mistralai
  model: "mistral-small-latest"  # Required: model identifier
  api_key: ${MISTRAL_API_KEY}  # Required: use environment variable
  base_url: "https://api.mistral.ai/v1/"  # Optional: custom endpoint

# Model Configuration
model_settings:
  temperature: 0.7
  max_tokens: 1000
  top_p: 1.0
  frequency_penalty: 0.0
  presence_penalty: 0.0
  stop_sequences: []
  
# Request Settings
request:
  timeout: 30
  retry:
    max_attempts: 3
    initial_delay: 1
    backoff_factor: 2
    
# Context Management
context:
  system_prompt: "You are a helpful assistant"
  max_context_length: 16000
  memory:
    enabled: true
    max_messages: 10
    conversation_db: "yamllm/memory/conversation_history.db"
    vector_store:
      index_path: "yamllm/memory/vector_store/faiss_index.idx"
      metadata_path: "yamllm/memory/vector_store/metadata.pkl"
      top_k: 2
    
# Output Formatting
output:
  format: "text"  # text, json, or markdown
  stream: true

# Logging Configuration
logging:
  level: "INFO"
  file: "yamllm.log"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Tool Management
tools:
  enabled: false
  tool_timeout: 10
  tool_list: ['calculator', 'web_search']

# Safety Settings
safety:
  content_filtering: true
  max_requests_per_minute: 60
  sensitive_keywords: []
```

## Section Details

### Provider Settings

| Setting | Type | Required | Description |
|---------|------|----------|-------------|
| name | string | Yes | LLM provider name |
| model | string | Yes | Model identifier |
| api_key | string | Yes | API key (use env vars) |
| base_url | string | No | Custom API endpoint |

### Model Settings

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| temperature | float | Yes | 0.7 | Response randomness |
| max_tokens | integer | Yes | 1000 | Max response length |
| top_p | float | Yes | 1.0 | Nucleus sampling |
| frequency_penalty | float | Yes | 0.0 | Token frequency penalty |
| presence_penalty | float | Yes | 0.0 | Token presence penalty |
| stop_sequences | list | Yes | [] | Stop sequence tokens |

### Request Settings

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| timeout | integer | Yes | 30 | Request timeout (seconds) |
| retry.max_attempts | integer | Yes | 3 | Max retry attempts |
| retry.initial_delay | integer | Yes | 1 | Initial retry delay |
| retry.backoff_factor | integer | Yes | 2 | Retry backoff multiplier |

### Context Management

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| system_prompt | string | Yes | - | System context |
| max_context_length | integer | Yes | 16000 | Max context tokens |
| memory.enabled | boolean | Yes | true | Enable memory |
| memory.max_messages | integer | Yes | 10 | History size |
| memory.conversation_db | string | Yes | - | SQLite DB path |
| memory.vector_store.* | object | Yes | - | Vector store settings |

### Output Settings

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| format | string | Yes | "text" | Response format |
| stream | boolean | Yes | true | Enable streaming |

### Logging Settings

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| level | string | Yes | "INFO" | Log level |
| file | string | Yes | "yamllm.log" | Log file path |
| format | string | Yes | - | Log format string |

### Tool Settings

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| enabled | boolean | Yes | false | Enable tools |
| tool_timeout | integer | Yes | 10 | Tool timeout |
| tool_list | list | Yes | [] | Available tools |

### Safety Settings

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| content_filtering | boolean | Yes | true | Enable filtering |
| max_requests_per_minute | integer | Yes | 60 | Rate limit |
| sensitive_keywords | list | Yes | [] | Blocked keywords |

## Environment Variables

Use environment variables for sensitive data:

```yaml
provider:
  api_key: ${PROVIDER_API_KEY}
```

## Provider-Specific Examples

See the `.config_examples` directory for complete provider-specific configurations:
- `openai_config.yaml`
- `google_config.yaml`
- `deepseek_config.yaml`
- `mistral_config.yaml`