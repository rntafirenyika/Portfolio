#include <iostream>
using namespace std;

int main()
{
    float marks, earnings;
    char grade;

    cout << "University marks: ";
    cin >> marks;
    cout << "Earnings: ";
    cin >> earnings;

    if (marks >= 90)
        grade = 'A';
    else if (marks >= 75)
        grade = 'B';
    else if (marks >= 60)
        grade = 'C';
    else
        grade = 'F';

    switch (grade)
    {
    case 'A':
        cout << "She can go to any university of her choice and she will get a car." << endl;
        break;
    case 'B':
        if (earnings > 5000)
            cout << "She can go to any university of her choice and she will get a car." << endl;
        else
            cout << "She can study at the university of her choice, but she will not get a car." << endl;
        break;
    case 'C':
        cout << "She must study at the nearest university." << endl;
        break;
    case 'F':
        cout << "She cannot go to university" << endl;
    }
}
