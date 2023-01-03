"Developer: Hosna Hamdieh"
"Practicing condidtions using if, else if and else"

#include <iostream>
#include <stdlib.h> 
int main() {
 
  // Live long and prosper
srand (time(NULL));
 
int computer = rand() % 3 + 1;
int user = 0;
std::cout << "====================\n";
std::cout << "rock paper scissors!\n";
std::cout << "====================\n";
 
std::cout << "1) ✊\n";
std::cout << "2) ✋\n";
std::cout << "3) ✌️\n";
 
std::cout << "shoot! ";
std::cin>>user;
if (user == 1)
  std::cout << "you choose: ✊\n";
else if (user == 2)
  std::cout << "you choose: ✋\n";
else
  std::cout << "you choose: ✌️\n";
if (computer == 1)
    std::cout << "cpu choose: ✊\n";
  else if (computer == 2)
    std::cout << "cpu choose: ✋\n";
  else
    std::cout << "cpu choose: ✌️\n";

if (user==computer) {std::cout<<"No one wines\n";}
else if ((user==1 && computer==2)||(user==2 && computer==3)||(user==3 && computer==1)){std::cout<<"computer wines\n";}
else {std::cout<<"user wines\n";}}