// Works out which letter of the alphabet a given upper case letter represents.
#include <string>
#include <iostream>
using namespace std;

int main()
{
    // Declare variables and constants
    char letter;
    int number;
    const int START = 64;

    // Prompt user for output
    cout << "Enter an upper case letter: ";
    cin >> letter;

    // calculate the letter number
    number = letter - START;

    // Print message
    cout << letter << " is in position " << number << " in the alphabet" << endl;

    return 0;
}
