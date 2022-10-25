from PIL import Image, ImageFont, ImageDraw
import csv
import uuid
import qrcode

def idcardgen(path):

  names = []

  with open(path, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
      for item in row:
        names.append(item)
  csvfile.close()
  names = names[1:]

  for name in names:
    blank_idcard = Image.open(r" -- PATH TO BLANK ID CARD TEMPLATE -- ")
    W, H = blank_idcard.size
    image_editable = ImageDraw.Draw(blank_idcard)
    name_font = ImageFont.truetype(r' -- PATH TO FONT FILE (.TTF) --',45)
    w, h = name_font.getsize(name.upper())
    image_editable.text(((W-w)/2, 730), name.upper(), (0, 0, 0), font=name_font) # Co-ordinates of the name and RGB values of the colour that is to be used for the name
    downfile = (" -- PATH TO DIRECTORY TO STORE THE GENERATED ID CARDS -- " + name + ".png")

    qr_content = {"id": uuid.uuid1(), "name": name,} # Generating a unique id for each participant and storing it in a json format
    qr = qrcode.QRCode(box_size=9, border=2)
    qr.add_data(qr_content)
    qr.make() # Generating the qr code with the json that contains the name and the uid
    img_qr = qr.make_image()
    blank_idcard.paste(img_qr, (160, 350)) # Co-ordinates of the QR
    blank_idcard.save(downfile)
  return names



# ----------------------##########################-------------------------------


if __name__ == '__main__':
  names = idcardgen(' --PATH TO CSV CONTAINING ALL THE NAMES-- ')
  print(names)