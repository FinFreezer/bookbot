def count_words(string):
    word_list = string.split()
    return len(word_list)

def count_letter_usage(string):
    found_characters = set()
    recurrence = { }

    for char in string:
        if char.lower() not in found_characters:
            found_characters.add( char.lower() )
            recurrence[ char.lower() ] = 1
        else:
            recurrence[ char.lower() ] += 1

    for letter, amount in recurrence.items():
        print(f" '{letter}': {amount} ")