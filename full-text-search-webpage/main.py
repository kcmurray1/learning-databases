import pandas as pd
from app.database.database import BookDatabase
from app import create_app
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
        for author in clean_authors(authors):   
            with BookDatabase("database/relational-books.db") as db:
                # Insert into Authors table
                author_id = db.insert_author(author)
                # Insert into Books table
                db.insert_book((author_id, price, title, category, month, year, description))

   
    
    


def main():
    app = create_app()
    app.run(debug=True)
    # csv_file = "./database/BooksDatasetSmall.csv"

    # populate_database(csv_file)


if __name__ == "__main__":
    main()