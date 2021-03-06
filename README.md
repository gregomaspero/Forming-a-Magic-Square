# Forming a Magic Square
Link to problem: https://www.hackerrank.com/challenges/magic-square-forming/problem

Link to my solution: https://www.hackerrank.com/challenges/magic-square-forming/forum/comments/981593

------------------------------------------
PROBLEM: 

<img width="778" alt="Screen Shot 2021-07-16 at 4 13 23 PM" src="https://user-images.githubusercontent.com/59319786/125997613-85be1414-e317-4fa6-a791-5de0e2b2a857.png">

DETAILED Mathematical + Coding explanation by Gregorio Maspero:

To begin with, this problem involves a lot of mathematics. Even though it may seem that there are plenty of different Magic Squares, there are only 8 different magic squares which, in fact, result from the modification of a unique magic solution. First we are going to go with the "Magic Square" facts:

1- The sum of each line should be 15: This one can be easily calculated. The sum of the first row should be equal to the sum of the second row and equal to the sum of the third row. Since the numbers from each row does not alter the sum of any other row, then as the sum of all the numbers in the square(1 to 9) is 45 and we have 3 rows, then we can conclude that 45/3=15 is the sum of each row.

2- The center number of the square should be 5: For this case we will evaluate what happens when this number is higher than 5 and lower than 5. a - Higher than 5: It is impossible to have a number higher than 5 in the center since this number has “contact” with all the numbers in the square. This means that the number in the middle will always share one sum with the higher number of the square which is 9. So if we place any number higher than 5 such as 6, then we will always have at least one sum which will be higher than 15 since (9+6+x), being x at least 1, will always be higher than 15. b - Lower than 4: The center number cannot be less than 4 because we will need to use numbers higher than 9 which we cannot. It is important to notice that there are 4 different “lines” that go through the center that needs to sum 15: one horizontal, one vertical and two diagonal. This means that we will need 4 pairs of different numbers that sum at least 11 which is impossible without repeating. i.e: if we place a 4 in the middle we will need a "5 and a 6" on two opposite sides to sum 11, then a "3 and a 8", "2 and 9" and finally a "1 and 10" which is absurd. Same thing happens for numbers 1, 2 and 3. Thus, the center number must be 5.

3- Number 9 should go in one of the 4 middle edges: We will show this case by demonstrating that number 9 cannot go in any corner. If we place a 9 in any corner (having a 5 in the center as we already demonstrated), then we should also place a 1 in the opposite corner to sum 15 (only option). So far we have used numbers 1,5,9 but we also need to sum 6 between the two missing numbers from each row and column that the number 9 is placed in. This is impossible to achieve since there is no way to form two different pairs that sum 6 with the remaining numbers; the only possible pair is (2,4).

Having all this data we can start solving the magic square just like a reduced Sudoku. First we are going to place the number 9 in the middle top, thus the number 1 in the middle bottom. The first row needs to sum 15 so the only pair possible to use is pair (2,4). The thing here is that we can place either number on either place so we will have two possibilities. When we place any of these numbers, the rest of the magic square is forced to be completed with one unique solution. If we place the number 2 in the top left corner we will end up with the matrix: [2,9,4],[7,5,3],[6,1,8] but if we place the 2 in the top right corner we will end up with the matrix: [4,9,2],[3,5,7],[8,1,6] which is like a side inverted version of the first matrix.

We are not done yet. Just like we mentioned before, the number 9 can go in any of the 4 middle edges of the square. We are not writing all these down, but we can demonstrate that we will only have two solutions for each position of the number 9 in any of the middle edges. These solutions will be similar to the 2 solutions we have already found but “rotated” depending where the number 9 is located. We can easily visualize this by imagining we have a rubik's cube on our hand and we start rotating the front side of the cube clockwise. All the numbers (in this case the colors) will still have the same neighbors so the sum will not change. We can rotate this front side 4 times until it becomes the same, so we will have a total of 2*4 = 8 different magic squares.

Now it is just a matter of coding an algorithm that will rotate these 2 solutions clockwise to get all the possible magic squares and then compare all these 8 magic squares with the given matrix. Finally we will stay with the magic square that will require less cost. The code can be seen [here](https://github.com/gregomaspero/Forming-a-Magic-Square/blob/main/solution.py)

