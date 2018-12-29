from init import *
# warframe.market request for all items
url= urllib.request.urlopen('https://api.warframe.market/v1/items')
string = url.read().decode('utf-8')# conversion
json_obj = json.loads(string)
payload = json_obj['payload']['items']['en']
items = [payload[item]['item_name'] for item in range(len(payload))]
user32 = ctypes.windll.user32
current = set()

COMBINATIONS = [{keyboard.Key.delete}]

def execute():
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
    # top left item im = ImageGrab.grab(bbox=(120,250,360,490))
    #0.7,0.17,0.94,0.83 
    #im = ImageGrab.grab(bbox=(1800,250,2450,1200))
    im = ImageGrab.grab(bbox=(user32.GetSystemMetrics(0)*0.7,user32.GetSystemMetrics(1)*0.17,user32.GetSystemMetrics(0)*0.94,user32.GetSystemMetrics(1)*0.83))
    im.save("1.png")
    im = Image.open("1.png")
    # run ocr on image
    text = pytesseract.image_to_string(im, lang = "eng")
    if len(difflib.get_close_matches(text,items,1)) > 0:
        final = difflib.get_close_matches(text,items,1)[0]
        print(final)
        print('Ducats:',item_ducats(final))
        print('Plat:',item_plat(final))
        item_open(final)
    else:
        print('no matches.')
    
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]) and not key in current:
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
               
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# to do
# show current plat price on item(s) on the right
# button on the right that opens to browser for market page
