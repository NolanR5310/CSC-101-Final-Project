3 files will be used in this program, NOT including this README file
1. driver.py
   1. This is where the program will run, it will have 2 functions.
   2. One function will read the BookData.csv file and return the list of all books
        a. This function is currently written in this file
   3. The other function will return a filtered list of books based on user input
        a. This function prototype is written in this file
   4. This file also includes definitions of all lists and dictionaries used
2. data.py
   1. This is where the class Book is defined
   2. Attributes of Title, Author, Rating, Price, Genre,  and Year
3. BookData.csv
   1. This is the file containing the data set of 550 books containing the same attributes from the data.py file above
4. test_driver.py
   1. This is the file that contains the test functions for driver.py. Tests include loading books from the .csv, filtering the books, and sorting the books.