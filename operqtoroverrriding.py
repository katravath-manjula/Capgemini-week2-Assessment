class Book:
    def __init__(self, title, author):  # Fixed the constructor name
        self.title = title
        self.author = author

    def __add__(self, other):  # Fixed operator overloading method
        if isinstance(other, Book):
            com_title = f'{self.title} & {other.title}'
            return Book(com_title, self.author)  # You might want to adjust the author handling

    def __str__(self):  # Fixed the string representation method
        return f'{self.title} by {self.author}'


b = Book("Wings of Fire", "Kalam")
b1 = Book("My Life Story", "Kalam")
b_s = b + b1
print(f'Book series: {b_s}')  # This will now work correctly
