class Book:
    def __init__(self, title, author, publication_year):
        self.title = str(title)
        self.author = str(author)
        self.year = int(publication_year)
    
    def __del__(self):
        return f"Deleting {self.year}"
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    

    