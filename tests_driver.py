import unittest
import driver
import data

class TestLibraryFunctions(unittest.TestCase):
    def setUp(self):
        # Sample book objects for testing
        self.sample_books = [
            data.Book("Book A", "Author One", 4.5, 100, 10, "Fiction", 2020),
            data.Book("Book B", "Author Two", 4.7, 150, 15, "Non Fiction", 2019),
            data.Book("Book C", "Author One", 4.7, 200, 8, "Fiction", 2021),
        ]

    # ----- load_books_from_csv -----

    def test_load_books_returns_list(self):
        result = driver.load_books_from_csv("BookData.csv")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_loaded_books_are_book_objects(self):
        result = driver.load_books_from_csv("BookData.csv")
        self.assertTrue(all(isinstance(b, data.Book) for b in result))

    # filter_books

    def test_filter_books_by_author(self):
        filtered = driver.filter_books(self.sample_books, "na", "Author One", (0, 20), "Fiction")
        self.assertEqual(len(filtered), 2)
        self.assertTrue(all("Author One" in b.authors for b in filtered))

    def test_filter_books_by_price_range(self):
        filtered = driver.filter_books(self.sample_books, "na", "na", (9, 11), "Fiction")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Book A")

    def test_filter_books_by_title_case_insensitive(self):
        filtered = driver.filter_books(self.sample_books, "book c", "na", (0, 20), "Fiction")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Book C")

    def test_filter_books_by_genre(self):
        filtered = driver.filter_books(self.sample_books, "na", "na", (0, 20), "Non Fiction")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].genre, "Non Fiction")

    def test_filter_books_sorting_by_rating_then_title(self):
        filtered = driver.filter_books(self.sample_books, "na", "na", (0, 20), "Fiction")
        self.assertEqual(filtered[0].title, "Book C")  # Same rating as A, but C comes first alphabetically

if __name__ == "__main__":
    unittest.main()