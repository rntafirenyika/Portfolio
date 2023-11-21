// Checks if 100m2 of carpet can cover the user's room size
#include <iostream>
using namespace std;

int main()
{
    float length, width, area, notCovered;
    const int CARPET_AVAILABLE = 100;

    // Prompt user for room dimensions
    cout << "Length: ";
    cin >> length;
    cout << "Width: ";
    cin >> width;

    area = length * width;

    if (area <= CARPET_AVAILABLE)
    {
        cout << "Available carpet is enough to cover the room." << endl;
    }
    else
    {
        notCovered = area - CARPET_AVAILABLE;
        cout << "Available carpet is not enough to cover the room." << endl;
        cout << notCovered << "m2 will not be covered." << endl;
    }

    return 0;
}
