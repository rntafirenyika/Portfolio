// Swaps the first letters of two words
#include <string>
#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    string word1 , word2, swapped;
    char letter1 , letter2;

    // Prompt user for the words
    cout << "Enter two words: ";
    cin >> letter1 >> word1 >> letter2 >> word2;

    // Perform swap
    swapped = letter2 + word1 + " " + letter1 + word2;
    // Print output
    cout << "Spoonerised words: " << swapped << endl;

    return 0;



}
