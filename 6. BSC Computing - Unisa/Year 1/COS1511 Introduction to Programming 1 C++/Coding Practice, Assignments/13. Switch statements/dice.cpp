#include <iostream>
#include <ctime>
using namespace std;

int main()
{
    // Declare variables
    int d1, d2, total;
    char status;

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
    switch (total)
    {
        case 7:
        case 11:
            cout << "You win!" << endl;
            break;
        case 2:
            cout << "Snake eyes!" << endl;
            break;
        case 12:
            cout << "Good shot!" << endl;
            break;
        default:
            cout << "Try again." << endl;
    }
    return 0;
}
