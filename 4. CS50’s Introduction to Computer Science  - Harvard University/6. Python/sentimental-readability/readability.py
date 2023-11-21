def main():
    # Prompt user for text and prints out the grade using Coleman-Liau formula.
    text = input("Text: ")
    print(f"Grade {grade(text)}")


def grade(text):
    num_letters = count_letters(text)
    num_words = count_words(text)
    num_sentences = count_sentences(text)
    index = round(0.0588 * (num_letters/num_words*100) - 0.296 * (num_sentences/num_words*100) - 15.8)
    if index < 1:
        return "Before Grade 1"
    elif index >= 16:
        return "Grade 16+"
    else:
        return f"Grade {index}"


def count_letters(text):
    # Count number of letters in text.
    letters_count = 0
    for char in text:
        if char.isalnum():
            letters_count += 1
    return letters_count


def count_words(text):
    # Count number of words in text.
    return len(text.split(" "))


def count_sentences(text):
    # Count number of sentences in text.
    sentence_count = 0
    for char in text:
        if char in [".", "!", "?"]:
            sentence_count += 1
    return sentence_count


if __name__ == "__main__":
    main()