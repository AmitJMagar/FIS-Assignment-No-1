# FIS-Assignment-No-1

Assume that the Romania map from the text and lecture has been changed such that all roads are 1 mile long. Write a Python program that finds optimal paths between a given pair of cities using Iterative Deepening Search (IDS). Your IDS will need to be a graph search. Because there are cycles in the map, revisiting cities can lead to an infinite loop.

The file A1 init code.zip available through MyCourses contains a program SearchGraph.py. The program reads a graph from a text file (for this assignment, use the provided file romania), and the names for the initial and goal city names. Your program will output the following:

(a) During the execution of iterative deepening, print the search tree each time all of the search tree nodes at the depth limit for the current iteration of IDS have been visited.

(b) At the end of the search:
i. If a solution exists, return the list of cities in the solution, beginning with the initial city and ending with the goal city.
ii. Otherwise, return a list containing the string ‘FAILED SEARCH.’ You need to modify the file SearchGraph.py, and provide a text file tests.txt, that shows the execution of your program for 3 pairs of cities:
    • Arad to Bucharest,
    • two additional city pairs of your choosing (interesting cases).

A bash shell script test has been provided, which you will modify to automate the execution of your test cases (see the
README for details).

Submit SearchGraph.py, tests.txt, romania map file, and your updated test script as the .zip file a1.zip.

# Map for the assignment is also below

![romania-graph](https://user-images.githubusercontent.com/20141798/35662691-7d0dbc72-06e7-11e8-942c-4718f079bb8f.png)
