# Program Name: Lab1.py (use the name the program is saved as)
# Course: IT1114/Section XXX
# Student Name: John Doe
# Assignment Number: Lab#
# Due Date: xx/xx/ 20XX
# Purpose: What does the program do (in a few sentences)?
# List specific resources used to complete the assignment.

# Input : All of these contains input and formulas for each variable
RoomLength = str(input("the length of the room :"));
RoomWidth = str(input("the width of the room :"));
CostPerSqFt = int(input("the cost of the flooring per square foot :"));\
TotalSqFt = roomLength * RoomWidth;
TotalFlooringCost = TotalSqFt * CostPerSqFt;
Tax = TotalFlooringCost * 7/100;
TotalDue = TotalFlooringCost + Tax;

# Output : Prints all answers
print("Square feet: " + TotalSqFt);
print("Flooring: " + TotalFlooringCost);
print("Tax: " + Tax);
print("Total due: " + TotalDue);

