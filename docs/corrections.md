{% include navigation.html %}

# Test Corrections

## Final Test 5
### Score: 37/50
#### Question 1: A company that develops mobile applications wants to involve users in the software development process. Which of the following best explains the benefit in having users participate?
#### Right Answer: Users can provide feedback that can be used to incorporate a variety of perspectives into the software.
#### Corrections: Correct. Users can provide feedback that can help inform program design and development. Information gathered from potential users can be used to understand the purpose of a program from diverse perspectives and to develop a program that fully incorporates these perspectives.

#### Question 5: A computer program uses 3 bits to represent integers. When the program adds the decimal (base 10) numbers 5 and 3, the result is 0. Which of the following is the best explanation for the result?
#### Right Answer: An overflow error occurred.
#### Corrections: The binary representations (in 3 bits) of 5 and 3 are 101 and 011, respectively. If these numbers are added, the result would be 1000. Since only 3 bits are used to represent integers in this example, the result would be stored as 000. This is an example of overflow error.

#### Question 6: A wildlife preserve is developing an interactive exhibit for its guests. The exhibit is intended to allow guests to select the name of an animal on a touch screen and display various facts about the selected animal. For example, if a guest selects the animal name “wolf,” the exhibit is intended to display the following information.
``Classification: mammal
Skin type: fur
Thermoregulation: warm-blooded
Lifestyle: pack
Average life span: 10–12 years
Top speed: 75 kilometers/hour
The preserve has two databases of information available to use for the exhibit. The first database contains information for each animal’s name, classification, skin type, and thermoregulation. The second database contains information for each animal’s name, lifestyle, average life span, and top speed.``
##### Which of the following explains how the two databases can be used to develop the interactive exhibit?
#### Right Answer: Both databases are needed. Each database can be searched by animal name to find all information to be displayed.
#### Corrections: The information to be displayed comes from both databases. The animal name can be used search the first database to find the classification, skin type, and thermoregulation information. The animal name can be used search the second database to find the lifestyle, average life span, and top speed information.

#### Question 9: The table below shows the time a computer system takes to complete a specified task on the customer data of different-sized companies. Based on the information in the table, which of the following tasks is likely to take the longest amount of time when scaled up for a very large company of approximately 100,000 customers?
#### Right Answer: Sorting data
#### Corrections: Sorting data increases at a greater rate than searching through data as the number of customers increase. That is why sorting data takes more time.

#### Question 10: The code segment below is intended to display all multiples of 5 between the values start and end, inclusive. For example, if start has the value 3 5 and end has the value 5 0, the code segment should display the values 3 5, 4 0, 4 5, and 5 0. Assume that start and end are multiples of 5 and that start is less than end. Which of the following could replace MISSING EXPRESSION  in line 2 so that the code segment works as intended?
#### Right Answer: ((end - start)/5)+1
#### Corrections: The loop should iterate once for each multiple of 5 from start to end. The number of multiples of 5 from start to end is given by ((end - start)/5)+1. For the example given, ((end - start)/5)+1 evaluates to 4.

#### Question 16: Consider the two programs below. Which of the following best compares the values displayed by programs A and B?
#### Right Answer: Program A initializes i to 1. Inside the loop, it prints i and then increments i. 
#### The loop terminates when i is greater than 10, which occurs after 10 is printed. Program A prints 1 2 3 4 5 6 7 8 9 10. Program B initializes i to 0. Inside the loop, it increments i and then prints i. The loop terminates when i equals 10, which occurs after 10 is printed. Program B prints 1 2 3 4 5 6 7 8 9 10.

#### Question 17: An online game collects data about each player’s performance in the game. A program is used to analyze the data to make predictions about how players will perform in a new version of the game. The procedure GetPrediction (idNum) returns a predicted score for the player with ID number idNum. Assume that all predicted scores are positive. The GetPrediction procedure takes approximately 1 minute to return a result. All other operations happen nearly instantaneously. Two versions of the program are shown below.
#### Right Answer: Version II requires approximately 5 more minutes to execute than version I.
#### Corrections: Version I calls the GetPrediction procedure once for each element of idList, or four times total. Since each call requires 1 minute of execution time, version I requires approximately 4 minutes to execute. Version II calls the GetPrediction procedure twice for each element of idList, and then again in the final display statement. This results in the procedure being called nine times, requiring approximately 9 minutes of execution time.

