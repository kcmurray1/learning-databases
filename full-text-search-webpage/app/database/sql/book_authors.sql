CREATE TABLE "BookAuthors" (
"author_id" INTEGER,
"book_id" INTEGER,
FOREIGN KEY ("author_id") REFERENCES "Authors"("author_id"),
FOREIGN KEY ("book_id") REFERENCES "Books"("book_id"),
PRIMARY KEY ("author_id", "book_id")
)