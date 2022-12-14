import re
import openai


def generate_branding_snippet(prompt: str) -> str:
    # open ai api
    openai.api_key = ""

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
    openai.api_key = ""

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

def snippet_and_slogan():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args  = parser.parse_args()

    user_input=args.input

    print(f"User input: {user_input}")

    snippet_result = generate_branding_snippet(user_input)
    keywords_result = generate_keywords(user_input)
    
    return f"Slogan: {snippet_result}. Kewords: {keywords_result}"

