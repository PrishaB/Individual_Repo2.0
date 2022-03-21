## Create Task Work
<!-- {% include navigation.html %} -->
<table>
     <tr>
         <td><a href="index">Home</a></td>
         <td><a href="code">Replit Code</a></td>
         <td><a href="create_task">Create Task Work</a></td>
         <td><a href="notes">CB Notes</a></td>
         <td><a href="https://github.com/PrishaB/Individual_Repo2.0/projects/1#card-79113428">Review Ticket</a></td>
     </tr>
 </table>

Create Task One-Minute Video Link: https://drive.google.com/file/d/1MC9QIr6Zt-_QvZVwjWtfa4SvADldXGZz/view?usp=sharing

## 3A:
Purpose: Create a quiz for users to take that allows them to study for their computer science quiz

Functionality: Simple multiple choice quiz, the program keeps track of the right answers and the wrong answers.

Inputs/Outputs: Three questions and four possible answers for each. Users can click on the answers and see if they are correct or incorrect.

## 3B:
Two program code segments:

![3Bp1](https://github.com/arushi10/codefish/blob/database/static/assets/prisha_images/CreateTask1.JPG)
![3Bp2](https://github.com/arushi10/codefish/blob/database/static/assets/prisha_images/CreateTask2.JPG)

The myQuestions array is used to store the different questions and answers that are part of the quiz. The following function takes values from the subarray questions and matches them with values from the subarray answers and checks to see if the correct answer lines up with what the user selected. If it is correct, the program changes the text color to green and increases the score of correct answers but if it is wrong, it changes it to red and does nothing to the score.

If the array hadn’t been written, you would have to write out each question and answer several times as you write out radio buttons and check to make sure the user’s input is correct.

## 3C:
![3Cp1](https://github.com/arushi10/codefish/blob/database/static/assets/prisha_images/CreateTask3.JPG)
![3Cp2](https://github.com/arushi10/codefish/blob/database/static/assets/prisha_images/CreateTask4.JPG)

The procedure changes the score of the person taking the quiz. The original score is set at zero and when the correct answer is selected, the score increases by one.


## 3D:

![3Dp1](https://github.com/arushi10/codefish/blob/database/static/assets/prisha_images/CreateTask5.JPG)

User’s answer must be inputted. If the user's answer matches the correct answer, the score increases by one.

![3Dp2](https://github.com/arushi10/codefish/blob/database/static/assets/prisha_images/CreateTask6.JPG)

The score must be a value from 0 to the length of the subarray questions. It shows the numbers correct that the user got.
