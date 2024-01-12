import os
import re
import argparse
from openai import OpenAI


def main():
    print(generate_branding_snippet("coffee"))

    # print("running copy kitt")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args  = parser.parse_args()

    user_input=args.input

    print(f"User input: {user_input}")

    snippet_result = generate_branding_snippet(user_input)

    keywords_result = generate_keywords(user_input)

    # print(snippet_result)
    print(keywords_result)


def generate_branding_snippet(prompt: str) -> str:
    # open ai api
    client = OpenAI(
        api_key=""
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", f"content": f"Generate a 20 word upbeat branding snippet slogan for {prompt} mat buisness."}]
    )
    # extracts the text
    text = response.choices[0].message.content

    # Strips white space
    text = text.strip()

    # if last character in sentence is not a punctuation, put a "..."
    if text[-1] not in {"!", ".", "?"}:
        text += '...'

    return str(text)


def generate_keywords(prompt: str) -> list[str]:
    # open ai api
    client = OpenAI(
        api_key=""
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": f"Generate 6 related keywords for my {prompt} buisness do not use the word {prompt} in them."}]
    )
    # extracts the text
    keywords_text = response.choices[0].message.content


    return str(keywords_text)


def validate_length(prompt: str) -> bool:
    return len(prompt) <= 12


if __name__ == "__main__":

    print(generate_keywords("yoga mats"))
    print(generate_branding_snippet("yoga mats"))
