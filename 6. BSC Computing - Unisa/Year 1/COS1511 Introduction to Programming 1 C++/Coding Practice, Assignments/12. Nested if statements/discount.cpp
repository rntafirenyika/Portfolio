#include <iostream>
using namespace std;

int main()
{
    float discount, amount, netAmount;

    cout << "Amount Spent: ";
    cin >> amount;

    if (amount >= 200)
        discount = 0.5;
    else if (amount >= 100)
        discount = 0.4;
    else if (amount >= 70)
        discount = 0.3;
    else if (amount >= 50)
        discount = 0.2;
    else
        discount = 0.1;

    netAmount = amount - amount * discount;

    cout.setf(ios::fixed);
    cout.precision(2);
    cout << "Discounted amount: R" << netAmount << endl;

    return 0;
}
