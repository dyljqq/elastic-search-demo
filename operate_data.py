# coding: utf-8

import os


def main():
    cmd = 'curl -XPOST "localhost:9200/bank/account/_bulk?pretty" --data-binary @/Users/jiqinqiang/Desktop/elastic_search/demo/accounts.json'

    cmd = '''
    curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
    {
        "query": {"match_all":  {}}
    }
    '
    '''
    os.system(cmd)


if __name__ == '__main__':
    main()
    
