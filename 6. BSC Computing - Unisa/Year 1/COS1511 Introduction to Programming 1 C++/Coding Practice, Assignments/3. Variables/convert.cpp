//Fahrenheit to Celsius conversion
#include <iostream>
using namespace std;

int main()
{
    int F, C;
    cout << "Fahrenheit: ";
    cin >> F;
    C = 5 * (F - 32) / 9;
    cout << C << " degrees Celsius" << endl;

    return 0;
}
