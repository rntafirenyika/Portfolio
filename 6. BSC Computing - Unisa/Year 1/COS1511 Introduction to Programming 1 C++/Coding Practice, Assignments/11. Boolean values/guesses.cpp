// Guessing game
#include <iostream>
using namespace std;

int main()
{
    // Declare constants and variables
    int numberGuess;
    const int SECRET = 12;
    const int TRIES = 10;
    bool found;

    found = false;

    // Repeat a max of Tries if guessed number is incorrect
    for (int i = 1; i <= TRIES; i++ )
    {
        cout << "Guess a number between 1 and 100: ";
        cin >> numberGuess;

        found = numberGuess == SECRET;

        if (found)
        {
            cout << "Well done! You got the number in " << i << " guesses." << endl;
            break;
        }
        else if (i == TRIES)
        {
            cout << "Tough luck! Your 10 chances are over." << endl;
        }
        else
        {
            cout << "Incorrect guess, please try again" << endl;
        }
        cout << endl;
    }

    return 0;
}