#### Question 22: A certain computer game is played between a human player and a computer-controlled player. Every time the computer-controlled player has a turn, the game runs slowly because the computer evaluates all potential moves and selects the best one. Which of the following best describes the possibility of improving the running speed of the game?
#### Right Answer: The game’s running speed might be improved by using a process that finds approximate solutions every time the computer-controlled player has a turn.
#### Corrections: Selecting the best move is an optimization problem that cannot be solved in a reasonable time based on the information that the game runs slowly. If the algorithm for selecting the best move is running too slowly, the game may run more quickly if a heuristic is used to find approximate solutions.

#### Question 30: A student wrote the following program to remove all occurrences of the strings "the" and "a" from the list wordList. While debugging the program, the student realizes that the loop never terminates. Which of the following changes can be made so that the program works as intended?
#### Right Answer: Inserting index  ←  index - 1 between lines 7 and 8
#### Corrections: The program traverses wordList starting at the end of the list and moving to the start of the list, removing any elements that are equal to "the" or "a" along the way. Inserting this statement between lines 7 and 8 decrements index after checking each list element, ensuring that all elements are checked.

#### Question 40: Some programming languages use constants, which are variables that are initialized at the beginning of a program and never changed. Which of the following are good uses for a constant?
``I. To represent the mathematical value π (pi) as 3.14
II. To represent the current score in a game
III. To represent a known value such as the number of days in a week``
#### Right Answer: I and III only
#### Corrections: A constant is a good choice for statement I and statement III because the value of pi and the number of days in a standard calendar week never change.

#### Question 43: Which of the following statements about the Internet is true?
#### Right Answer: The Internet is designed to scale to support an increasing number of users.
#### Corrections: The Internet was designed to be scalable, using open protocols to easily connect additional computing devices to the network.

#### Question 45: The two code segments below are each intended to display the average of the numbers in the list One word, num List. Assume that One word, num List contains more than one value. Which of the following best describes the two code segments?
#### Right Answer: Both code segments display the correct average, but code segment I requires more arithmetic operations than code segment II.
#### Corrections: Both code segments display the correct average. Code segment I requires more arithmetic operations because it performs the operation sum divided by LENGTH, open parenthesis, num List, close parenthesis within the loop, while code segment II performs the same operation only once.

#### Question 48: Which of the following best explains how a certificate authority is used in protecting data?
#### Right Answer: A certificate authority verifies the authenticity of encryption keys used in secured communications.
#### Corrections: Certificate authorities are entities that issue digital certificates, which are used to certify the ownership of public keys.

## Final Test 3
### Score: 41/50
#### Question 2: Which of the following best explains the ability to solve problems algorithmically?
#### Right Answer: There exist some problems that cannot be solved algorithmically using any computer.
#### Corrections: Correct. An undecidable problem is one for which no algorithm can be constructed that is always capable of providing a correct yes-or-no answer. Some instances of an undecidable problem may have an algorithmic solution, but there is no algorithmic solution that could solve all instances of the problem.

#### Question 6: Which of the following algorithms display all integers between 1 and 20, inclusive, that are not divisible by 3?
#### Right Answer: Step 1:
``Set x to 1.
  Step 2: If x is divisible by 3, then do nothing; otherwise display x.
  Step 3: Increment x by 1.
  Step 4: Repeat steps 2 and 3 until x is greater than 20.``
#### Corrections: This algorithm displays the numbers 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, and 20. After 20 is displayed, x is incremented to 21. The value 21 is not displayed since it is a multiple of 3 and the algorithm terminates.

#### Question 7: In the following procedure, the parameter n is an integer greater than 2. Which of the following best describes the value returned by the procedure?
#### Right Answer: The procedure returns the sum of the integers from 1 to n.
#### Corrections: The procedure initially sets result to 1 and j to 2. In the REPEAT UNTIL loop, result is first assigned the sum of result and j, or 1 + 2. The value of j is then increased to 3. In each subsequent iteration of the loop, result is increased by each successive value of j (3, 4, 5, etc.) until j exceeds n. Therefore, the procedure returns the sum of the integers from 1 to n.

