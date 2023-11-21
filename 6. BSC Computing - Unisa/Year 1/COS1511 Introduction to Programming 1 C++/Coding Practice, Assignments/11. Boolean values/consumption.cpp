// Calculate Water Consumption bill due
#include <iostream>
using namespace std;

int main ()
{
    const float FIXED_RATE = 10;
    const float FREE_UNITS = 20;
    float unitsUsed, cost;
    bool baseUnits, tier1, tier2;

    cout << "Enter water units used: ";
    cin >> unitsUsed;

    baseUnits = unitsUsed <= FREE_UNITS;
    tier1 = unitsUsed > FREE_UNITS && unitsUsed <= 40;
    tier2 = unitsUsed > 40 && unitsUsed <= 100;

    if (baseUnits)
    {
        cost = 0.00;
    }
    else if (tier1)
    {
        cost = (unitsUsed - FREE_UNITS) * FIXED_RATE;
    }
    else if (tier2)
    {
        cost = (20 * FIXED_RATE) + (unitsUsed - 40) * FIXED_RATE * 1.5;
    }
    else
    {
        cost = (20 * FIXED_RATE) + (60 * FIXED_RATE * 1.5) + (unitsUsed - 100) * FIXED_RATE * 2;
    }

    cout.setf(ios::fixed);
    cout.precision(2);

    cout << "The cost of " << unitsUsed << " units is R" << cost << endl;

    return 0;
}
