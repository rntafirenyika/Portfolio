// Simple cheque account
#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    float balance, transaction;

    // Prompt for opening balance
    cout << "Opening balance: ";
    cin >> transaction;
    balance += transaction;

    // Loop to prompt for a transaction and adjust balance accordingly until 0 is entered.
    do
    {
        cout.setf(ios::fixed);
        cout.precision(2);
        cout << "You balance is now: R" << balance << endl;
        cout << endl;

        cout << "Enter amount, positive values for Deposits and negative for cheques: ";
        cin >> transaction;
        balance += transaction;
    }
    while (transaction != 0);

    return 0;
}
