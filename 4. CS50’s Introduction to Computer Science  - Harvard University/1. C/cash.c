#include <cs50.h>
#include <stdio.h>

// Prompts the user for the number of cents that a customer is owed and then prints the smallest number of coins with which that change can be made.

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // Prompt user for change owed
    int c;
    do
    {
        c = get_int("Change owed: ");
    }
    while (c < 0);
    return c;
}

int calculate_quarters(int cents)
{
    // Calculate number of quarters in change
    int q = cents / 25;
    return q;
}

int calculate_dimes(int cents)
{
    // Calculate number of dimes in change
    int d = cents / 10;
    return d;
}

int calculate_nickels(int cents)
{
    // Calculate number of nickels in change
    int n = cents / 5;
    return n;
}

int calculate_pennies(int cents)
{
    // Calculate number of pennies in change
    int P = cents / 1;
    return P;
}
