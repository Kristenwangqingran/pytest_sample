#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project :pytest_sample
@File :seller_flash_sale.py
@Author :jing.wang@shopee.com
@Date :28/05/2024 11:07
"""
import requests
url = "https://test.shopee.sg/api/v4/flash_sale/get_all_itemids"
params = {
    "need_personalize": True,
    "promotionid": 23244,
    "sort_soldout": True,
    "tracker_info_version": 1
}
res = requests.get(url=url, params=params)
print(res.status_code)
print(res.json()['data']['promotionid'])