# Question 10 -
# Write a program to count the number of verbs, nouns, pronouns, and adjectives in a given particular phrase or
# paragraph, and return their respective count as a dictionary.

# Note -
# 1. Write code comments wherever required for code
# 2. You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# -----------------------------------------------------------------------------------------------------------------------------------------
# Solution:
# we are using the spaCy library, which is a popular NLP library in Python, 
# to perform part-of-speech tagging on the given text

import spacy

def count_partsofspeech(text):
    # load the pre trained English Model (en_core_web_sm) and process the text using the nlp object
    try:
        nlp = spacy.load("en_core_web_sm")

    except OSError:
        print("Downloading 'en_core_web_sm' model...")
        spacy.cli.download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")

    doc = nlp(text=text)

    # Creating dictionary of each parts of speech
    parts_of_speech_count = {
        'NOUN' : 0,
        'PRONOUN' : 0,
        'ADJECTIVE' : 0,
        'VERB' : 0
    }

    # Calculating Count of parts of speech
    for token in doc:
        if token.pos_ in parts_of_speech_count:
            parts_of_speech_count[token.pos_] += 1

    return parts_of_speech_count


if __name__ == "__main__":
    input_text = input("Enter The Text:\n")
    print(f"The text is: {input_text}\n")
    print(f"Count of parts of speech : {count_partsofspeech(input_text)}\n")