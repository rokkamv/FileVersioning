#include <iostream>
#include <ctime>

using namespace std;

int main() {
    string fol;
    fol="first";
    time_t now;
    char dt[60];
    time(&now);
    tm *ptm=localtime(&now);
    strftime(dt,30,"%d/%m/%Y_%H:%M:%S",ptm);
    cout<<dt<<endl;
    return 0;
}
