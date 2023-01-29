import sqlite3

with sqlite3.connect("mydb.db") as connection:
    cursore = connection.cursor()
    with open("BooksAndAuthors.sql", "r") as sql:
        req = sql.read()
        cursore.executescript(req)
    cursore.execute("""
        INSERT INTO Authors (Name, Surname) VALUES ("Новиков", "Савелий");
        INSERT INTO Authors (Name, Surname) VALUES ("Гаврилов", "Константин");
        INSERT INTO Authors (Name, Surname) VALUES ("Лебедев", "Дмитрий");
        INSERT INTO Authors (Name, Surname) VALUES ("Маркина", "Мария");
        INSERT INTO Authors (Name, Surname) VALUES ("Ларин", "Артём");
        INSERT INTO Authors (Name, Surname) VALUES ("Виноградова", "Василиса");
        INSERT INTO Authors (Name, Surname) VALUES ("Григорьева", "Виктория");
        INSERT INTO Authors (Name, Surname) VALUES ("Кондратьева", "София");
        """)
    cursore.execute("""
        INSERT INTO Books (Name, Year) VALUES ("Не оборачивайся", "2024");
        INSERT INTO Books (Name, Year) VALUES ("Бесконечная история", "2016");
        INSERT INTO Books (Name, Year) VALUES ("Последняя надежда", "2018");
        INSERT INTO Books (Name, Year) VALUES ("Потерянные души", "2020");
        INSERT INTO Books (Name, Year) VALUES ("Родственные души", "1984");
        INSERT INTO Books (Name, Year) VALUES ("Между двух миров", "2022");
        INSERT INTO Books (Name, Year) VALUES ("Дом на третьей улице", "1994");
        INSERT INTO Books (Name, Year) VALUES ("Серый кот", "2023");

        """)
    cursore.execute("""
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("1", "2");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("6", "8");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("3", "1");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("4", "7");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("3", "2");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("4", "3");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("2", "4");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("6", "1");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("1", "2");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("3", "8");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("4", "3");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("7", "4");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("8", "5");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("4", "6");
        INSERT INTO BooksAndAuthors (ID_books, ID_authors) VALUES ("6", "2");
        """)
# №1 Вывести Авторов по названию Книги
    cursore.execute("""
        Select Books.ID
        From Books
        WHERE name == "Между двух миров";

        SELECT Authors.ID
        FROM BooksAndAuthors
        WHERE ID_books == 6;
        -- 
        SELECT Authors.Name
        FROM Authors
        WHERE ID In (8,1,2);
        """)
# №2 Вывести Книги у которых год издания больше или равен 2020 у Автора указав его фамилию
    cursore.execute("""
        SELECT Books.ID
        FROM Books
        WHERE Books.Year >= 2020;

        SELECT ID_authors
        FROM BooksAndAuthors
        WHERE ID_books in(1,4,6,8);

        SELECT Authors.Surname, Books.Name
        FROM Authors, Books
        WHERE Authors.ID In (2,8,7,3,1,2,3,5,6,2) AND Books.Year >= 2020;
    """)
# №3 Удалить Книгу по названию из таблицы (при этом связь должна удаляться автоматически)
    name = input("Введите имя книги когорое хотите удалить: ")
    cursore.executemany ("""
        SELECT Books.ID
        FROM Books
        WHERE Books.name == "?";

        DELETE FROM BooksAndAuthors
        WHERE ID_books == 6;
    """, name)