// Calculates how many boxes will be needed for packing, and how many items will be left over.
#include <iostream>
using namespace std;

int main()
{
    int total, per_box, num_boxes, remainder;
    cout << "Total number of items to be packed: " << endl;
    cin >> total;
    cout << "Number of items fitting in a box: " << endl;
    cin >> per_box;

    num_boxes = total / per_box;
    remainder = total % per_box;

    cout << "Total boxes required: " << num_boxes << endl;
    cout << "Number of items remaining: " << remainder << endl;

    return 0;

}
