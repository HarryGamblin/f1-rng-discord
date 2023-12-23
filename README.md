They wanted to create a block of code that would give a true/false output depending on if a given number was even or odd. Very easy way to do this would be to divide the number by 2 and check the remainder. If it's zero the number is even, if not it's odd. But rather than do that he painstakingly wrote out each individual number from 0 upwards to the highest number the block of code would realistically ever be given and all of their respective outputs.

This is bad because
1) Not scalable, if for whatever reason the number the function could receive gets higher than you'll have to go back and do this process for all the numbers leading up to it.

2) Error-prone, if for whatever reason this function receives a higher number than expected, it won't return anything and potentially will crash the game.

3) Not readable, takes up a huge amount of space in the code editor.