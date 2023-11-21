#include <iostream>
using namespace std;

int main()
{
    int wattage, lifeE;
    lifeE = 0;

    cout << "Enter bulb's wattage: ";
    cin >> wattage;

    switch(wattage)
    {
        case 25:
            lifeE = 25000;
            break;
        case 40:
        case 60:
            lifeE = 1000;
            break;
        case 75:
        case 100:
            lifeE = 750;
            break;
        default:
            cout << "Invalid wattage!";
    }

    if (lifeE != 0)
    {
        cout << "The life expectancy of a bulb with " << wattage << " watts is " << lifeE << " hours." << endl;
    }

    return 0;

}
