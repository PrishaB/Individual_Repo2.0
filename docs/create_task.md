## Create Task Work

{% include navigation.html %}

Create Task One-Minute Video Link: https://drive.google.com/file/d/1Jdd3l3uBkOyCpBLy6Sq-IKOuFc-7U9Kr/view?usp=sharing

## 3A:
Purpose: Create a quiz for users to take that allows them to study for their computer science and/or math quiz. More questions can be added to the quiz by the user so they can study more things.

Functionality: Simple free response quiz, the program keeps track of the user's score and presents it at the end. There is also a program that allows users to add more questions to their current study time. 

Inputs/Outputs: Originally three questions with three responses. The program will reveal a question and accept the user's input, check it with the right answer, and let the user know whether they are right or wrong. The program also takes in the user's custom questions and temporarily adds it to the list of questions to help the students further review their concepts.

## 3B:
Two program code segments:

![3Bp1](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/CStest.JPG)
![3Bp2](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/add_to_CStest.JPG)

The CStest list stores all the questions and answers that are in the CStest by default. The answers are appended to the questions, making it easier to correct the user's responses when the function randomly generates questions to ask the user since the answer is attached to the question. The next image shows the function add_to_CStest which allows the student to add more questions to the CStest list so that they can further quiz themselves on the topics. This allows the student to use the quiz more beneficially since they can add more questions to the quiz which allows them to study more topics.

Without the list, the function wouldn't be able to shuffle the questions and the code would be hardcoded to display the questions in a static manner. The questions and their answers would always be in the same order which would make it hard for the student to properly study for their exam(s). Adding on, without a list, it would be difficult to add more questions to the quiz and the main way to change the questions would be to hardcode new questions and answers.

## 3C:
![3Cp1](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/run_CStest.JPG)
![3Cp2](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/CS_test.JPG)

Here we have an image of the function run_CStest. This function shuffles the questions and sets the score to zero before randomly generating the questions and showing the users how they did by giving them feedback and showing them their final score. This code implements sequencing by running through the list and shuffling it in a randomized order for the user's benefit. It also implents selection in the if then statements that determine whether or not the user's input is equal to the right answer. The function also implements iteration through its for loop which runs through the freshly randomized list and displays the key values from the list and then checks the user's inputs to the values in the list. We also have an image of the function being called and here, it's part of the list of a submenu so that the users can run it from the menu options.


## 3D:
### First instance:
![3Dp1](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/CS_test.JPG)

Here is the first instance where run_CStest is being called. It is being called here so that the user can run the code and take the test. If the person selects the value '1' from the submenu, they run the test program.

Results:
![results](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/runtimeforCStest.JPG)

### Second instance:
![3Dp2](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/add_to_CStest.JPG)

This is the second instance where run_CStest is being called. Once the user runs add_to_CStest and contributes a question and response to the list, run_CStest is run and the test is started once more to prove that the new question and answer has been added to the list.

Results:
![results2](https://github.com/PrishaB/Individual_Repo2.0/blob/main/images/runtimeforaddtoCStest.JPG)
