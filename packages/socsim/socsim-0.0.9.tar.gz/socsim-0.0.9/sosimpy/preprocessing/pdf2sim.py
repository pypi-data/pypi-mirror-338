from markitdown import MarkItDown
import re
from openai import OpenAI
import os

# perhaps try docling or marker (https://github.com/VikParuchuri/marker?utm_source=chatgpt.com) in the future
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key='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')

# paper_path = "papers/selective-exposure.pdf"
paper_path = "papers/transformers.pdf"

def clean_newlines(text):
    # Replace newlines that are not followed by another newline with a space
    cleaned_text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # Optionally, strip excessive whitespace
    cleaned_text = re.sub(r'[ \t]+', ' ', cleaned_text)
    return cleaned_text.strip()

def main():
    # PDF to markdown
    md = MarkItDown(enable_plugins=True, llm_client=client, llm_model="gpt-4o") # Set to True to enable plugins
    result = md.convert(paper_path)
    print(result.text_content)
    result = clean_newlines(str(result))
    with open("./analysis/temp.txt", "w") as f:
        f.write(result)

    # think of Agent properties to create

    # Run simulation

if __name__ == '__main__':
    main()