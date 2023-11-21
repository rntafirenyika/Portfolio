#include <iostream>
using namespace std;

int main()
{
    float sales = 0.0;
    float commission = 0.0;

    cout << "Enter a sales amount: ";
    cin >> sales;

    while (sales > 0.0)
    {
        commission = sales * 0.1;
        cout << commission << endl;
        cout << "Enter the next sales amount: ";
        cin >> sales;
    }
    // endwhile

    return 0;
}
