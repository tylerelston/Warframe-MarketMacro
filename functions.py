from init import *

def item_price(name):
    name = name.replace(' ', '_').lower()
    url= urllib.request.urlopen('https://api.warframe.market/v1/items/'+name)
    string = url.read().decode('utf-8')
    json_obj = json.loads(string)
    ducats = json_obj['payload']['item']['items_in_set'][0]['ducats']
    print(ducats)
