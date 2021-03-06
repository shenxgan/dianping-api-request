#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append("..")

from db import _db as db
from dianping import DianpingApi


if __name__ == '__main__':

    api = DianpingApi('85719554', 'b9aafd8a60e1435faf7ba3389cdb4e9a')
    business_id_list = []
    businesses = db.business.find()
    for business in businesses:
        business_id_list.append(str(business['business_id']))
    business_id_list = set(business_id_list)
    business_id_list = list(business_id_list)
    loop_count = len(business_id_list) / 40
    i = 0
    businesses = []
    while i <= loop_count:
        if i == loop_count:
            business_ids = business_id_list[i:]
        else:
            business_ids = business_id_list[i*40:(i+1)*40]
        i += 1
        print business_ids
        businesses += api.get_batch_businesses_by_id(business_ids)
    #db.batch_business.insert(businesses)
    for business in businesses:
        db.business.update({'business_id': business['business_id']}, {'$set': business}, upsert=True)
