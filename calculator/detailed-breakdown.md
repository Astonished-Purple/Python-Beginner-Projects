# line by line breakdown of calculator.py

this breakdown will detail each of the 58 lines of code with the remaining 23 lines of comments and spacers being excluded from the breakdown.

---

line number:_______________ explanation________________________________
---
7: imports the python library 'math' to enable the use of the sqr.root function later in the script   

14: outputs the options to the user for calculations they can use along with a number to select it later   

21: creates the 'addition' function to be developed and called later in the program  
22: creates 'num1' variable as a string from user input entered (needs casting later to calculate with)  
23: creates the 'num2' variable as a string from user input entered (needs casting later to calculate with)  
24: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
25: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
26: completes the addition calculation and stores the answer as the variable 'answer'  
27: outputs the variable 'answer' made on the previous line  

31: creates the 'subtraction' function to be developed and called later in the program  
32: creates 'num1' variable as a string from user input entered (needs casting later to calculate with)  
33: creates the 'num2' variable as a string from user input entered (needs casting later to calculate with)  
34: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
35: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
36: completes the subtraction calculation and stores the answer as the variable 'answer'  
37: outputs the variable 'answer' made on the previous line  

39: creates the 'multiplication' function to be developed and called later in the program  
40: creates 'num1' variable as a string from user input entered (needs casting later to calculate with)  
41: creates the 'num2' variable as a string from user input entered (needs casting later to calculate with)  
42: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
43: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
44: completes the multiplication calculation and stores the answer as the variable 'answer'  
45: outputs the variable 'answer' made on the previous line  

47: creates the 'division' function to be developed and called later in the program  
48: creates 'num1' variable as a string from user input entered (needs casting later to calculate with)  
49: creates the 'num2' variable as a string from user input entered (needs casting later to calculate with)  
50: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
51: casts 'num1' to a float data type so that it can be used for calculations including decimals unlike integer data type  
52: completes the division calculation and stores the answer as the variable 'answer'  
53: outputs the variable 'answer' made on the previous line  

55: creates the 'square_root' function to be developed and called later in the program  
56: creates 'num1' variable as a string from user input entered (needs casting later to calculate with)  
57: casts 'num1' to a float data type so it can be used for calculations including decimals unlike the integer data type  
58: creates 'answer' variable and uses the math.sqrt function from 'math' library imported on line 7 to square root num1  

64: takes choice of calculations offered on line 14 of the program and stores it as a string in the 'choice' variable  
65: casts the 'choice' variable from a string to integer data type stored as the variable 'choice_int'  

67: opens the comparative statement and uses == to compare if 'choice_int' is equal to 1  
68: if the comparative statement is true the program will run the 'addition' function  

70: opens the comparative statement and uses == to compare if 'choice_int' is equal to 2  
71: if the comparative statement is true the program will run the 'subtraction' function  

73: opens the comparative statement and uses == to compare if 'choice_int' is equal to 3  
74: if the comparative statement is true the program will run the 'multiplication' function  

76: opens the comparative statement and uses == to compare if 'choice_int' is equal to 4  
77: if the comparative statement is true the program will run the 'division' function  

79: opens the comparative statement and uses == to compare if 'choice_int' is equal to 5  
80: if the comparative statement is true the program will run the 'square_root' function  
