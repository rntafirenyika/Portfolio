#include <iostream>
using namespace std;

int main()
{
    int hours;
    float charge;
    char vehicle;

    cout << "Hours parked: ";
    cin >> hours;
    cout << "(M)otorcar or (T)ruck: ";
    cin >> vehicle;

    switch (hours)
    {
        case 1:
            charge = 2.00;
            break;
        case 2:
            charge = 3.00;
            break;
        case 3:
        case 4:
        case 5:
            charge = 5.00;
            break;
        default:
            charge = 10.00;
    }
    if (vehicle == 'T' || vehicle == 't')
        charge ++;

    cout.setf(ios::fixed);
    cout.precision(2);
    cout << "Amount Due: R" << charge << endl;

    return 0;
}
