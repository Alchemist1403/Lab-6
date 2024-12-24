class Book:

    def __init__(self, name, number_of_pages, minutes_for_page, number_of_pictures):
        self.name = name
        self.number_of_pages = number_of_pages
        self.minutes_for_page = minutes_for_page
        self.number_of_pictures = number_of_pictures

    def time_of_reading(self):
        print(f"Time of reading: {self.number_of_pages * self.minutes_for_page} min")

    def __add__(self,other):
        return Book(
            f"{self.name} + {other.name}",
            self.number_of_pages + other.number_of_pages,
            self.minutes_for_page + other.minutes_for_page,
            self.number_of_pictures + other.number_of_pictures
            )


class Encyclopedia(Book):

    def __init__(
            self,
            name,
            number_of_pages,
            minutes_for_page,
            number_of_pictures,
            number_of_articles
            ):
        Book.__init__(self,name, number_of_pages, minutes_for_page, number_of_pictures)
        self.number_of_articles = number_of_articles

    def articles_per_page(self):
        print(f"Articles per page: {round(float(self.number_of_articles)/float(self.number_of_pages))}")


class Phone_directory(Book):

    def __init__(
            self,
            name,
            number_of_pages,
            minutes_for_page,
            number_of_pictures,
            number_of_phone_numbers
            ):
        Book.__init__(self, name, number_of_pages, minutes_for_page, number_of_pictures)
        self.number_of_phone_numbers = number_of_phone_numbers

    def phone_numbers_per_page(self):
        print(f"Phone numbers per page: {round(float(self.number_of_phone_numbers)/float(self.number_of_pages))}")


# Examples
book1 = Book("IT",1184,2.5,30)
print(book1.name)
book1.time_of_reading()

book2 = Encyclopedia("Encyclopedia of Crystals",288,3,40,245)
print(book2.name)
book2.time_of_reading()
book2.articles_per_page()

book3 = Phone_directory("BT Teesside",136,4,0,18000)
print(book3.name)
book3.time_of_reading()
book3.phone_numbers_per_page()

book4 = book1 + book2
print(f"New book(name): {book4.name}")
print(f"New book(pages): {book4.number_of_pages}")
