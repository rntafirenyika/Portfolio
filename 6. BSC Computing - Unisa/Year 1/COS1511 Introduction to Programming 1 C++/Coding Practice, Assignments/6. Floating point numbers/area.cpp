#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    float area, length, width;

    // Prompt user for the length and width
    cout << "Length: ";
    cin >> length;
    cout << "Width: ";
    cin >> width;

    // Calculate area
    area = length * width;

    // set output format
    cout.setf(ios::fixed);
    cout.precision(3);

    // print area
    cout << endl;
    cout << "The area is " << area << " square metres." << endl;

    return 0;

}
