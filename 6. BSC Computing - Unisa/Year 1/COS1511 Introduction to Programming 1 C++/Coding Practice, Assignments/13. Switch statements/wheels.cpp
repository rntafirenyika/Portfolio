#include <iostream>
using namespace std;

int main()
{
    int nrWheels; // number of wheels of a vehicle using the road
    int countTwo = 0, countFour = 0, countMore = 0; // the counters for the // number of vehicles with // two, four and more than // four wheels respectively

    while (true)
    {
        cout << "Vehicle countTwo(2), countTwo(4), countMore(6), Exit(0): ";
        cin >> nrWheels;

        if (nrWheels == 0)
            break;
        else if (nrWheels < 0 || nrWheels != 2 || nrWheels != 4 || nrWheels != 6)
        {
            cout << "Invalid input!" << endl;
            cout << endl;
            continue;
        }

        switch (nrWheels)
        {
            case 2:
                countTwo++;
                break;
            case 4:
                countFour++;
                break;
            default:
                countMore++;
        }

    }

    cout << endl;
    cout << "countTwo: " << countTwo << endl;
    cout << "countTwo: " << countFour << endl;
    cout << "countTwo: " << countMore << endl;

    return 0;
}
