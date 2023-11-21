#include <iostream>
using namespace std;

int main()
{
    string name;
    int age, marks;
    bool validAge, validMarks;

    while (true)
    {
        validAge = false;
        validMarks = false;

        cout << "Enter Student name: ";
        cin >> name;
        cout << "Enter Student age: ";
        cin >> age;
        cout << "Enter Student marks: ";
        cin >> marks;

        if (age < 30)
        {
            validAge = true;
        }
        if (marks > 65)
        {
            validMarks = true;
        }
        if (validAge && validMarks)
        {
            cout << "Student " << name << " was successful." << endl;
            break;
        }
        cout << "Student " << name << " was not successful." << endl;
        cout << endl;

    }



    return 0;

}
