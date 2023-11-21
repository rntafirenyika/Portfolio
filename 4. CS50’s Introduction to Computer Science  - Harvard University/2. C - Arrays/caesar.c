#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Encrypts messages using Caesar’s cipher. Using command-line argument, the user provides what the key should be in the secret message at runtime.

bool only_digits(string input);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // check if the number of arguments are correct
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);
    char ciphertext;

    // Get plaintext from user
    string plaintext = get_string("plaintext:  ");

    printf("ciphertext: ");
    for (int i = 0; i < strlen(plaintext); i++)
    {
        ciphertext = rotate(plaintext[i], key);
        printf("%c", ciphertext);
    }
    printf("\n");
    return 0;
}


bool only_digits(string input)
{
    // check if all characters are digits
    for (int i = 0; i < strlen(input); i++)
    {
        if (isalpha(input[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    char rotated;
    // check if letter is lowercase and apply key
    if (c >= 97 && c <= 122)
    {
        if ((c - 96 + n) % 26 == 0)
        {
            rotated = (c + n);
        }
        else
        {
            rotated = ((c - 96 + n) % 26) + 96;
        }
        return rotated;
    }

    // check if letter is uppercase and apply key
    else if (c >= 65 && c <= 90)
    {
        if ((c - 64 + n) % 26 == 0)
        {
            rotated = (c + n);
        }
        else
        {
            rotated = ((c - 64 + n) % 26) + 64;
        }
        return rotated;
    }

    else
    {
        return c;
    }
}