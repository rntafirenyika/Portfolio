#include <iostream>
using namespace std;

int main()
{
    const int baseCost = 900;
    int roomCost, tax, discount, totalExc, totalInc, numRooms, days;

    cout << "Please enter the following:" << endl;
    cout << "cost per room: ";
    cin >> roomCost;
    cout << "sales tax per room: ";
    cin >> tax;
    cout << "the number of rooms: ";
    cin >> numRooms;
    cout << "number of days: ";
    cin >> days;
    cout << endl;

    totalExc = roomCost * numRooms * days;
    totalInc = totalExc + (totalExc * tax / 100);

    if (numRooms >= 30)
    {
        discount = 30;
    }
    else if (numRooms >= 20)
    {
        discount = 20;
    }
    else if (numRooms >= 10)
    {
        discount = 10;
    }
    else
    {
        discount = 0;
    }

    if (discount > 0 && days >= 3)
    {
        discount += 5;
    }

    // Display the output
    cout << "The total cost for one room is R" << roomCost << endl;
    cout << "The discount per room is " << discount << "%" <<endl;
    cout << "The number of rooms booked: " << numRooms << endl;
    cout << "The total cost of the rooms are R: " << totalExc << endl;
    cout << "The sales tax paid is : " << tax << "%" <<endl;
    cout << "The total cost per booking is R" << totalInc << endl;

    return 0;

}
