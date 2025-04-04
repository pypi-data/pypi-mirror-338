# Natural Programming with Python

A natural programming inspired decorator for easy LLM function calls with Pydantic parsing.

## Installation

```bash
pip install naturalpy
```

## Overview

`natpy` provides a seamless way to integrate LLMs into your Python functions using simple decorators. It transforms your functions into natural language interfaces to AI models, handling all the complexity of API calls and response parsing.

Built on top of the [instructor](https://github.com/jxnl/instructor) library, `natpy` uses type annotations and docstrings to convert function calls into structured LLM queries and properly typed responses.

## Features

- Simple `@natural` decorator syntax
- Uses function docstrings as prompts
- Parameter substitution with `${param_name}` syntax
- Automatic response parsing based on return type annotations
- Supports complex return types (Lists, Dicts, Pydantic models)
- Configurable model parameters (temperature, max tokens, etc.)

## Quick Start

First, set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=your-api-key-here
```

Then, use the `@natural` decorator in your code:

```python
from naturalpy import natural
from typing import List

@natural
def generate_ideas(topic: str, count: int) -> List[str]:
    """
    Generate ${count} creative ideas related to ${topic}.
    Each idea should be innovative and practical.
    """

# Call like a normal function
ideas = generate_ideas("sustainable urban gardening", 3)
print(ideas)  # ['Vertical hydroponic systems for balconies', ...]
```

## Advanced Usage

### Returning Complex Types

The `@natural` decorator supports a variety of return types:

```python
from typing import Dict, List
from pydantic import BaseModel

# Return a dictionary
@natural
def analyze_sentiment(text: str, aspects: List[str]) -> Dict[str, float]:
    """
    Analyze the following text: "${text}"
    
    Give me a sentiment score for each of these aspects:
    ${aspects}
    
    For each aspect, provide a score between 0 and 1 where 0 is very negative
    and 1 is very positive.
    """

# Return a Pydantic model
class MovieRecommendation(BaseModel):
    title: str
    year: int
    director: str
    why_recommended: str

@natural
def recommend_movie(genres: List[str], mood: str) -> MovieRecommendation:
    """
    Recommend a movie that matches these genres: ${genres}
    The viewer is in a ${mood} mood.
    """
```

### Customizing LLM Parameters

You can customize the LLM parameters by passing them to the decorator:

```python
@natural(
    model="gpt-4o-2024-08-06",
    temperature=0.9,
    max_tokens=500
)
def write_story(plot: str, style: str) -> str:
    """
    Write a short story based on this plot:
    ${plot}
    
    Write in the style of ${style}.
    """
```

## Error Handling

The decorator includes robust error handling:

- Missing docstring: `ValueError` is raised if a function has no docstring
- Missing return type: `TypeError` is raised if a function has no return type annotation
- Invalid parameter references: `RuntimeError` is raised if the docstring references parameters that don't exist
- API or parsing errors: `RuntimeError` is raised with details about the failure

## How It Works

1. The decorator extracts the function's docstring and uses it as a prompt
2. It substitutes `${parameter_name}` placeholders with actual argument values
3. It determines the expected return type from the function's annotations
4. It calls the OpenAI API with the assembled prompt
5. The response is parsed according to the expected type using instructor
6. The parsed result is returned from the function call

## Requirements

- Python 3.8+
- OpenAI API key
- instructor
- pydantic

## License

MIT License
