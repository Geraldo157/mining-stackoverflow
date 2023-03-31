from scrapy.item import Item, Field

# Specify what the code wants to mine on the website


class StackItem(Item):
    title = Field()
    url = Field()
    pass
