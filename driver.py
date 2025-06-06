
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
            book_instance = data.Book(
                title=row["Name"],
                authors=row["Author"],
                rating=float(row["User Rating"]),
                reviews=int(row["Reviews"]),
                price=int(row["Price"]),
                year=int(row["Year"]),
                genre=row["Genre"]
            )
            books.append(book_instance)
    return books
def filter_books(books: list[data.Book], search_title: str, search_author: str,
                 search_price_range: tuple[int, int], search_genre: str) -> list[data.Book]:
    filtered = []
    for b in books:
        if search_title.lower() != "na" and search_title.lower() not in b.title.lower():
            continue
        if search_author.lower() != "na" and search_author.lower() not in b.authors.lower():
            continue
        if not (search_price_range[0] <= b.price <= search_price_range[1]):
            continue
        if search_genre.lower() != b.genre.lower():
            continue
        filtered.append(b)
    return sorted(filtered, key=lambda x: (-x.rating, x.title.lower()))

def display_menu():
    print("\n📚 Welcome to the Library Book Tracker 📚")
    print("1. Search books with filters")
    print("2. Show all books")
    print("3. Exit")


def run_interface():
    list_of_books = load_books_from_csv("BookData.csv")
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            user_title = input("Enter desired title (or 'na'): ")
            user_author = input("Enter desired author (or 'na'): ")
            user_min_price = int(input("Enter minimum price: "))
            user_max_price = int(input("Enter maximum price: "))
            user_genre = input("Enter genre (Fiction or Non Fiction): ")

            results = filter_books(list_of_books, user_title, user_author, (user_min_price, user_max_price), user_genre)

            if results:
                print(f"\nFound {len(results)} matching book(s):\n")
                for b in results:
                    print(b)
            else:
                print("No books matched your criteria.")

        elif choice == "2":
            print(f"\nShowing all {len(list_of_books)} books:\n")
            for b in list_of_books:
                print(b)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    run_interface()

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
