#include <iostream>
using namespace std;

bool isLeap(int year);

int main()
{
    int year, month, numDays;

    cout << "Month (1-12): ";
    cin >> month;
    cout << "Year: ";
    cin >> year;

    switch (month)
    {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            numDays = 31;
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            numDays = 30;
            break;
        case 2:
            if (isLeap(year))
                numDays = 29;
            else
                numDays = 28;
            break;
        default:
            cout << "Invalid information";
            numDays = 0;
            break;
    }
    cout << "Month has " << numDays << " days." << endl;

    return 0;
}


bool isLeap(int yearP)
{
    bool leapYear;

    leapYear = false;

    if (yearP % 100 == 0)
    {
        if (yearP % 400 == 0)
            leapYear = true;
    }
    else if (yearP % 4 == 0)
        leapYear = true;

    return leapYear;
}
