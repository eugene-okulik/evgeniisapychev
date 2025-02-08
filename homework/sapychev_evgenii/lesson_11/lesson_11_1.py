import random


class Book():
    material = 'Бумага'
    text = True
    book_name = ''
    bok_author = ''
    book_len = random.randint(1, 999999)
    ISBN = random.randint(100000, 999999)
    book_reserved = True

    def __init__(self, book_name, bok_author, book_len, book_reserved):
        self.book_name = book_name
        self.bok_author = bok_author
        self.book_len = book_len
        self.book_reserved = book_reserved

    def info(self):
        if self.book_reserved:
            print(f'Название: {self.book_name}, Автор: {self.bok_author}, {self.book_len}: 500, Материал:'
                  f'{self.material}, Зарезервирована')
        else:
            print(f'Название: {self.book_name}, Автор: {self.bok_author}, {self.book_len}: 500, Материал:'
                  f'{self.material}')


class textbook(Book):
    school_subject = ''
    school_subject_number_class = random.randint(1, 11)
    availability_of_tasks = True

    def __init__(self, book_name, bok_author, book_len, school_subject, school_subject_number_class, book_reserved):
        super().__init__(book_name, bok_author, book_len, book_reserved)
        self.school_subject = school_subject
        self.school_subject_number_class = school_subject_number_class

    def info_subject_book(self):
        if self.book_reserved:
            print(f'Название: {self.book_name}, Автор: {self.bok_author}, страниц: {self.book_len}, предмет:'
                   f'{self.school_subject}, класс: {self.school_subject_number_class}, зарезервирована')
        else:
            print(f'Название: {self.book_name}, Автор: {self.bok_author}, страниц: {self.book_len}, предмет:'
                   f'{self.school_subject}, класс: {self.school_subject_number_class}')


book1 = Book('Идиот', 'Достоевский', 100, True)
book2 = Book('Война и мир', 'Толстой', 200, False)
book3 = Book('Преступления и наказание', 'Достоевский', 300, False)
book4 = Book('Мастер и маргарита', 'Булгаков', 400, False)
book5 = Book('Гарри Поттер', 'Роулинг', 500, False)
subject_book1 = textbook('Алгебра', 'Архимед', 100, 'Математика', 8, True)
subject_book2 = textbook('Теоретическая физика', 'Энштейн', 200, 'Физика', 8, False)
subject_book3 = textbook('Млекопитающие', 'Гиппократ', 300, 'Биология', 8, False)


book1.info()
subject_book1.info_subject_book()
