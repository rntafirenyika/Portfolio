#include <iostream>
using namespace std;

int findValue(int numberP)
{
    int count = 0;
    int value = 20;
    while (count < numberP)
    {
        value += count;
        count ++;
    }
    return value;
}

int main ()
{
    cout << findValue(3);
    return 0;
}
