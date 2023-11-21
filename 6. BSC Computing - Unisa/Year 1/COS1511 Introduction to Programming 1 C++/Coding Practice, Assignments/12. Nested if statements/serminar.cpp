#include <iostream>
using namespace std;

int main()
{
	// Declaring variables
	int peopleCount;
	float amountDue;

	// Prompt user for number of people
	cout << "Enter the number of people registered: ";
	cin >> peopleCount;
	while (peopleCount < 1)
	{
		cout << "Invalid input! " << endl;
		cout << endl;
		cout << "Enter the number of people registered: ";
		cin >> peopleCount;

	}

	// Calculate and display amount due
	if (peopleCount >= 11)
		amountDue = 60 * peopleCount;
	else if (peopleCount >= 5)
		amountDue = 80 * peopleCount;
	else
		amountDue = 100 * peopleCount;

    // Format float output
    cout.setf(ios::fixed);
    cout.precision(2);

	cout << "The amount due is R" << amountDue << endl;

	return 0;
}
