CREATE TABLE "BookCategories" (
"book_id" INTEGER NOT NULL,
"category_id" INTEGER NOT NULL,
FOREIGN KEY ("book_id") REFERENCES "Books"("book_id"),
FOREIGN KEY ("category_id") REFERENCES "Categories"("category_id"),
PRIMARY KEY ("book_id", "category_id")
)