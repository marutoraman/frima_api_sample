from engine.mercari_api import *

  
def test_search_items():
    mercari = MercariAPI()
    items = mercari.search_items("任天堂　スイッチ ライト 本体", page_limit=1, exlude_keyword="フィルム セット カバー ジャンク コントローラー", min_price= 5000, is_detail=True)
    print(len(items))
    print(items[0].__dict__)
    

def test_fetch_item():
    mercari = MercariAPI()
    item = mercari.fetch_item("m90146743211")
    import pprint
    print(item["data"]["description"])
    pprint.pprint(item["data"])