CREATE TABLE "Authors" (
	"author_id"	INTEGER UNIQUE,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	PRIMARY KEY("author_id" AUTOINCREMENT)
)