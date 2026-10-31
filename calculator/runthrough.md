# guide for running and experimenting with calculator.py

for the code in this repository it was all written in VSCodium so instructions will be best suited to that as an editor if you are an absolute beginner, although you can use any editor such as thonny 
which can be downloaded for Windows, Mac and Linux at **thonny.org**. Instructions for setting up VSCodium are included in the main repository landing page inside the README.md file

 <img width="972" height="724" alt="image" src="https://github.com/user-attachments/assets/c39b32c5-44df-4586-9376-1018c696ed02" />



---
once the editor is setup
---

once you have setup your chosen python editor you can download or copy/paste the 'calculator.py' file into the editor so you can run it and experiment with it. in your chosen editor there will be a run
button typically a green button but sometimes in editors like VSCodium it is just the word 'Run' at the top next to options like 'File' and 'Terminal'

---
running the script
---

once you have imported the code from the Github repository you can freely edit and run the code in your chosen editor. the first thing to do to make sure everything is working is just to run it in the
editor/IDE and test a few options which you can follow using the 'detailed-breakdown.md' file included in the calculator project folder. For simple testing of one of the functions i will detail the steps
below:

step 1: click 'Run'  
step 2: when prompted to enter the number for the calculation enter 1 for addition  
step 3: when prompted for the first number enter 10  
step 4: when prompted for the second number enter 5  
step 5: if the code runs correctly it will output '15.0' (the decimal is due to use of the float data type)

you should be able to follow the same or similar steps to run the other 4 functions available in the program.

---
adding to the code
---

for anyone who would like to adjust or add to the code this section is dedicated to a guided addition of a squaring function.

here are the steps to edit the code and create this function with screenshots to help:

first you should look to add the square function to the list of calculations outputted on line 14. You can do this as shown below in the screenshot by adding another \n to tell python to leave a blank
line before continuing to output the next part of the statement acting as a fast way to organise code as it runs and then adding '6 = square' to the print statement.

<img width="820" height="30" alt="image" src="https://github.com/user-attachments/assets/c6890e6b-f93b-4667-8351-adc71bf7538c" />

the next step is to create the function to square a number. this can be done as shown in the screenshot below. the highlighted section shows the added section of code.

<img width="614" height="677" alt="image" src="https://github.com/user-attachments/assets/910aebfb-c152-4df9-91dd-915bc740372d" />

now that the function has been added the final step to get it working and integrated with the rest of the script is to add the conditional if statement at the end of the code to allow the user to select 
option 6 and have it run the square function. this can be done as shown in the highlighted section of the screenshot below

<img width="573" height="409" alt="image" src="https://github.com/user-attachments/assets/79b12564-e2ec-4953-ad09-110d2b66b4fd" />

now the function should work by running the program and following these steps:  
step 1: when prompted for a number for the calculation enter 6 which correlates to the square function  
step 2: when prompted for the first number of the calculation enter 5 or a chosen number  
step 3: if the code is written correctly with no errors it will output 25.0 or your chosen number squared  

that's everything for this runthrough hopefully it was useful and feel free to save it for in future or anything like that


---

