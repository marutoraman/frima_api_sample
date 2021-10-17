from engine.paypay_api import *


def test_search_items():
    paypay = PaypayAPI()
    items = paypay.search_items("任天堂　スイッチ ライト 本体", page_limit=1, exlude_keyword="フィルム セット カバー ジャンク コントローラー", min_price= 5000)
    
    print(len(items))
    print(items[0])
    for item in items:
        print(item.__dict__)
    

def test_fetch_item():
    mercari = PaypayAPI()
    item = mercari.fetch_item("z93496554")
    import pprint
    pprint.pprint(item)