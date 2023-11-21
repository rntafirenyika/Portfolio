#include <iostream>
using namespace std;

int main()
{
    int year;
    bool leapYear;

    leapYear = false;

    cout << "Enter a year: ";
    cin >> year;

    if (year % 100 == 0)
    {
        if (year % 400 == 0)
            leapYear = true;
    }
    else if (year % 4 == 0)
        leapYear = true;

    if (leapYear)
        cout << year << " is a leap year" << endl;
    else
        cout << year << " is not a leap year" << endl;

    return 0;
}
