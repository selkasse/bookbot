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
