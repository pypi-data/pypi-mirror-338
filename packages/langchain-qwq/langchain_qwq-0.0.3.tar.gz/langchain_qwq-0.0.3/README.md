# langchain-qwq

This package contains the LangChain integration with QwQ

## Installation

```bash
pip install -U langchain-qwq
```

And you should configure credentials by setting the following environment variables:

* TODO: fill this out

## Chat Models

`ChatQwQ` class exposes chat models from QwQ.

```python
from langchain_qwq import ChatQwQ

llm = ChatQwQ()
llm.invoke("Sing a ballad of LangChain.")
```
