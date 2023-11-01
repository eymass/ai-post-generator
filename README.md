# Post AI Generation for Products Comparison


[![openai version](https://a11ybadges.com/badge?logo=openai)](https://pypi.org/project/openai/0.28.1/)


POST Generator is a Python app based on OpenAI GPT models, 
that generates a blog post which compares 
between number of products on the same category.
It uses the [OpenAI API](https://platform.openai.com/docs/introduction) to generate the post text.

this app is fully customizable, you can change the number of products to compare, 
and you can add as much as context you want to finetune the model.

This app will provide with a full .json file with the post body.

## Requirements

1. Python 3.7+
2. OpenAI token

## Installation & Usage
```pip install -r requirements.txt```

## Basic Usage

```python
generate.py "best 3 AI image generation of 2023" "img_gen1" 3
```

