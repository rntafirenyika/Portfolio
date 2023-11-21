#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for name and prints hello + name
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}