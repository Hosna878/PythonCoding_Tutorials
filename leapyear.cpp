"Developer: Hosna Hamdieh"
"Practicing condidtions using if, else if and else"

#include <iostream>

int main() {
  int year;
  std::cout<<"Enter a year: ";
  std::cin>>year;
  if (year % 4 == 0 || year %400 ==0){std::cout<<"It is a leap year\n";}
  else if (year % 100 == 0 and year % 400 != 0) {std::cout<<"It is NOT a leap year\n";}
  else {std::cout<<"It is NOT a leap year\n";} 
}