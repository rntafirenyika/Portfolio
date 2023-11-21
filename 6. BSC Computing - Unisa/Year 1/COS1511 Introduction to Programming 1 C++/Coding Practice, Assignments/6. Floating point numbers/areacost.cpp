// Calculates the total price of a wall-to-wall carpet
#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    float area, length, width, price;
    const float PRICEPSM = 59.50;

    // Prompt user for the length and width
    cout << "Length: ";
    cin >> length;
    cout << "Width: ";
    cin >> width;

    // Calculate area
    area = length * width;
    price = area * PRICEPSM;

    // set output format
    cout.setf(ios::fixed);
    cout.precision(3);

    // print area and price
    cout << endl;
    cout << "The area is " << area << " square metres." << endl;

    cout.precision(2);
    cout << "The total cost of a wall-to-wall carpet is R" << price << endl;

    return 0;

}
