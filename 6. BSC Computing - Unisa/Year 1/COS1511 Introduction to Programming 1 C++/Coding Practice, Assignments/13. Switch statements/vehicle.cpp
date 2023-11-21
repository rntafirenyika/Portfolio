#include <iostream>
using namespace std;

int main()
{
    int age;

    cout << "Enter age: ";
    cin >> age;

    switch (age)
    {
        case 1:
        case 2:
        case 3:
        case 4:
            cout << "You can ride a tricycle" << endl;
            break;
        case 5:
        case 15:
            cout << "You can ride a bike" << endl;
            break;
        case 16:
        case 17:
            cout << "You can ride a motorcycle" << endl;
            break;
        default:
            cout << "You can drive a car" << endl;
    }

    return 0;
}
