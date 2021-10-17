import requests
from requests.api import head

from engine.searched_item import SearchedItem

from common.logger import set_logger
logger = set_logger(__name__)

class PaypayAPI():
    MODE_CONFIG = {
        "search_items": {
            "url": "https://paypayfleamarket.yahoo.co.jp/api/v1/search",
            "key": "",
        },
        "item_detail": {
            "url": "https://paypayfleamarket.yahoo.co.jp/api/item/v2/items/{id}",
            "key": ""
        },
    }

    def meke_headers(self):
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
            "x-platform": "web",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://paypayfleamarket.yahoo.co.jp/",
            "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            "sec-ch-ua-platform": "Windows"
        }
    
    def make_request(self, mode: str, params: dict={}):
        self.meke_headers()
        url = self.MODE_CONFIG[mode]["url"].format(**params)
        res = requests.get(url, headers=self.headers, params=params)
        res.raise_for_status()
        return res.json()

    
    def fetch_item(self, item_id: str):
        try:
            params = {
                "id": item_id
            }
            res = self.make_request(mode="item_detail", params=params)
            return res
        except Exception as e:
            logger.error(e)
            return []
        
    
    def search_items_for_page(self, q: str, page: int=0, sort: str="price", order: str="asc", exclude_keyword: str="",
                              min_price: int=300, max_price: int=99999, status: str="open", item_condition: str="NEW,USED10,USED20",
                              shipping_payer_id: int=2):
        query = q + (" -" + " -".join(exclude_keyword.split()) if len(exclude_keyword.split()) >= 1 else "")
        params = {
            "result": 100,
            "query": query,
            "sort": sort,
            "order": order,
            "minPrice": min_price,
            "maxPrice": max_price,
            "itemStatus": status,
            "itemConditions": item_condition,
            "shipping_payer_id": shipping_payer_id,
            "page": page
        }
        print(params)

        try:
            res = self.make_request(mode="search_items", params=params)
            if res.get("items"):
                return self._extract_items(res["items"])
                # return res["items"]
            else:
                logger.info("data end")
                return []
        except Exception as e:
            logger.error(e)
            return []
        
    
    def search_items(self, q: str, page_limit: int=5, exlude_keyword: str="", min_price: int=300, max_price: int=99999, sort: str="price", order: str="asc", shipping_payer_id: int=2, item_condition: str="1,2,3"):
        items = []
        for page in range(page_limit):
            res = self.search_items_for_page(q, page, exclude_keyword=exlude_keyword, min_price=min_price, max_price=max_price, 
                                             sort=sort, order=order, shipping_payer_id=shipping_payer_id, item_condition=item_condition)
            if len(res) == 0:
                break
            items.extend(res)
            logger.info(f"page: {page + 1}")
            
        return items
    

    def _extract_items(self, items: list):
        results =[]
        for item in items:
            results.append(
                SearchedItem(
                    id = item.get("id"),
                    name = item.get("title"),
                    price = item.get("price"),
                    thumbnail_url = item.get("thumbnailImageUrl"),
                    site = "paypay"
                )
            )
            
        return results