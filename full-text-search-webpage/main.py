from app import create_app
import pandas as pd
from app.database.database import BookDatabase

def clean_authors(authors):
    authors_cleaned = list()
    authors = authors.split(',')  
    print("BEFORE:", authors)
    for i in range(0, len(authors) - 1,2):

        last_name, first_name = authors[i:i + 2]
        last_name = last_name.replace("By ", "")
        last_name = last_name.replace(" and ", "")
        authors_cleaned.append((first_name.strip(), last_name.strip()))
    return authors_cleaned

def populate_database(file):
    book_frame = pd.read_csv(file)
    for title, authors, description, category, publisher, price, month, year in book_frame.values:
        with BookDatabase("./app/database/books_final.db") as db:
            # Insert into Books table
            book_id = db.insert_book((price, title, month, year, description))
            print(book_id)
            for author in clean_authors(authors):   
                # Insert into Authors table
                author_id = db.insert_author(author)

                # Insert into BookAuthors table
                db.insert_book_author(author_id, book_id)

def main():

    # csv_file = "./app/database/BooksDatasetSmall.csv"

    # populate_database(csv_file)
    app = create_app()
    app.run(debug=True)
   


if __name__ == "__main__":
    main()