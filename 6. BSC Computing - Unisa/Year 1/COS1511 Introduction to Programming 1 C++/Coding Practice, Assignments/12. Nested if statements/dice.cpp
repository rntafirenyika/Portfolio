#include <iostream>
#include <ctime>
using namespace std;

int main()
{
    // Declare variables
    int d1, d2, total;

    // seed the random number generator with the current time
    srand(time(0));

    // roll two dices
    d1 = 1 + rand() % 6;
    d2 = 1 + rand() % 6;

    // calculate the total and display
    total = d1 + d2;
    cout << "Die 1 roll: " << d1 << endl;
    cout << "Die 2 roll: " << d2 << endl;

    // print results based on total
    if (total == 7 || total == 11)
        cout << "You win!" << endl;
    else if (total == 2)
        cout << "Snake eyes!" << endl;
    else if (total == 12)
        cout << "Good shot!" << endl;
    else
        cout << "Try again." << endl;

    return 0;
}
