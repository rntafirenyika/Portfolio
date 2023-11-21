// Create a fictious dialogue
#include <string>
#include <iostream>
using namespace std;

int main()
{
    // Declare variables
    string name1, name2, colour, noun, adjective;
    int number;

    // Promp user for input
    cout << "Enter a person's name: ";
    cin >> name1;
    cout << "Enter another person's name: ";
    cin >> name2;
    cout << "Enter a colour: ";
    cin >> colour;
    cout << "Enter a number: ";
    cin >> number;
    cout << "Enter a noun: ";
    cin >> noun;
    cout << "Enter an adjective: ";
    cin >> adjective;

    // Print dialogue
    cout << endl;
    cout << "Dialogue" << endl;
    cout << "========" << endl;
    cout << name1 << ": \"Couldn't you see that the traffic light was " << colour << "?\"" << endl;
    cout << name2 << ": \"But I had " << number << " people and a " << noun << " in the car with me.\"" << endl;
    cout << name1 << ": \"That is so " << adjective << "! You could have had them all killed.\"" << endl;
}
