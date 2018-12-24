import tkinter,json,pytesseract,urllib.request,difflib
from PIL import ImageGrab
from PIL import Image
# warframe.market request for all items
url= urllib.request.urlopen('https://api.warframe.market/v1/items')
string = url.read().decode('utf-8')# conversion
json_obj = json.loads(string)
payload = json_obj['payload']['items']['en']

items = [payload[item]['item_name'] for item in range(len(payload))]

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
im = ImageGrab.grab(bbox=(120,250,360,490))
im.save("1.png")
im = Image.open("1.png")
# run ocr on image
text = pytesseract.image_to_string(im, lang = "eng")
print(text)
final = difflib.get_close_matches(text,items,1)[0]
print(final)


# to do
# get warframe.market data from api on item...buyprice/sellprice/
# show current plat price on item(s)
# support different resolutions...selection with mouse cursor?
