// Display debit or credit depending on balance
#include <iostream>
using namespace std;

int main ()
{
    int balance;
    cout << "Balance: ";
    cin >> balance;

    if (balance >= 0)
    {
        cout << "Credit" << endl;
    }
    else
    {
        cout << "Debit" << endl;
    }

    return 0;
}
