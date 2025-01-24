

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        return self.page.goto(url)
