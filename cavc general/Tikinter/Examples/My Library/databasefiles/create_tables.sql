CREATE TABLE books (
	book_id	int IDENTITY(1,1) PRIMARY KEY,
	book_name	varchar(255) NOT NULL,
	book_author	varchar(255) NOT NULL,
	book_page	varchar(255) NOT NULL,
	book_language	varchar(255) NOT NULL,
	book_status	INTEGER DEFAULT 0
);
CREATE TABLE members (
	member_id	int IDENTITY(1,1) PRIMARY KEY,
	member_name	varchar(255) NOT NULL,
	member_phone	varchar(255) NOT NULL
);
CREATE TABLE borrows (
	borrow_id	int IDENTITY(1,1) PRIMARY KEY,
	bbook_id	varchar(255),
	bmember_id	varchar(255)
);
CREATE TABLE sqlite_sequence (
	name	varchar(255),
	seq	INTEGER
);
