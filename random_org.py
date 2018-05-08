# coding:utf-8
import requests
import ast


def random_get(max_=10, min_=1, num=1):
    a = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "ddcdd8bd-09a0-44e9-bb09-cb49010a80ba",
            "n": num,
            "min": min_,
            "max": max_,
            "replacement": True,
            "base": 10
        },
        "id": 1
    }

    r = requests.post(url="https://api.random.org/json-rpc/1/invoke", json=a)
    return ast.literal_eval(r.content)["result"]["random"]["data"]


if __name__ == '__main__':
    print random_get(max_=100, min_=1, num=5)
