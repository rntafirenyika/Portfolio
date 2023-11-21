//Sorts an array of 15 random integers
#include <iostream>
#include <ctime>
using namespace std;

int main( )
{
    const int NUM_VALS = 15;
    int values[NUM_VALS];
    int nextVal, current;

    srand(time(0));

    for (int i = 0; i < NUM_VALS; i++)
    {
        nextVal = rand( ) % 1000;
        current = i - 1;

        while ((current >= 0) && (values[current] > nextVal))
        {
            values[current+1] = values[current];
            current--;
        }
        values[current + 1] = nextVal;

        cout << "After the " << i+1 << "th value has been generated, "
                << "the sorted array looks as follows:" << endl;
            for (int j = 0; j <= i; j++)
                cout << values[j] << ' ';
            cout << endl;
    }

    cout << endl << endl << "The final sorted array:" << endl;
    for (int i = 0; i < NUM_VALS; i++)
        cout << values[i] << " ";
    cout << endl << endl;

    return 0;
}

