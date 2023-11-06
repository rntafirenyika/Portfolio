# Returns a list containing all the words in the file which match the search term.

# Function to read file
def read_file():
    words = []
    with open("words.txt") as file:
        for row in file:
            words.append(row.strip())
    return words
    

def dotwild(search_term):
    words = read_file()
    ind =[]
    for i in range(len(search_term)):
        if search_term[i].isalpha():
            ind.append((i, search_term[i]))
                   
    for word in words:
        if len(word) == len(search_term) and word[ind[0][0]] == ind[0][1] and word[ind[1][0]] == ind[1][1]:
            results.append(word)


def find_words(search_term: str):
    words = read_file()
    
    global results
    results = []
    
    # Find only words which match the search term exactly.
    if "*" not in search_term or "." not in search_term:
        for word in words:
            if word == search_term:
                results.append(word)
    
    # Find words that has * wildcats - start with or end with.
    if search_term.startswith("*"):
        for word in words:
            if word.endswith(search_term[1:]):
                results.append(word)
    elif search_term.endswith("*"):
        for word in words:
            if word.startswith(search_term[:-1]):
                results.append(word)
    
    # Find words with . wildcats - any single character is acceptable in its place.
    if search_term.count(".") >= 1:
        dotwild(search_term)
    return results

if __name__ == "__main__":
    """
    # Using recursion
    def dotwild(search_term):
        words = read_file()
                
        i = ord('a')
        while i <= 122:
            nch = chr(i)
            if search_term.count(".") == 1:
                nsearch_term = search_term.replace(".", nch)
                for word in words:
                    if word == nsearch_term:
                        results.append(word)
            else:
                nsearch_term = search_term.replace(".", nch, 1)
                dotwild(nsearch_term)
            i += 1
    """ 