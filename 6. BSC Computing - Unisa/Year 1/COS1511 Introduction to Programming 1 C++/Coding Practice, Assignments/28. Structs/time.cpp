#include <iostream>
using namespace std;

struct Time
{
    int hours, minutes, seconds;
};


void changeTime (Time & timeP, int interval)
{
    int totalSecs, totalMins, totalHrs, remSecs, remMins, remHrs;

    totalSecs = timeP.seconds + interval;
    remSecs = totalSecs % 60;
    totalMins = timeP.minutes + totalSecs / 60;
    remMins = totalMins % 60;
    totalHrs = timeP.hours + totalMins / 60;
    remHrs = totalHrs % 24;

    timeP.hours = remHrs;
    timeP.minutes = remMins;
    timeP.seconds = remSecs;

}


int main()
{
    int interval;
    Time mytime;

    mytime.hours = 1;
    mytime.minutes = 30;
    mytime.seconds = 10;


    cout << "Please enter the number of seconds: ";
    cin >> interval;

    changeTime(mytime, interval);

    cout << "Hours: " << mytime.hours << endl;
    cout << "Minutes: " << mytime.minutes << endl;
    cout << "Seconds: " << mytime.seconds << endl;

    return 0;
}
