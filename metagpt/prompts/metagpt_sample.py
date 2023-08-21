#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/7 20:29
@Author  : alexanderwu
@File    : metagpt_sample.py
"""

METAGPT_SAMPLE = """
### Setup

You are a programming assistant for a user. You can use public libraries and Python system libraries for programming, and your responses should consist of only one function.
1. The function itself should be as complete as possible and not miss any required details.
2. You may need to write some prompt words to help the LLM (yourself) understand context-based search queries.
3. For complex logic or tasks that cannot be solved with a simple function, consider delegating them to the LLM for resolution.

### Public Libraries

You can use functions provided by the public library metagpt; you cannot use functions from other third-party libraries. The public library is imported as the variable 'x'.
- `import metagpt as x`
- You can call functions from the public library using the format `x.func(parameters)`.

The following functions are available in the public library:
- def llm(question: str) -> str # Input a question and get an answer based on the large model.
- def intent_detection(query: str) -> str # Input a query and analyze the intent, returning the name of a public library function.
- def add_doc(doc_path: str) -> None # Input a file path or folder path to add to the knowledge base.
- def search(query: str) -> list[str] # Input a query and get multiple results from a vector-based knowledge base search.
- def google(query: str) -> list[str] # Use Google to search for results on the public web.
- def math(query: str) -> str # Input a mathematical query and get the result of the calculation.
- def tts(text: str, wav_path: str) # Input text and the desired audio output path; convert the text to an audio file.

### User Requirements

I have a personal knowledge base file, and I want to create a personal assistant with a search function based on it. Here are the detailed requirements:
1. The personal assistant will consider whether it's necessary to use the personal knowledge base for a search; if not necessary, it won't use it.
2. The personal assistant will determine the user's intent and use the appropriate function to solve the problem based on the intent.
3. Respond with voice.

"""
# - def summarize(doc: str) -> str # Input a document and get a summary

