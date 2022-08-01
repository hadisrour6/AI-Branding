import re
import openai


def generate_branding_snippet(prompt: str) -> str:
    # open ai api
    openai.api_key = "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"

    enriched_prompt = f"Generate upbeat branding snippet for {prompt}"

    response = openai.Completion.create(engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=25)

    # extracts the text
    text = response["choices"][0]["text"]

    # Strips white space
    text = text.strip()

    # if last character in sentence is not a punctuation, put a "..."
    if text[-1] not in {"!", ".", "?"}:
        text += '...'

    return text


def generate_keywords(prompt: str) -> list[str]:
    # open ai api
    openai.api_key = "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"

    enriched_prompt = f"Generate related branding keywords for {prompt}"

    response = openai.Completion.create(engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=25)

    # extracts the text
    keywords_text = response["choices"][0]["text"]

    # Strips white space
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-", keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    return keywords_array


