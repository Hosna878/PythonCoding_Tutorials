"Developer: Hosna Hamdieh"
"Practicing condidtions using if, else if and else"

#include <iostream>
 
int main() {
 
  // The magic starts here
 int gryffindor,hufflepuff,ravenclaw,slytherin=0;
 int answer1,answer2,answer3,answer4;
 std::cout<<"The Sorting Hat Quiz!\n";
 std::cout<<"Q1) When I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nanswer1: ";
 std::cin>>answer1;
 if (answer1 == 1) {hufflepuff+=1;}
 else if (answer1 == 2) {slytherin+=1;}
 else if (answer1 == 3) {ravenclaw+=1;}
 else if (answer1 == 4) {gryffindor+=1;}
 else {std::cout<<"Invalid input\n";}
 std::cout<<"Q2) Dawn or Dusk?\n1) Dawn\n2) Dusk\nanswer2: ";
 std::cin>>answer2;
 if (answer2 == 1) {gryffindor+=1;ravenclaw+=1;}
 else if (answer2 == 2) {hufflepuff+=1;slytherin+=1;}
 else {std::cout<<"Invalid input\n";}
 std::cout<<"Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\nanswer3: ";
 std::cin>>answer3;
 if (answer3 == 1) {slytherin+=1;}
 else if (answer3 == 2) {hufflepuff+=1;}
 else if (answer3 == 3) {ravenclaw+=1;}
 else if (answer3 == 4) {gryffindor+=1;}
 else {std::cout<<"Invalid input\n";}
 std::cout<<"Q4) Which road tempts you most?\n1) The wide, sunny grassy lane\n2) The narrow, dark, lantern-lit alley\n3) The twisting, leaf-strewn path through woods\n4) The cobbled street lined (ancient buildings)\nanswer4: ";
 std::cin>>answer4;
 if (answer4 == 1) {hufflepuff+=1;}
 else if (answer4 == 2) {slytherin+=1;}
 else if (answer4 == 3) {gryffindor+=1;}
 else if (answer4 == 4) {ravenclaw+=1;}
 else {std::cout<<"Invalid input\n";}
 int max=0;
 std::string house;
 if (gryffindor > max) {
 
  max = gryffindor;
  house = "Gryffindor";
 
}
 
if (hufflepuff > max) {
 
  max = hufflepuff;
  house = "Hufflepuff";
 
}
 
if (ravenclaw > max) {
 
  max = ravenclaw;
  house = "Ravenclaw";
 
}
 
if (slytherin > max) {
 
  max = slytherin;
  house = "Slytherin";
 
}
 
std::cout << house << "!\n";
}

