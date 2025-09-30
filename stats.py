def word_count(text):
    words = text.split()
    return len(words)

def char_dict(text):
    char_count = {}
    for character in text:
        char = character.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(d):
    return d["num"]

def to_sorted_list(char_count_dict):
    sorted_list = []
    for ch in char_count_dict:
        sorted_list.append({"char": ch, "num": char_count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    
