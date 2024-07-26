CREATE TABLE "Categories" (
	"category_id"	INTEGER UNIQUE,
	"name"	TEXT NOT NULL DEFAULT 'uncategorized',
	PRIMARY KEY("category_id" AUTOINCREMENT)
)