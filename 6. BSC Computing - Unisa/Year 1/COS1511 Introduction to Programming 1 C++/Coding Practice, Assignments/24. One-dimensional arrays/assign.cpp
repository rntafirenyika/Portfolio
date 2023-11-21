// Assign numbers is array1 to array 2
#include <iostream>
using namespace std;

int main()
{
    const int NUMS = 10;
    float numbers[NUMS], numbers2[NUMS];

    for (int i = 0; i < NUMS; i++)
    {
        cout << "Enter number: ";
        cin >> numbers[i];
    }

    for (int i = 0; i < NUMS; i++)
    {
        numbers2[i] = numbers[i];
        cout << numbers2[i] << " ";
    }

    cout << endl;

    return 0;
}
