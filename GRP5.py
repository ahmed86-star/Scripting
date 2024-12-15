# FILE: 2252_AhmedAbdirahman_Lesson06.py
# NAME: Random Numbers Analyzer
# AUTHOR(s): Abdirahman Ahmed
# DATE: 11/16/2024


import random


pirate_dict = {
    "hello": "ahoy",
    "hi": "yo-ho-ho",
    "my": "me",
    "friend": "bucko",
    "sir": "matey",
    "where": "whar",
    "is": "be",
    "the": "th'",
    "there": "thar",
    "you": "ye"
}

#  
def convert_ing(word):
    if word.endswith("ing"):
        return word[:-3] + "in'"
    return word


def insert_arr(sentence):
    if random.choice([True, False]):  # 50% chance
        sentence += " Arr!"
    return sentence

#  translate a single word
def translate_word(word):
 
    punctuation = ""
    if word.endswith((".", ",")):
        punctuation = word[-1]
        word = word[:-1]

    
    translated_word = pirate_dict.get(word.lower(), word)
    translated_word = convert_ing(translated_word)

    
    if word[0].isupper():
        translated_word = translated_word.capitalize()

  # punctuation back
    return translated_word + punctuation

# Main function to run the translator
def pirate_translator(phrase):
    words = phrase.split()  
    pirate_words = [translate_word(word) for word in words] 
    translated_sentence = " ".join(pirate_words)  # Join words into a sentence
    translated_sentence = insert_arr(translated_sentence)  
    return translated_sentence


print("Welcome to the Pirate Translator! Enter a phrase to see it in pirate speak.")
user_input = input("Enter your phrase: ")
print("Pirate Speak:", pirate_translator(user_input))

