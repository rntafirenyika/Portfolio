// Calculates account balance with interest over 18 years
#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    float runningBalance;
    const float INTEREST_RATE = 0.045;
    const float DEPOSIT = 500;
    const float OPENING_BALANCE = 1000;
    int years = 18, count;

    count = 0;
    runningBalance = OPENING_BALANCE;
    while (count < 18)
    {
        runningBalance = runningBalance + (runningBalance * INTEREST_RATE);
        runningBalance += 500;
        count ++;
    }

    cout.setf(ios::fixed);
    cout.precision(2);
    cout << "The balance on the 18th birthday is R" << runningBalance << endl;
    return 0;
}
