class Book:
    def __init__(self, title, page_count, year_published):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
            raise ValueError("page_count must be an integer")
        self.title = title
        self.page_count = page_count
        self.year_published = year_published

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
