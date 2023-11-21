#include <cs50.h>
#include <stdio.h>

// Calculates the number of years required for the population to grow from the start size to the end size.

int main(void)
{
    // Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // Calculate number of years until we reach threshold
    int y = 0;
    float currentpop;

    if (end_size == start_size)
    {
        y = 0;
    }

    else
        do
        {
            start_size = start_size + (start_size / 3) - (start_size / 4);
            y++;
        }
        while (start_size < end_size);

    // Print number of years
    printf("Years: %i\n", y);

}
