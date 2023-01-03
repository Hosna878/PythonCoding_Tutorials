"Developer: Hosna Hamdieh"
"Practicing condidtions, and for loaps"

#include <iostream>
int main(){
  std::string story;
  std::string next;
  std::string answer;
  // int chance=0;
  std::string beginning="Once upon a time lived a curious girl, wanting to learn more about the world and see other places.\nShe lived in a small vilage near a river and looked at the boats living the vilage every day, wanting to go on an adventure.\nOne day her father gave her money to go and buy a particular tool from the shop when \n";
  story += beginning;
  std::cout<<story;
  std::cout<<"A. She saw a stranger looking very interesting living the shop.\nB. She got hungrry and changed her path to grab somthing to eat.\nC. Someone called her name from far\nSelected?(A, B or C)";
  // std::cin>>answer;
  for (int chance=1;chance<3;chance++){std::cin>>answer;if(answer=="A" || answer=="a" || answer=="B" || answer=="b" ||answer=="C" || answer=="c"){break;}}
  if (answer=="A" || answer=="a") 
  {
    next="She fallowed him for a bit ending up \n";
    story+=next;
    std::cout<<next;
    std::cout<<"A. Near the river\nB. In an old pub\nC. Out of the town\nSelected?(A, B or C)";
    std::cin>>answer;
    for (int chance=1;chance<3;chance++){std::cin>>answer;if(answer=="A" || answer=="a" || answer=="B" || answer=="b" ||answer=="C" || answer=="c"){break;}}
    if (answer=="A" || answer=="a") 
    {
    next="She saw him boarding a boat and then she fallowed him and was never seen again.\n";
    story+=next;
    std::cout<<next; 
  }
   else if (answer=="B" || answer=="b") 
   {
    next="He ordered a bear and went to sit in the corner and looked at her in a strange way so she left and went to the tool store scared and confused.\n";
    story+=next;
    std::cout<<next;} 
  else if (answer=="C" || answer=="c") {
    next="She could not believe how long it has passed and now it was nearly dark so went back home thinking why she followed him in the first place.\n";
    story+=next;
    std::cout<<next;
  }
  }
  if (answer=="B" || answer=="b") 
  {
    next="She went to the nearest shop to buy bread and jam but when she got there the store was empty and the door was half open \n";
    story+=next;
    std::cout<<next;
    std::cout<<"A. She looked around and could not find any one\nB. She was scared and called out for help\nC. It was clear that she needed to inform someone\nSelected?(A, B or C)";
    std::cin>>answer;
    for (int chance=1;chance<3;chance++){std::cin>>answer;if(answer=="A" || answer=="a" || answer=="B" || answer=="b" ||answer=="C" || answer=="c"){break;}}
    if (answer=="A" || answer=="a") {
    next="So she left for home.\n";
    story+=next;
    std::cout<<next;} 
  
   else if (answer=="B" || answer=="b") {
    next="There was blood everywhere and in a matter of seceonds she was running out of fear.\n";
    story+=next;
    std::cout<<next;}
   else if (answer=="C" || answer=="c"){
    next="She went to the owner's house that was near it was a silly mistake she forgot to lock up as she was in a hurry\n";
    story+=next;
    std::cout<<next;
  }}
  else if (answer=="C" || answer=="c") 
  {
    next="It was someone she did not know so\n";
    story+=next;
    std::cout<<next;
    std::cout<<"A. It took her a bit to answer it turned out she has droped her bag by accident.\nB. She did not respond at first but then she asked 'do I know you?'\nC. She looked harder and it was indeed someone familiar yet strange\nSelected?(A, B or C)";
    std::cin>>answer;
    for (int chance=1;chance<3;chance++){std::cin>>answer;if(answer=="A" || answer=="a" || answer=="B" || answer=="b" ||answer=="C" || answer=="c"){break;}}
    if (answer=="C" || answer=="c") {
    next="It turned out it was her friends dad and he was looking for her.\n";
    story+=next;
    std::cout<<next;} 
  
   else if (answer=="A" || answer=="a") {
    next="He gave her bag back and it was close as she nearly lost the money she needed for the tools.\n";
    story+=next;
    std::cout<<next;}
   else if (answer=="B" || answer=="b") {
    next="The stranger said 'no but I like to get to know you better'\n";
    story+=next;
    std::cout<<next;
  }}
  std::cout<<"The complete story:\n"<<story;
}