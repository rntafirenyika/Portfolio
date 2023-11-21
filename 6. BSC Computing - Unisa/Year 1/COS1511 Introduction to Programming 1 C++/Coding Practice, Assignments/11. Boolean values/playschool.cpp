#include <iostream>
using namespace std;

int main()
{
    int childAge, income, parentAge;
    bool validChildAge, validIncome, validParentAge, validMaritalStatus;
    char maritalStatus;
    const int MAX_INCOME = 60000;
    const int MAX_PARENT_AGE = 30;

    cout << "Please enter child's age: ";
    cin >> childAge;
    cout << "Please enter parent's marital status, (M)arried or (S)ingle: ";
    cin >> maritalStatus;
    cout << "Please enter parent's annual income: ";
    cin >> income;
    cout << "Please enter parent's age: ";
    cin >> parentAge;

    validChildAge = childAge >= 3 && childAge <= 5;
    validMaritalStatus = maritalStatus == 'S' || maritalStatus == 's';
    validIncome = income < MAX_INCOME;
    validParentAge = parentAge < MAX_PARENT_AGE;

    cout << endl;
    if (validChildAge && validMaritalStatus && validIncome && validParentAge)
    {
        cout << "Acceptance criteria has been met." << endl;
    }
    else
    {
        cout << "Sorry, acceptance criteria has not been met." << endl;
    }

    return 0;
}
