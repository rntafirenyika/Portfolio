#include <iostream>
using namespace std;

int main()
{
    // Declare variables and constants
    int year;
    const int THRESHOLD = 1945;
    const float ENTRANCE_FEE = 20.0;

    // Prompt user for date of birth
    cout << "When were you born? ";
    cin >> year;

    // Check if user qualifies for free entry or must pay
    if (year < THRESHOLD)
        cout << "Free entry";
    else
        cout << "Entrance fee R" << ENTRANCE_FEE;
    cout << endl;
}
