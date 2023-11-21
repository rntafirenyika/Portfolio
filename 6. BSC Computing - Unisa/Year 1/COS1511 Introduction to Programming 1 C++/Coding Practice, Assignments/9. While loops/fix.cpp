#include <iostream>
using namespace std;

int main()
{
    float total = 0.0;
    float value, last = 0;
    int num, count;
    cout << "Enter number of values: ";
    cin >> num;
    count = 0;
    while (count < num)
    {
        cout << "Enter a value : ";
        cin >> value;
        last = value;
        count++;
        total += value;
    }
    cout << "The last value entered was " << last << endl;
}
