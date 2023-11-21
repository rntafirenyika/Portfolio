// Calculate average height for a group of individuals
#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    int people, count;
    float total, height, average;

    // Prompt user for number of people who participated in the survey
    cout << "How many people participated in the survey: ";
    cin >> people;
    cout << endl;

    count = 1;
    total = 0.0;
    while (count <= people)
    {
        cout << "Enter height for person " << count << ": ";
        cin >> height;
        total += height;
        count++;
    }

    // Calculate the average
    average = total / people;

    // Format output
    cout.setf(ios::fixed);
    cout.precision(2);

    cout << endl;
    cout << "The average height is " << average << endl;

    return 0;

}
