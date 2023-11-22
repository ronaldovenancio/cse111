"""
____________________________________________________________________
Author: Ronaldo Venancio
Assignments in CSE 111
Purpose: L03 Prove: Milestone.

Your program’s output should be similar to the sample run output shown here. However, because your program randomly chooses the determiners, nouns, and verbs, your program will generate different sentences than the six shown here.
> python sentences.py
The cat laughed.
Some girls thought.
One man eats.
Many dogs run.
The woman will think.
Many men will write.
____________________________________________________________________
"""
import random

def main():

    for i in range(0,6):
        # Create a list of strings and assign
        # the list to a variable named words.
        words = ["boy", "girl", "cat", "dog", "bird", "house"]
        quantities = [0, 1]
        quantity = int(random.choice(quantities))
        tenses = ["present", "past", "future"]
        tense = str(random.choice(tenses))
        # Call the random.choice function which will choose
        # one string from the words list. Store the chosen
        # string in a variable named word.
        word = random.choice(words)
        # Call the capitalize method which will
        # capitalize the first letter of the word.
        cap_word = word.capitalize()
        #print(f"{cap_word}")
       # print(f"{quantity}")
       # print(f"{tense}")
        sentence = make_sentence(quantity, tense)
        print(f"{sentence}")
    pass

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    """Return a randomly chosen verb. 
    If tense is "past",this function will return one of these ten verbs:"drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
    "drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
    "drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one ofthese ten verbs:
    "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    if tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"]
    if tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    if tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    # Randomly choose and return a determiner.
    verb = random.choice(verbs)
    return verb


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    word = str(get_determiner(quantity))
    noun = str(get_noun(quantity))
    verb = str(get_verb(quantity,tense))
    cap_word = word.capitalize()
    sentence = f"{cap_word} {noun} {verb}."
    return sentence


# Start this program by
# calling the main function.
main()