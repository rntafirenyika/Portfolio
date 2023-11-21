#include <iostream>
using namespace std;

const int NUM_WEEKS = 4;
const int NAME = 3;

int main ()
{
    int sales[NUM_WEEKS][NAME] = {{100, 120, 103}, {96, 122, 111}, {110, 101, 119}, {106, 99, 102}};

    for (int i = 0; i < NUM_WEEKS; i++)
    {
        int highest;
        highest = 0;
        for (int j = 0; j < NAME; j++)
        {
            if (sales[i][j] > highest)
                highest = sales[i][j];
        }

        for (int j = 0; j < NAME; j++)
        {
            if (sales[i][j] == highest)
                cout << "The highest sales in week " << i+1 << " were " << highest << " books." << endl;
        }
    }
}
