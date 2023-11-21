//Precision practice
#include <iostream>
using namespace std;

int main( )
{
    float a, b, c;

    cout << "Enter three floating point numbers:" << endl;
    cin >> a >> b >> c;

    cout.precision(5);
    cout << a << " " << b << " " << c << endl;

    cout << "Enter two more floating point numbers:" << endl;
    cin >> b >> a;

    cout.setf(ios::fixed);
    cout.precision(3);
    cout << a << " " << b << " " << c << endl;

    return 0;
}
