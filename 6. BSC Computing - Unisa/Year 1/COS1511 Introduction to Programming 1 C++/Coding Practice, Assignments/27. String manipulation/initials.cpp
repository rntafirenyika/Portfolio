#include <iostream>
#include <string>

using namespace std;

string getInitials(string name)
{
    string initials;
    int position;

    initials = name[0];
    position = name.find(" ");
    while (position != -1)
    {
        initials += name[position+1];
        position = name.find(" ", position+1);
    }

    return initials;
}

int main()
{
    string name, initials;

    cout << "Enter name: ";
    getline(cin, name, '\n');

    initials = getInitials(name);

    cout << initials << endl;

    return 0;
}
