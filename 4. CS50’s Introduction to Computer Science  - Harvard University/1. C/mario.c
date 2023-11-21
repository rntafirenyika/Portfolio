#include <cs50.h>
#include <stdio.h>

//  Prompts user for a positive integer between 1 and 8, inclusive. Recreates Mario pyramid using hashes (#) for bricks.

int main(void)
{
    // Get height of pyramid from user as an interger
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n <= 0 || n > 8);

    //printing the pyramid
    int m = n - 1;
    for (int i = 1; i <= n; i++)
    {
        // print required spaces
        for (int j = m; j > 0; j--)
        {
            printf(" ");
        }

        // Print #
        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }

        printf("\n");
        m--;
    }

}