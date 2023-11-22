"""
____________________________________________________________________
Author: Ronaldo Venancio
Assignments in CSE 111
Purpose: L04 Prove: Milestone.
I created an extra function get_adjective()

Your program’s output should be similar to the sample run output shown here. However, because your program randomly chooses the determiners, nouns, and verbs, your program will generate different sentences than the six shown here.
You may add other functions if you find them helpful. 
The get_preposition function must randomly choose a preposition from a list and return the randomly chosen preposition. The get_prepositional_phrase function must make a prepositional phrase by calling the get_preposition, get_determiner, and get_noun functions.
> python sentences.py
One girl talked for the car.
A bird drinks off one child.
The child will run on the car.
Some dogs drank above many rabbits.
Some children laugh at many dogs.
Some rabbits will talk about some cats.
____________________________________________________________________
"""
import random

def main():
    tenses = ["single_past", "single_present", "single_future", "plural_past", "plural_present", "plural_future"]
    #for i in range(0,6):

    for item in tenses:
        # Create a list of strings and assign
        # the list to a variable named words.
        tense = str(item)
        words = ["boy", "girl", "cat", "dog", "bird", "house"]
        prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
        preposition = random.choice(prepositions)
        quantities = [0, 1]
        quantity = int(random.choice(quantities))
        """tenses = ["single_past", "single_present", "single_future", "plural_past", "plural_present", "plural_future"]"""
        #tenses = ["single_past", "single_present", "single_future"]
        #tense = str(random.choice(tenses))
        # Call the random.choice function which will choose
        # one string from the words list. Store the chosen
        # string in a variable named word.
        word = random.choice(words)
        # Call the capitalize method which will
        # capitalize the first letter of the word.
        cap_word = word.capitalize()
        #print(f"{cap_word}")
        #print(f"{quantity}")
        #print(f"{tense}")
        sentence = make_sentence(quantity,tense)
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
    If tense is "single_past",this function will return one of these ten verbs:"drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"
    If tense is "single_present" and quantity is 1, this function will return one of these ten verbs:
    "drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"
    If tense is "single_present" and quantity is NOT 1, this function will return one of these ten verbs:"drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"
    If tense is "single_future", this function will return one ofthese ten verbs: "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "single_past" or "plural_past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    if tense == "single_present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    if tense == ("single_present" and quantity != 1) or "plural_present":
        verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    if tense == "single_future" or "plural_future":
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    # Randomly choose and return a determiner.
    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition


def get_adjective():
    """Return a randomly chosen adjective
    from this list of prepositions:
        "wonderful", "beautiful", "tall", "short", "small",
        "big", "brave", "alert", "colossal", "adorable",
        "abrupt", "acidic", "agressive", "bored", "bright",
        "confused", "corny", "costly", "cruel", "diminutive",
        "determined", "courageus", "dilapited", "diminutive", "distressed",
        "disturbed", "funny", "handsome", "lovely", "friendly", "perfect", "narrow", "perplexed", "upset", "impresssionabel"

    Return: a randomly chosen preposition.
    """
    adjectives = ["wonderful", "beautiful", "tall", "short", "small",
        "big", "brave", "alert", "colossal", "adorable",
        "abrupt", "acidic", "agressive", "bored", "bright",
        "confused", "corny", "costly", "cruel", "diminutive",
        "determined", "courageus", "dilapited", "diminutive", "distressed",
        "disturbed", "funny", "handsome", "lovely", "friendly", "perfect", "narrow", "perplexed", "upset", "impresssionabel"]
    adjective = random.choice(adjectives)
    return adjective


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """

    prep = str(get_preposition())
    word = str(get_determiner(quantity))
    noun = str(get_noun(quantity))
    prepositional_phrase = str(f"{prep} {word} {noun}")
    return prepositional_phrase


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    word = str(get_determiner(quantity))
    adjec = str(get_adjective())
    noun = str(get_noun(quantity))
    verb = str(get_verb(quantity,tense))
    prep_phrase = str(get_prepositional_phrase(quantity))
    cap_word = word.capitalize()
    sentence = f"{cap_word} {adjec} {noun} {verb} {prep_phrase}."
    return sentence


# Start this program by
# calling the main function.
main()