# Source: https://www.geeksforgeeks.org/how-to-make-api-calls-using-python/
#         https://pypi.org/project/Wikipedia-API/
#         https://codeberg.org/zortazert/Python-Projects/src/branch/main/api/free-dictionary.py
#         https://pypi.org/project/wonderwords/

import requests
import wikipediaapi

# --- Get Wikipedia summary ---
def get_wikipedia(wikiPage):
    wikiAccessAgent = wikipediaapi.Wikipedia(user_agent='API_Test (gabrielfernandez@example.com)', language='en')
    return wikiAccessAgent.page(wikiPage)

# --- Get dictionary definitions ---
def get_dictionary(dictionarySetter):
    try:
        dictionaryData = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{dictionarySetter}").json()
        definitions = dictionaryData[0]["meanings"][0]["definitions"]
        return [d["definition"] for d in definitions]
    except Exception:
        return ["No definitions found."]

# --- Get thesaurus synonyms and antonyms ---
def get_thesaurus(dictionarySetter):
    try:
        dictionaryData = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{dictionarySetter}").json()
        synonyms = dictionaryData[0]["meanings"][0].get("synonyms", [])
        antonyms = dictionaryData[0]["meanings"][0].get("antonyms", [])
        return synonyms, antonyms
    except Exception:
        return [], []

# --- Optional: Get a random word (if you still use wonderwords) ---
from wonderwords import RandomWord

def generate_randWord():
    randomizer = RandomWord()
    return randomizer.word()

# --- Optional: Manual test (CLI) ---
def main():
    while True:
        query = input("Enter a word (or 'exit'): ").strip()
        if query.lower() == "exit":
            break
        if query.lower() == "random":
            query = generate_randWord()
            print(f"Random word: {query}")

        print("\n--- Wikipedia ---")
        page = get_wikipedia(query)
        print(page.summary if page.exists() else "No Wikipedia entry found.")

        print("\n--- Dictionary ---")
        definitions = get_dictionary(query)
        for i, d in enumerate(definitions, 1):
            print(f"{i}. {d}")

        print("\n--- Thesaurus ---")
        syns, ants = get_thesaurus(query)
        print("Synonyms:", ", ".join(syns) if syns else "None")
        print("Antonyms:", ", ".join(ants) if ants else "None")
        print("\n" + "-" * 50 + "\n")

if __name__ == '__main__':
    main()
