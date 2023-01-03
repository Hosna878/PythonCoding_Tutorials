"Developer: Hosna Hamdieh"
"Practicing condidtions using case"

#include <iostream>
int main() {
  double weight;
  std::cout<<"Enter your earth weight: ";
  std::cin>>weight;
  int planet;
  double RG;
  std::cout<<"Enter a number for the planet you want:\n1: Mercury, 2: Venus, 3: Mars, \n4: Jupiter, 6: Saturn 6: Uranus, 7: Neptune \nSelected planet: ";
  std::cin>>planet;
  switch (planet) {
    case 1: RG = 0.38;break;
    case 2: RG = 0.91;break;
    case 3: RG = 0.38;break;
    case 4: RG = 2.34;break;
    case 5: RG = 1.06;break;
    case 6: RG = 0.92;break;
    case 7: RG = 1.19;break;
    default: RG = 1;break;
  }
  double calculated_weight = weight * RG;
  std::cout<<"Your wieght in the chosen planet("<<planet<<") is "<<calculated_weight<<"\n";
 
}

