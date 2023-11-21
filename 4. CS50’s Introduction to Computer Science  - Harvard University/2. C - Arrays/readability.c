#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

// Takes a text and determines its reading level using the Coleman-Liau index.

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Get input text
    string text = get_string("Text: ");

    int numLetters = count_letters(text);
    int numWords = count_words(text);
    int numSentences = count_sentences(text);
    float index = (0.0588 * (float)numLetters / numWords * 100) - (0.296 * (float)numSentences / numWords * 100) - 15.8;

    if (index < 1.0)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16.0)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }

}


int count_letters(string text)
{
    // Calculate the number of letters in the text
    int numLetters = 0;
    for (int i = 0; strlen(text) >= i; i++)
    {
        // check for uppercase letters and convert to lower
        if (isupper(text[i]))
        {
            text[i] = text[i] + 32;
        }

        // check if letter and count
        if (text[i] >= 97 && text[i] <= 122)
        {
            numLetters++ ;
        }
    }

    return numLetters;
}


int count_words(string text)
{
    // Calculate number of words in the text
    int numWords = 0;
    for (int i = 0; strlen(text) >= i; i++)
    {
        if (text[i] == 32)
        {
            numWords++;
        }
    }

    // Taking into account the last word.
    if (numWords > 1)
    {
        return numWords + 1;
    }

    // Else return zero
    else
    {
        return numWords;
    }
}


int count_sentences(string text)
{
    // Calculate the number of letters in the text
    int numSentences = 0;
    for (int i = 0; strlen(text) >= i; i++)
    {

        // check for sentence end and count
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            numSentences++ ;
        }
    }

    return numSentences;
}