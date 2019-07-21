#include<iostream>
#include<fstream>
#include<ctime>
#include<string>

using namespace std;

int main(int argc, char* argv[]){
  string fol=argv[1],text=argv[2],uname=argv[3];
  // if(argv[1]==NULL || argv[2]==NULL || argv[3]==NULL){
  //   cout<<"Error";
  // }
  cout<<fol<<endl<<text<<endl<<uname<<endl;
  time_t now;
  char dt[100];
  time(&now);
  tm *ptm=localtime(&now);
  strftime(dt,50,"%d-%m-%Y_%Hh%Mm%Ss",ptm);
  // fstream of(fname,ios::out);
  // of<<fname<<endl;
  string flname=fol+'_'+uname+'_'+dt;
  if(argc==5){
    system(("cd C:/Users/V/Desktop/ConMan/Repos/repo_"+fol+"/"+fol+" && echo "+text+" > "+flname+".txt").c_str());
    system(("cd C:/Users/V/Desktop/ConMan/Repos/repo_"+fol+"/"+uname+" && echo "+text+" > "+flname+".txt").c_str());
  }
  else
    system(("cd C:/Users/V/Desktop/ConMan/Repos/repo_"+fol+"/"+uname+" && echo "+text+" > "+flname+".txt").c_str());
  return 0;
}
