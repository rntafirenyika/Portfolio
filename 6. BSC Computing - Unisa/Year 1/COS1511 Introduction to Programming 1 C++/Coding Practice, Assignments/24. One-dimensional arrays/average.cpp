#include <iostream>
using namespace std;

const int NUM_DAYS = 365; // number of days per year

int calcAverage (int cratesP[])
{
    int total, average;

    for (int i = 1; i <= NUM_DAYS; i++)
        total += cratesP[i];

    average = total / NUM_DAYS;

    return average;
}

int main()
{
    int crates[NUM_DAYS]; // array of days
    int average; // the average number of crates

    for (int i = 1; i <= NUM_DAYS; i++)
    {
        cout << "Day " << i << ": ";
        cin >> crates[i];
    }


    average = calcAverage(crates);
    cout << average << endl;

    return 0;
}
