#!/usr/bin/env python
# encoding: utf-8
import datetime
import json


def read_file():
    json_file_path = 'weibospider/output/tweet_spider_by_keyword_20230514151451.jsonl'
    ids = ''
    # 文件中的每一行都存有json数据，读取每一行中的id字段
    with open(json_file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.strip()
            if line:
                json_line = json.loads(line)
                ids = ids + ' ' + (json_line['user']['_id'])
    # 将ids写入文件
    res_file_name = 'weibospider/output/user_info_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.jsonl'
    with open(res_file_name, 'w', encoding='UTF-8') as f:
        f.write(ids)


if __name__ == '__main__':
    read_file()
