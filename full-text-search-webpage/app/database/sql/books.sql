CREATE TABLE "Books" (
	"book_id"	INTEGER UNIQUE,
	"price"	REAL,
	"title"	TEXT,
	"month"	TEXT,
	"year"	INTEGER,
	"description"	TEXT NOT NULL DEFAULT 'No Description',
	PRIMARY KEY("book_id" AUTOINCREMENT)
)