class Book:
    def __init__(self, title):
        self.title = title
        self.content = f"""Title: {self.title}\n"""

    def add_chapter(self, x):
        self.content += f"""# {x}\n"""

    def add_line(self, y):
        self.content += f"""{y}\n"""

    def write(self, n):
        filename = open(n, "wt")
        filename.write (self.content)
        filename.close()




