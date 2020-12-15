import json

import requests

from common.api import SHOW_PACK_ORDERS, get_url, BUY_BACK


class Bag(object):
    ITEM_STATUS = {
        0:"NORMAL",
        1:"取回中",
        2:"",
        3:"",
        4:"",
        5:"",
    }

    def __init__(self, user):
        self.user = user
        self.order_item = {}

    def _show_bag(self, page_size):
        _requests = self.user.get_request_client()
        url = get_url(SHOW_PACK_ORDERS)
        return _requests.get(
            url,
            params=page_size,
            headers={"authorization": self.user.token}
        )

    def show_bag(self):
        page_param = {
                "page": 1,
                "size": 1,
                "sort": 0,
        }
        count_resp = self._show_bag(page_param)
        count = json.loads(count_resp.text)["data"]["totalElements"]
        # 重设总数量
        page_param["size"] = count
        return self._show_bag(page_param)

    def load_all_in_bag(self):
        resp = self.show_bag()
        list_data = json.loads(resp.text)["data"]["content"]
        if list_data is not None :
            # 遍历是个Map
            for map_item in list_data:
                status = map_item.get("takeStatus")
                # 分组
                sort_list = self.order_item.get(status)
                if sort_list is None:
                    sort_list = []
                    self.order_item[status] = sort_list
                sort_list.append(map_item)

    def buy_back(self, id_arr):
        _requests = requests
        url = get_url(BUY_BACK)
        return _requests.post(
            url,
            json=id_arr,
            headers={"authorization": self.user.token}
        )






