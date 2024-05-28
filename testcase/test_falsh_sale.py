#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project :pytest_sample
@File :test_falsh_sale.py
@Author :jing.wang@shopee.com
@Date :23/04/2024 15:57
"""
import requests


class TestFlashSale:
    def test_flash_sale_invalid_promotionid(self):
        url = "https://test.shopee.sg/api/v4/flash_sale/get_all_itemids"
        params = {
            "need_personalize": True,
            "promotionid": 23244,
            "sort_soldout": True,
            "tracker_info_version": 1
        }
        res = requests.get(url=url, params=params)
        assert res.status_code == 200
        assert res.json()['data']['promotionid'] == None

    def test_flash_sale_valid_promotionid(self):
        url = "https://test.shopee.sg/api/v4/flash_sale/get_all_itemids"
        params = {
            "need_personalize": True,
            "promotionid": 217555847557120,
            "sort_soldout": True,
            "tracker_info_version": 1
        }
        res = requests.get(url=url, params=params)
        assert res.status_code == 200
        assert res.json()['data']['promotionid'] != None

    def test_flash_sale_version_error(self):
        url = "https://test.shopee.sg/api/v4/flash_sale/get_all_itemids"
        params = {
            "need_personalize": True,
            "promotionid": 217555847557120,
            "sort_soldout": True,
            "tracker_info_version": 2
        }
        res = requests.get(url=url, params=params)
        assert res.status_code == 200
        assert res.json()['error'] != 0
