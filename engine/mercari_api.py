import requests
from requests.api import head
from engine.searched_item import SearchedItem

from common.logger import set_logger
logger = set_logger(__name__)

class MercariAPI():
    MODE_CONFIG = {
        "search_items": {
            "url": "https://api.mercari.jp/search_index/search",
            "key": "eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4Ijoic0V4dnNWRF9FZzlsRXZvaUtvbjZxQW1Kc2JqVUlKMmVxY1IyZHlrcnRSNCIsInkiOiJxb0pCQ0NwR05qd2FqemtDcmVBVkk5eFFqSjlLMjhIR2EyOW92elFUTG8wIn19.eyJpYXQiOjE2MzQ0NTQ5NjQsImp0aSI6IjU3YzQwNTMyLTc2OTUtNDEwZi1iNjI1LWE5MTkxMWYwNDY3MCIsImh0dSI6Imh0dHBzOi8vYXBpLm1lcmNhcmkuanAvc2VhcmNoX2luZGV4L3NlYXJjaCIsImh0bSI6IkdFVCJ9.pAEC_3VIc0A3eSmQMUrTGSljsQVq0N7gpSAbmNd-o6WqKvL12JBjlj793l8i_2KTi1uGGB0NPWdr6Gt8Z4F2uQ",
        },
        "item_detail": {
            "url": "https://api.mercari.jp/items/get",
            "key": "eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4Ijoic0V4dnNWRF9FZzlsRXZvaUtvbjZxQW1Kc2JqVUlKMmVxY1IyZHlrcnRSNCIsInkiOiJxb0pCQ0NwR05qd2FqemtDcmVBVkk5eFFqSjlLMjhIR2EyOW92elFUTG8wIn19.eyJpYXQiOjE2MzQ0NTQ5OTUsImp0aSI6IjU3YzQwNTMyLTc2OTUtNDEwZi1iNjI1LWE5MTkxMWYwNDY3MCIsImh0dSI6Imh0dHBzOi8vYXBpLm1lcmNhcmkuanAvaXRlbXMvZ2V0IiwiaHRtIjoiR0VUIn0.7mtRnkDsqS9UMBTIx9x2nOmcV67KtglNvde-YQ1zi8FQEpUgyF1c9dsYRrBiUrfq-VIamZRCoRDeJxjJ9JV_4g"
        },
    }
    
    def meke_headers(self, mode: str):
        '''
        リクエスト用のヘッダを生成
        '''
        # 実際にメルカリにアクセスしたRequestHeaderを踏襲する
        self.headers = {
            "dpop": self.MODE_CONFIG[mode]["key"], # dropは認証キーのようなもので、APIのエンドポイント毎に異なる（詳細は非公表なため不明）
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
            "x-platform": "web",
            "sec-fetch-dest": "empty",
            "sec-fetch-site": "cross-site",
            "origin": "https://jp.mercari.com",
            "referer": "https://jp.mercari.com/",
            "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            "sec-ch-ua-platform": "Windows"
        }
    
    
    def make_request(self, mode:str, params: dict={}):
        '''
        リクエストを作成して、リクエストを行い、結果を返す
        '''
        self.meke_headers(mode)
        url = self.MODE_CONFIG[mode]["url"]
        res = requests.get(url, headers=self.headers, params=params)
        res.raise_for_status()
        return res.json()
        
    
    def fetch_item(self, item_id: str):
        '''
        商品詳細ページの情報を取得
        '''
        pass
        
    
    def search_items_for_page(self, q: str, page: int=0, sort: str="price", order: str="asc", exclude_keyword: str="", category_id: str="",
                              min_price: int=300, max_price: int=99999, status: str="on_sale", item_condition: str="1,2,3",
                              shipping_payer_id: int=2):
        '''
        商品検索（１ページ分）
        '''
        pass
        
    
    def search_items(self, q: str, page_limit: int=5, exlude_keyword: str="", category_id: str="",
                     min_price: int=300, max_price: int=99999, sort: str="price", order: str="asc", shipping_payer_id: int=2, item_condition: str="1,2,3",
                     is_detail: bool=False):
        '''
        商品検索（複数ページ）
        '''
        pass
       
    
    def _extract_items(self, items: list):
        '''
        取得した結果を展開して、共通Item用のClassに格納する
        '''
        pass