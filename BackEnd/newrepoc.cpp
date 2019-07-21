#include <iostream>
#include <ctime>

using namespace std;

int main(int argc,char* argv[]) {
    string fol=argv[1],uname=argv[2];
    time_t now;
    char dt[100];
    time(&now);
    tm *ptm=localtime(&now);
    strftime(dt,50,"%d-%m-%Y_%Hh%Mm%Ss",ptm);
    string flname=fol+'_'+uname+'_'+dt;
    system(("cd .. && cd Repos && mkdir repo_"+fol+" && cd repo_"+fol+" && mkdir "+fol+" && cd "+fol+" && echo "+flname+" > "+flname+".txt").c_str());
    system(("cd .. && cd Repos && cd repo_"+fol+" && mkdir "+uname+" && cd "+uname+" && echo "+flname+" > "+flname+".txt").c_str());
    return 0;
}
