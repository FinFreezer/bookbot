def count_words(string):
    word_list = string.split()
    return len(word_list)

def count_letter_usage(string):
    found_characters = set()
    recurrence = { }

    for char in string:
        if char.lower() not in found_characters and char.lower().isalpha():
            found_characters.add( char.lower() )
            recurrence[ char.lower() ] = 1
        elif ( char.lower().isalpha() ):
            recurrence[ char.lower() ] += 1
        else:
            continue

    """for letter, amount in recurrence.items():
        print(f" '{letter}': {amount} ")"""
    
    sort_by_count(recurrence)
    return recurrence

def sort_by_count(dictionary):
    sorted_list = []
    for letter, amount in dictionary.items():
        sorted_list.append(
            [
            {"name":letter},
            {"num":amount}
            ]
        )

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items[1]["num"]
