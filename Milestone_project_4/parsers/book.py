from locators.book_locators import BookLocators

class BookParser:
    RATINGS={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }
    def __init__(self, parent):
        self.parent=parent
    def __repr__(self):
        return f'<Book {self.name} costs {self.price} and has a rating of {self.rating} out of 5 stars>'
    @property
    def name(self):
        locator=BookLocators.NAME
        return self.parent.select_one(locator).attrs['title']
    
    @property
    def link(self):
        locator=BookLocators.LINK
        return self.parent.select_one(locator).attrs['href']
    
    @property
    def price(self):
        locator=BookLocators.PRICE
        return self.parent.select_one(locator).string
    
    @property
    def rating(self):
        locator=BookLocators.RATING
        rating_classes=self.parent.select_one(locator).attrs['class']
        rating_class=[e for e in rating_classes if e != 'star-rating']
        rating_number=BookParser.RATINGS.get(rating_class[0])
        return rating_number