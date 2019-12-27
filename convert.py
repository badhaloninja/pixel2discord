from PIL import Image
import os, sys

alpha = False			# Alpha for each pixel (Fully transparent pixels ignore this)
filename = 'user1.png'	# File name

def GetInput(message=""):
    if sys.version_info >= (3,0):
        return input(message)
    else:
        return raw_input(message)

def warn(message):
	print("WARNING: "+message)
	GetInput("Press Enter to continue...")

directory = "./"+filename+"_out"+"/"
im = Image.open(filename, 'r')
width, height = im.size

if width > 27:
	warn("After 27 pixels (emojis) wide they no longer display as big emojis in discord,\n current width is: "+str(width))

if height > 50:
	warn("Isn't "+str(height)+" lines a bit too tall?")

pix_val = list(im.getdata()) 
def rgb2hex(rgb, num=True):
	hex_result = "".join([format(val, '02X') for val in rgb])
	return (("#" if num else "")+hex_result)
pix_val_flat = [x for sets in pix_val for x in sets]
color_pallet = []
for x in pix_val:
	if alpha == True:
		y = x[:4]
	else:
		if x != (0, 0, 0, 0):
			y = x[:3]
		else:
			y = x[:4]
	if y not in color_pallet:
		color_pallet += [y]


if len(color_pallet) >= 50:
	warn("Unless boosted Discord servers can only have 50 non-animated emojis!")

color_pallet_hex_out = []
if not os.path.exists(directory):
    os.makedirs(directory)
for rgb in color_pallet:
	color_pallet_hex_out = str(rgb2hex(rgb))
	if rgb != (0, 0, 0, 0):
		if alpha == True:
			im_new = Image.new("RGBA", (1, 1), color_pallet_hex_out)
		else: 
			im_new = Image.new("RGB", (1, 1), color_pallet_hex_out)
		im_new.save(directory+color_pallet_hex_out+".png")
	else:
		im_new = Image.new("RGBA", (1, 1), color_pallet_hex_out)
		im_new.save(directory+"Transp"+".png")

f = open(directory+"disp.txt", "w")
color_pallet_hex_out = ()
out_hex_emojis = ""
i = 0
for rgb in pix_val:
	if i == width:
		out_hex_emojis += "\n"
		i = 0
	i += 1
	if rgb != (0, 0, 0, 0):
		if alpha == True:
			color_pallet_hex_out = str(rgb2hex(rgb[:4],False))
		else: 
			color_pallet_hex_out = str(rgb2hex(rgb[:3],False))
		out_hex_emojis += ":"+color_pallet_hex_out+":"
	else:
		out_hex_emojis += ":"+"Transp"+":"
f.write(out_hex_emojis)
f.close()

print("Done")