#### Question 8: A teacher has a goal of displaying the names of 2 students selected at random from a group of 30 students in a classroom. Any possible pair of students should be equally likely to be selected. Which of the following algorithms can be used to accomplish the teacher’s goal?
#### Right Answer:
``Step 1:
Assign each student a unique integer from 1 to 30.
Step 2:
Generate a random integer n from 1 to 30.
Step 3:
Select the student who is currently assigned integer n and display the student’s name.
Step 4:
The student who was selected in the previous step is assigned 0. All other students are reassigned a unique integer from 1 to 29.
Step 5:
Generate a new random integer n from 1 to 29.
 Step 6:
Select the student who is currently assigned integer n and display the student’s name.``
#### Corrections: This algorithm selects 1 student from the group of 30 students, then selects another student from the remaining 29 students. Any possible pair of students is equally likely to be selected.

#### Question 17: The procedure 'smallest' is intended to return the least value in the list 'numbers'. The procedure does not work as intended. For which of the following values of 'theList' will 'smallest (theList)' NOT return the intended value? Select two
#### Right Answer: theList <-- (40, 30, 20, 10)
#### Corrections: The procedure returns the first number it encounters that is less than the first number in the list. For the list open bracket, 40, 30, 20, 10, close bracket, the procedure returns 3 0, which is not the least value in the list.

#### Question 18: The following procedure is intended to return true if the list of numbers myList contains only positive numbers and is intended to return false otherwise. The procedure does not work as intended.
``PROCEDURE allPositive(myList)
{
index ← 1
len ← LENGTH(myList)
REPEAT len TIMES
{
IF(myList[index] > 0)
{
RETURN(true)
}
index ← index + 1
}
RETURN(false)
} ``
#### For which of the following contents of myList does the procedure NOT return the intended result?
#### Right Answer: (-1, 0, 1)
#### Corrections: The procedure traverses this list and eventually encounters the positive value 1. At this point, the procedure returns true when it should return false because the list does not contain only positive values.

#### Question 31: A student is creating an algorithm to display the distance between the numbers num1 and num2 on a number line. The following table shows the distance for several different values. Which of the following algorithms displays the correct distance for all possible values of num1 and num2 ?
#### Right Answer: 
``Step 1: Subtract num1 from num2 and store the result in the variable diff.
Step 2: Take the absolute value of diff and display the result. ``
#### Corrections: Subtracting num1 from num2 will give the difference between the two numbers. Taking the absolute value of the difference will give the distance as a positive number.

#### Question 34: A student is creating an algorithm to display the distance between the numbers num1 and num2 on a number line. The following table shows the distance for several different values. Which of the following algorithms displays the correct distance for all possible values of num1 and num2 ?
#### Right Answer: Finding the fastest route that visits every location among  n  locations, which requires  n!  possible routes be examined.
#### Corrections: As this algorithm has a factorial efficiency, it does not run in a reasonable amount of time. A heuristic approach can be used to find an approximate solution than can run in a reasonable amount of time.

#### Question 39: A social media site allows users to send messages to each other. A group of researchers gathered user data for the first 10 years of the site’s existence. Some of the data are summarized in the table below, along with some of the company milestones. The researchers noticed that the total number of registered users appears to be increasing at about a constant rate. If this pattern continues, which of the following best approximates the total number of registered users, in millions, in year 12 (two years after the last entry in the table)?
#### Right Answer: 31.2
#### Corrections: The total number of registered users appears to be increasing by about 0.5 million each year, so in year 12, the number of users can be approximated at 31.2 million (30.2 + 0.5 + 0.5).

## Final Test 2
### Score: 44/50
#### Question 1: Which of the following best describes the ability of parallel computing solutions to improve efficiency?
#### Right Answer: The efficiency of a solution that can be broken down into parallel portions is still limited by a sequential portion.
#### Corrections: Correct. Parallel computing solutions consist of a parallel portion and a sequential portion. When increasing the use of parallel computing in a solution, the efficiency of the solution is limited by the sequential portion. This means that at some point, adding parallel portions will no longer meaningfully increase efficiency.

