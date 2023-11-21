// Check if total mass exceeds maximum load on a plane.
#include <iostream>
using namespace std;

int main()
{
    //Declare variables and constants
    const float MAXIMUM_LOAD = 10000;
    float totalMass, luggageMass;

    totalMass = 0;
    while (totalMass < MAXIMUM_LOAD)
    {
        cout << "Enter luggage mass: ";
        cin >> luggageMass;

        if (luggageMass == 0)
        {
            cout << "Exiting...";
            break;
        }
        else if (totalMass + luggageMass > MAXIMUM_LOAD)
        {
            cout << "Maximum load will be exceeded!";
            break;
        }
        totalMass += luggageMass;
        cout << "The total mass is now " << totalMass << "kgs" << endl;
        cout << endl;
    }

    return 0;
}
