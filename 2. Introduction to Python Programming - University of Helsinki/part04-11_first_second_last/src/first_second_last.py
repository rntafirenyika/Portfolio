# Returns the first word in the sentence.
def first_word(sentence):
    space_index = sentence.find(" ")
    return sentence[0:space_index]

# Returns the second word in the sentence.
def second_word(sentence):
    spaces = []
    copy_sent = sentence
    tracker = 0
    while copy_sent.find(" ") != -1:
        space_index = copy_sent.find(" ")
        tracker += space_index
        spaces.append(tracker)
        copy_sent = copy_sent[space_index+1:]
        tracker += 1
    if len(spaces) == 1:
        return sentence[spaces[0]+1:]
    return sentence[spaces[0]+1:spaces[1]]

# Returns the last word in the sentence.
def last_word(sentence):
    spaces = []
    copy_sent = sentence
    tracker = 0
    while copy_sent.find(" ") != -1:
        space_index = copy_sent.find(" ")
        tracker += space_index
        spaces.append(tracker)
        copy_sent = copy_sent[space_index+1:]
        tracker += 1    
    return sentence[spaces[-1]+1:]

# test functions
if __name__ == "__main__":
    sentence = "it was"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))