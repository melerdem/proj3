# API.py

import time
import requests
import wikipediaapi
from max_heap import MaxHeap
from BPTreeNode import BPTree  # Assuming B+ Tree is defined in bptree.py

# --- Initialize data structures ---
max_heap = MaxHeap()
bptree = BPTree(degree=3)  # You can adjust the degree of the B+ Tree

# --- Helper Function to Measure Access Time ---
def measure_time(operation, *args):
    start_time = time.time()
    result = operation(*args)
    end_time = time.time()
    return result, end_time - start_time

# --- Get Wikipedia summary ---
def get_wikipedia(wikiPage):
    wikiAccessAgent = wikipediaapi.Wikipedia(user_agent='API_Test (gabrielfernandez@example.com)', language='en')
    return wikiAccessAgent.page(wikiPage)

# --- Get dictionary definitions ---
def get_dictionary(dictionarySetter):
    try:
        dictionaryData = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{dictionarySetter}").json()
        definitions = dictionaryData[0]["meanings"][0]["definitions"]
        
        # Insert definitions into both MaxHeap and B+ Tree
        for definition in definitions:
            max_heap.insert(f"dict:{dictionarySetter}", definition["definition"])
            bptree.insert(f"dict:{dictionarySetter}", definition["definition"])

        # Return definitions for the response
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

# --- Measure Search Time ---
def measure_search_time(query):
    # Measure search times for MaxHeap and B+ Tree
    def max_heap_search():
        return max_heap.search(f"dict:{query}")

    def bptree_search():
        return bptree.search(f"dict:{query}")

    max_heap_result, max_heap_time = measure_time(max_heap_search)
    bptree_result, bptree_time = measure_time(bptree_search)

    # Print comparison of access times
    print(f"MaxHeap Search Result: {max_heap_result}")
    print(f"B+ Tree Search Result: {bptree_result}")
    print(f"MaxHeap Access Time: {max_heap_time} seconds")
    print(f"B+ Tree Access Time: {bptree_time} seconds")

    return max_heap_result, bptree_result, max_heap_time, bptree_time

# --- Optional: Extract max (for heap operations) ---
def extract_max_from_heap():
    return max_heap.extract_max()

# --- Main Function for Testing ---
def main():
    word = input("Enter a word to search for: ").strip()

    # Fetch and insert dictionary results
    get_dictionary(word)

    # Measure search times for both data structures
    measure_search_time(word)

if __name__ == '__main__':
    main()
