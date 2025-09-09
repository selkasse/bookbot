def get_num_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}

    for i in range(len(text)):
        character = text[i].lower()

        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sort_by_character(character_counts):
    character_dictionaries = []

    for key in character_counts:
        character_dictionary = {}

        character_dictionary["character"] = key
        character_dictionary["num"] = character_counts[key]

        character_dictionaries.append(character_dictionary)

    
    character_dictionaries.sort(reverse=True, key=sort_on)
    return character_dictionaries


