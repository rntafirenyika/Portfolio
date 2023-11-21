// Swaps the eatest element in an array with the first element of the array.
#include <iostream>
using namespace std;

void swap(int arrayP[])
{
    int highest = 0;
    int temp = 0;
    int index = 0;
    for (int i = 0; i < 10; i++)
    {
        if (arrayP[i] > highest)
        {
            highest = arrayP[i];
            index = i;
        }
    }

    temp = highest;
    arrayP[index]= arrayP[0];
    arrayP[0] = temp;

}


int main()
{
    int numbers[] = {10, 3, 56, 7, 0, 5, 44, 99, 76, 1};

    swap(numbers);

    for (int i = 0; i < 10; i++)
    {
        cout << numbers[i] << " ";
    }
    cout << endl;

    return 0;
}