#### Question 5: Which of the following activities is most likely to be successful as a citizen science project?
#### Right Answer: Collecting pictures of plants from around the world that can be analyzed to look for regional differences in plant growth.
#### Corrections: citizen science project requires data collection help from a wide range of people and this one is most accurate to that definition.

#### Question 12: Which of the following applications is most likely to benefit from the use of crowdsourcing?
#### Right Answer: An application that allows users to view descriptions and photographs of local landmarks
#### Corrections: Crowdsourcing is the practice of obtaining input or information from a large number of people via the Internet. Study key terms.

#### Question 41: The owner of a clothing store records the following information for each transaction made at the store during a 7-day period.

- The date of the transaction
- The method of payment used in the transaction
- The number of items purchased in the transaction
- The total amount of the transaction, in dollars
- Customers can pay for purchases using cash, check, a debit card, or a credit card.

#### Using only the data collected during the 7-day period, which of the following statements is true?
#### Right Answer: The total number of items purchased on a given date can be determined by searching the data for all transactions that occurred on the given date and then adding the number of items purchased for each matching transaction.
#### Corrections: For each transaction, the data includes the date of the transaction and the number of items purchased in the transaction. By searching the data to find all transactions that occurred on the given date, and then adding the number of items purchased in each of those transactions, the total number of items purchased on a given date can be determined.

#### Question 42: Which of the following statements describe how cloud computing has affected Internet communication? Select two answers.
#### Right Answer: Cloud computing has introduced new data-security concerns. (I only got one wrong so yeah)
#### Corrections: Cloud computing sites must consider security concerns in order to protect their users’ private data.

## Final Test 1
### Score: 43/50
#### Question 2: According to the domain name system (DNS), which of the following is a subdomain of the domain example.com?
#### Right answer: about.example.com
#### Corrections: I think I misread the answer choices. This is the right answer because the question never specified which region the domain came from so you can't add UK and about makes sense for a subdomain.

#### Question 24: Which of the following best explains how data is typically assembled in packets for transmission over the Internet?
#### Right Answer: Each packet contains data to be transmitted, along with metadata containing information used for routing the data.
#### Corrections: Data is being transmitted, not just bundled up

#### Question 37: The following code segment is intended to set max equal to the maximum value among the integer variables x, y, and z. The code segment does not work as intended in all cases. Which of the following initial values for x, y, and z can be used to show that the code segment does not work as intended?
#### Right Answer: x = 3, y = 2, z = 1
#### Corrections: OHHH OK SO, the function only works if y or z are the maximum values because the second if else statement isn't under the original if statement so it changes the max value to either y or z when executed.

#### Question 41: The figure below represents a network of physically linked computers labeled A through G. A line between two computers indicates that the computers can communicate directly with each other. Any information sent between two computers that are not directly connected must go through at least one other computer. For example, information can be sent directly between computers A and B, but information sent between computers A and C must go through other computers. What is the minimum number of connections that must be broken or removed in the network before computer E can no longer communicate with computer F?
#### Right Answer: 3
#### Corrections: Only need to take down lines connected to F. Once those lines are down, no one, not even E can connect.

#### Question 49: An Internet service provider (ISP) is considering an update to its servers that would save copies of the Web pages most frequently visited by each user. Which of the following is LEAST likely to occur as a result of the update?
#### Right Answer: Web sites that are not visited frequently might no longer be accessible to users.
#### Corrections: The actions of the ISP will only affect how frequently visited pages are loaded into Web browsers. Pages not saved by the ISP are still accessed as they were before.

#### Question 50: Digital images are often represented by the red, green, and blue values (an RGB triplet) of each individual pixel in the image. A photographer is manipulating a digital image and overwriting the original image. Which of the following describes a lossless transformation of the digital image?
#### Right Answer: Creating the negative of an image by creating a new RGB triplet for each pixel in which each value is calculated by subtracting the original value from 255. The negative of an image is reversed from the original; light areas appear dark, and colors are reversed.
#### Corrections: If a negative of the original image is made, each RGB triplet value will be computed by subtracting the original value from 255. The original value can then be restored by subtracting the new value from 255. This process is lossless because the exact original can be restored.

#### Question 50: Question is long so, basically given a segment of a student record storing database and asked what can I determine from the information.
#### Right Answer: I, II, and III
#### Corrections: All three options were correct. You could determine everything from the database.
