#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int i, j , k;
    cout << "Enter 3 numbers: ";
    cin >> i >> j >> k;

    if (i + j == k)
    {
        cout << i << " + " << j << " = " << k << endl;
    }
    else if (i + k == j)
    {
        cout << i << " + " << k << " = " << j << endl;
    }
    else if (k + j == i)
    {
        cout << k << " + " << j << " = " << i << endl;
    }
    else
    {
        cout << "None of the sum of the numbers equals the remaining number" << endl;
    }

    cout << endl;

    return 0;
}
