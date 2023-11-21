// Swaps the eatest element in an array with the first element of the array.
#include <iostream>
using namespace std;

int main()
{
    const int NUMS = 10;
    int numbers[NUMS];

    for (int i = 0; i < NUMS; i++)
    {
        cout << "Enter number: ";
        cin >> numbers[i];
    }

    for (int i = NUMS-1; i >= 0; i--)
    {
        cout << numbers[i] << " ";
    }
    cout << endl;

    return 0;
}
