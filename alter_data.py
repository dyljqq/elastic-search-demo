#coding: utf-8

import os


def main():
    cmd = '''
    curl -XPOST 'localhost:9200/customer/external/_bulk?pretty' -d '
    {"index":{"_id":"1"}}
    {"name": "John Doe" }
    {"index":{"_id":"2"}}
    {"name": "Jane Doe" }'
    '''

    cmd = 'curl -XGET "localhost:9200/customer/external/1?pretty"'
    print os.system(cmd)


if __name__ == '__main__':
    main()