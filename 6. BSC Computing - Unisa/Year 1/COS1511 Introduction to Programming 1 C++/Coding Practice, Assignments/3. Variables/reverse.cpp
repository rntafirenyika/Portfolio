//Prompts user for 3 numbers and displays them in reverse order.
#include <iostream>
using namespace std;

int main()
{
    int n1, n2, n3;
    cout << "Please enter 3 numbers: " << endl;
    cin >> n1 >> n2 >> n3;
    cout << "The numbers in reverse order are: " << n3 << " " << n2 << " " << n1 << endl;

    return 0;
}
