import Image
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-t", dest='type', help="Type of shield to use, HOI2 DH Biger V, defaults to HOI2")
parser.add_argument("-f", dest='file', help="File to use, automaically resizes, recommended to use a 70 by 44 px file for best quality")
parser.add_argument("-d", dest='destination', help="File to export to, .bmp automaticly added")
args = parser.parse_args()

print("Europa Engine Shield Converter")

if args.file == None or args.destination == None:
    sys.exit("No file or destination chosen")

if args.type == "HOI2":
    mask = Image.open("masks/Shield_HOI2.png")
elif args.type == "DH":
    mask = Image.open("masks/Shield_DH.png")
elif args.type == "Birger":
    mask = Image.open("masks/Shield_Birger.png")
elif args.type == "V":
    mask = Image.open("masks/Shield_Vicky.png")
else:
    mask = Image.open("masks/Shield_HOI2.png")

def image_shield( str ):
   size = 70, 44
   im = Image.open(str)
   if im.size != size:
       print("Sizes not optimal")
   resize = im.resize(size)
   rotate = resize.rotate(-90)
   return rotate;

using_shield = image_shield( args.file )

background = Image.new('RGBA', (176,70), (255, 255, 255, 255))
for x in range(0, 4):
    background.paste(using_shield,(44*x,0))
	
alpha = mask.split()[3]

background2 = Image.new("RGB", background.size, (0, 0, 0))
background2.paste(background, alpha)

background2.save(args.destination + ".bmp")

print("Done!")
