# langchain-litellm

This package contains the [LangChain](https://github.com/langchain-ai/langchain) integration with [LiteLLM](https://github.com/BerriAI/litellm)

## Installation

```bash
pip install -qU langchain-litellm
```

## Chat Models

`ChatLiteLLM` class exposes chat models from [LiteLLM](https://github.com/BerriAI/litellm).

```python
from langchain_litellm.chat_models import ChatLiteLLM
from langchain_core.messages import HumanMessage
messages = [
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    )
]
chat(messages)
```

## `ChatLiteLLM` also supports async and streaming functionality:
```python
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
await chat.agenerate([messages])
chat = ChatLiteLLM(
    streaming=True,
    verbose=True,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)
chat(messages)
```