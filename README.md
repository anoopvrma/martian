
### Overview

This library is build using Python and Fast API to call different LLM providers.

### Supported Models

- OpenAI
- Anthropic
- Together

### Implementation Details

This library is implemented using FastAPI in Python. 

#### Dependencies

It has dependencies on following Python packages 
- anthropic
- openai
- together
- FastAPI
- uvicorn

#### Structure

```
- api.py
- setup.py
- README.md
- models
    - model.py
- providers
    - base_provider.py
    - openai.py
    - togetherai.py
    - anthropic.py
- exceptions
    - error.py
```

##### api.py

Contains code related to APIs. As of now we have only one API (/complete) to call. This API calls different models based on parameters.

##### setup.py

Contains code to declare package details.

##### models

Builds and provides right model to call to fulfill request.

##### providers

- base_provider.py: contains code for provider interface. All providers must implement this interface so that we can call any provider without much changes at client side.
- openai.py, togetherai.py, anthropic.py : Provider implementation for respective model providers.

##### exceptions

Defines exceptions/errors raised by this package.


### TODO

Logging and metrics to track latency, success rate etc.

### Scaling 

To scale we need to upgrade plans from LLM providers. We can get RateLimitError for current API_KEY

### Design

To support multiple LLM providers without impacting client code, we need to support common interface, which is declared in base_provider package.



