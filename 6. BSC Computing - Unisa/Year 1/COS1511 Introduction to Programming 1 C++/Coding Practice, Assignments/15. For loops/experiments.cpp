#include <iostream>
using namespace std;

int main()
{
    float result, average;

    for (int exp = 0; exp < 4; exp++)
    {
        int total = 0;
        cout << "Please enter results for experiment no " << exp + 1 << ": " << endl;

        for (int i = 0; i < 5; i++)
        {
            cout << "Result no " << i + 1 << ": ";
            cin >> result;
            total += result;//calculate total
        }
        average = total / 5; //calculate average
        //Settings to Display the average with a precision of two digits after the decimal point
        cout.setf(ios::fixed);
        cout.precision(2);
        cout << "Average for experiment no " << exp + 1 << ": " << average << endl << endl; //display average
    }
    return 0;
}
