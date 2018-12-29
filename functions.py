from init import *

def item_ducats(name):
    name = name.replace(' ', '_').lower()
    url= urllib.request.urlopen('https://api.warframe.market/v1/items/'+name)
    string = url.read().decode('utf-8')
    json_obj = json.loads(string)
    ducats = json_obj['payload']['item']['items_in_set'][0]['ducats']
    return ducats

def item_plat(name):
    name = name.replace(' ', '_').lower()
    url= urllib.request.urlopen('https://api.warframe.market/v1/items/'+name+'/statistics')
    string = url.read().decode('utf-8')
    json_obj = json.loads(string)
    plat = json_obj['payload']['statistics_closed']['48hours'][0]['avg_price']
    return plat
