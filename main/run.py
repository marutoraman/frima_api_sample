import os
import sys
import fire
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine.mercari_api import MercariAPI
from engine.paypay_api import PaypayAPI


def run(q: str, page_limit: int=5, exlude_keyword: str="", 
        min_price: int=300, max_price: int=99999, sort: str="price", order: str="asc", shipping_payer_id: int=2, item_condition: str="1,2,3"):
    
    mercari = MercariAPI()
    paypay = PaypayAPI()

    items = []
    items.extend(mercari.search_items(
        q, page_limit, exlude_keyword, min_price=min_price, max_price=max_price, 
        sort=sort, order=order, shipping_payer_id=shipping_payer_id, item_condition=item_condition
        ))
    items.extend(paypay.search_items(
        q, page_limit, exlude_keyword, min_price=min_price, max_price=max_price, 
        sort=sort, order=order, shipping_payer_id=shipping_payer_id, item_condition=item_condition
        ))
    df = pd.DataFrame()
    for item in items:
        df = df.append(item.__dict__, ignore_index=True)
    
    df.to_csv("item_data.csv", mode="w", encoding="utf-8_sig")
    

if __name__ == "__main__":
    fire.Fire(run)