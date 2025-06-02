
#The initial function will open the csv data
    #it will take the csv data and read it
    #then it will return the list of all books called list_of_books
import csv
import data

def load_books_from_csv(filename):
    books = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = data.Book(
                title=row["Name"],
                authors=row["Author"],
                rating=float(row["User Rating"]),
                reviews=int(row["Reviews"]),
                price=int(row["Price"]),
                year=int(row["Year"]),
                genre=row["Genre"]
            )
            books.append(book)
    return books

list_of_books = load_books_from_csv("BookData.csv")
print(list_of_books)

#The central function evaluates a book value based on the provided filters
#The function will take in 4 user inputs.
    #Enter a desired title, if none, type na
    #Enter a desired author, if none type na
    #Enter your price range (2 values)
    #Would you like to see fiction or non-fiction? Enter Fiction or non-fiction.


#The function will return a list of book titles along with the corresponding attributes
    #ie: author, rating(any number 0-5, based on x number of reviews), price, genre and year published
    #the list will be returned in order from best ranked to worst ranked (descending order with 5 being the best)
    #If two books have the same rating, they should be arranged in alphabetical order

#The initial data list is defined as list_of_books
#The final list which will returned the filtered list of books from the central function will be defined as final_list
#No dictionaries will be defined in this program
