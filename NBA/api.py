import requests
import json

Match_List_Url = 'http://bifen4m.qiumibao.com/json/list.htm'


def match_list_request(url):
    response = requests.get(url)
    match = json.loads(response.text)


def main():
    match_list_request(Match_List_Url)


if __name__ == '__main__':
    main()
