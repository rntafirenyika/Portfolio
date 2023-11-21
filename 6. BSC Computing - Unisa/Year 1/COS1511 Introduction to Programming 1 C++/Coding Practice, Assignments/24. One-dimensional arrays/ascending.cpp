// Determines whether the values in an array are stored in ascending order
#include <iostream>
using namespace std;

int main()
{
    const int NUMS = 20;
    int numbers[NUMS] = {12, 15, 17, 23, 37, 40, 55, 54, 70, 77, 79, 80, 84, 86, 89, 91, 92, 100, 123, 126};
    int current;
    bool inOrder = true;

    for (int i = 0; i < NUMS-1; i++)
    {
        if (numbers[i] > numbers[i+1])
        {
            inOrder = false;
        }
    }

    if (inOrder)
        cout << "All the numbers are in ascending order." << endl;
    else
        cout << "The numbers are NOT in ascending order." << endl;

    cout << endl;

    return 0;
}
