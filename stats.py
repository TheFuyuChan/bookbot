def get_word_count(text):
    return len(text.split())

def char_count(text):
    chars = set()
    count = {}
    for char in text.lower():
        if char in chars:
            count[char] += 1
        else:
            chars.add(char)
            count[char] = 1
    return count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list = []
    true_list = []
    for e in dict:
        if e.isalpha():
            list.append({"char": e, "num": dict[e]})
    list.sort(reverse=True, key=sort_on)
    for i in list:
        true_list.append(f"{i['char']}: {i['num']}")
    return true_list
