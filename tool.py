import tkinter,json,pytesseract,urllib.request,difflib
from PIL import ImageGrab
from PIL import Image
from pynput import keyboard
# warframe.market request for all items
url= urllib.request.urlopen('https://api.warframe.market/v1/items')
string = url.read().decode('utf-8')# conversion
json_obj = json.loads(string)
payload = json_obj['payload']['items']['en']
items = [payload[item]['item_name'] for item in range(len(payload))]
print(items)
current = set()

COMBINATIONS = [{keyboard.Key.shift, keyboard.KeyCode(char='a')},
        {keyboard.Key.shift, keyboard.KeyCode(char='A')}]

def execute():
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
    im = ImageGrab.grab(bbox=(120,250,360,490))
    im.save("1.png")
    im = Image.open("1.png")
    # run ocr on image
    text = pytesseract.image_to_string(im, lang = "eng")
    if len(difflib.get_close_matches(text,items,1)) > 0:
        final = difflib.get_close_matches(text,items,1)[0]
        print(final)
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
# get warframe.market data from api on item...buyprice/sellprice/
# show current plat price on item(s)
# find buy orders for item, copy name/msg to clipboard
# selection with mouse cursor
