//Test whether a number is prime
#include <iostream>
using namespace std;

int main( )
{
    int x, y;
    cout << "Enter a positive integer: ";
    cin >> y;
    x = 2;
    while (x != y)
    {
        //test if x is a factor of y
        if (y % x == 0)
        cout << y << " is not prime" << endl;
        break;
        x++;
    }
    if (x == y)
        cout << y << " is prime!" << endl;

    return 0;
}
