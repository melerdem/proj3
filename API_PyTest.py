# Source: https://www.geeksforgeeks.org/how-to-make-api-calls-using-python/
#         https://pypi.org/project/Wikipedia-API/
#         https://codeberg.org/zortazert/Python-Projects/src/branch/main/api/free-dictionary.py
#         https://pypi.org/project/wonderwords/

import requests
import json
import wikipediaapi
from wonderwords import RandomWord

def get_wikipedia(wikiPage):
    wikiAccessAgent = wikipediaapi.Wikipedia(user_agent='API_Test (gabrielfernandez@ufl.edu)', language='en')

    try:
        page = wikiAccessAgent.page(wikiPage)

    except:
        print("The Wikipedia page could not be accessed")
        #page = wikiAccessAgent.page("error")

    return page

def get_dictionary(dictionarySetter):
    dictionaryData = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{dictionarySetter}").json()

    # Select in each data structure by naming one of the entries (like sub directories)
    print(dictionaryData[0]["word"] + " " + "(Definition)")
    print("--------------------------------------------------")

    # List all of the different definitions
    counter = 0
    for i in dictionaryData[0]["meanings"][0]["definitions"]:
        counter += 1
        print(counter, end=".) ")
        print(i["definition"], end="\n\n")

    return dictionarySetter

def get_thesaurus(dictionarySetter):
    dictionaryData = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{dictionarySetter}").json()
    #thesaurusData = Thesaurus(dictionarySetter)

    # Select the synonyms (and antonyms)
    # Synonyms
    try:
        numSym = len(dictionaryData[0]["meanings"][0]["synonyms"])
        
        
        print(dictionarySetter + " " + "(Synonyms)")
        print("--------------------------------------------------")
            
        for synonym in dictionaryData[0]["meanings"][0]["synonyms"]:
            print(synonym, end="\n\n")
        print()

    except:
        print("No synonym entry found in Thesaurus", end="\n\n")

    print()

    # Antonyms
    try:
        numAnt = len(dictionaryData[0]["meanings"][0]["synonyms"])

        print(dictionaryData[0]["word"] + " " + "(Antonyms)")
        print("--------------------------------------------------")

        for antonym in dictionaryData[0]["meanings"][0]["antonyms"]:
            print(antonym, end="\n\n")
        print()

    except:
         print("No antonym entry found in Thesaurus")

# Separating this into an indivudal function may never be necessary, but it should
# be useful if we need to get a random word any time other than at the beginning of
# inputting a new word
def generate_randWord(randomizer):
    return randomizer.word()


def main():
    randomizer = RandomWord()

    # User Input
    print("Input: ",end="")
    queryPhrase = input()

    if (queryPhrase == "do random"):
        queryPhrase = randomizer.word()

    print()

    # Perform Wikipedia checking operation
    try:
        page = get_wikipedia(queryPhrase)

        if page.exists():     
            # Wikipedia
            print(page.title + " " + "(Wikipedia)")
            print("--------------------------------------------------")
            print(page.summary)
            print()
        else:
            print('Failed to fetch page from API.')

            print()
    except:
        print("No entry found on Wikipedia")

    # Divide the text
    print()
    print("- - - - - - - - - -")
    print('\n')

    # Perform the Dictionary checking operation
    try:
        get_dictionary(queryPhrase)
    except:
        print("No entry found in Dictionary")
    
    # Divide the text
    print('\n')
    print("- - - - - - - - - -")
    print('\n')

    # Perform the Thesaurus checking operation
    try:
        get_thesaurus(queryPhrase)
    except:
        print(end="")

    # Print again to separate the request to press a key to continue the program
    print('\n')        

if __name__ == '__main__':
    main()