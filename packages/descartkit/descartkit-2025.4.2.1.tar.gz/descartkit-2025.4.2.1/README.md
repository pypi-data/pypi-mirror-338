
# descartkit

### LLM

#### Three steps to use models

##### Step1, llm_config.yaml

matter that needs attention
1. custom_model_name used for models.get_model_instance()
2. custom_model_name.name should specify the name of the model supported by the current company

```yaml
models:
  openai:
    custom_model_name:
      name: "gpt-4o"
      short_name: "OIG4"
      company: "openai"
      max_input_token: 8100
      max_output_token: 2048
      top_p: 0.5
      top_k: 1
      temperature: 0.5
      input_token_fee_pm: 30.0
      output_token_fee_pm: 60.0
      train_token_fee_pm: 0.0
      keys:
        - name: "openai_key1"
        - name: "openai_key2"

  siliconflow:
    qw-72b-p:
      name: "Qwen/QVQ-72B-Preview"
      short_name: "QW-72B-P"
      company: "siliconflow"
      max_input_token: 8100
      max_output_token: 2048
      top_p: 0.5
      top_k: 1
      temperature: 0.5
      input_token_fee_pm: 30.0
      output_token_fee_pm: 60.0
      train_token_fee_pm: 0.0
      keys:
        - name: "siliconflow_1"

```

##### Step2, llm_keys.yaml

1. The keys name of the model in llm_config.yaml corresponds to llm_keys.yaml one by one

```yaml
keys:
  openai_key1: "xx"
  openai_key2: "xx"
  anthropic_key1: "your_anthropic_api_key_1"
  anthropic_key2: "your_anthropic_api_key_2"
```

##### Step3, load models

```python
from descartkit.llm.config import load_models_from_yaml
from descartkit.llm import LLMClient

async def main():
  
    # The first method
    models = load_models_from_yaml(config_file="examples/llm_config.yaml", keys_file="examples/llm_keys.yaml")
    print(models.list_models())

    resp = await models.get_model_instance("gpt-4o").chat("who r u?")
    print(resp)

    # The second method
    client = LLMClient(config_file="llm_config.yaml", keys_file="llm_keys.yaml")
    print(client.list_models())
    resp = await client.chat("qw-72b-p", "who r u?", system_prompt="")
    print(resp)
    async for chunk in client.chat_stream("qw-72b-p", "who r u?", system_prompt=""):
        print(chunk)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
```
