#coding: utf-8

import os


#  创建一个索引
def create_index():
    command = "curl -XPUT 'localhost:9200/customer?pretty'"
    print os.system(command)

    command = "curl 'localhost:9200/_cat/indices?v'"
    print os.system(command)


# 索引并查询一个文档
def find_doc():
    cmd = '''
    curl -XPUT 'localhost:9200/customer/external/1?pretty' -d '
    {
        "name": "DYL"
    }'
    '''
    print os.system(cmd)

    cmd = 'curl -XGET "localhost:9200/customer/external/1?pretty"'
    print os.system(cmd)


# 删除一个索引
def delete_index():
    cmd = 'curl -XDELETE "localhost:9200/customer?pretty"'
    print os.system(cmd)


def main():
    #create_index()
    find_doc()
    delete_index()


if __name__ == '__main__':
    main()