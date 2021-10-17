import datetime

class SearchedItem():
    
    def __init__(self, id: str, name: str=None, price: int=None, thumbnail_url: str=None, 
                 description: str=None, 
                 start_at: datetime=None, item_condition: int=None, favorited_count: int=None,
                 category_name: str=None, seller_ratings: int=None, site: str=None):
        self.id = id
        self.name = name
        self.price = price
        self.thumbnail_url = thumbnail_url
        self.description = description
        self.start_at = start_at
        self.item_condition = item_condition
        self.favorited_count = favorited_count
        self.category_name = category_name
        self.seller_ratings = seller_ratings
        self.site = site