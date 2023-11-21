// Display a message as many times as requested by the user.
#include <string>
#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    int number, i = 0;
    string msg;

    // Prompt user for input
    cout << "Computer punishment\n";
    cout << "-------------------\n" << endl;
    cout << "Repetitions? ";
    cin >> number;
    cin.get();
    cout << "Message? ";
    getline(cin, msg, '\n');

    // print output
    cout << endl;
    while (i < number)
    {
        cout << msg << endl;
        i++;
    }

    return 0;
}
