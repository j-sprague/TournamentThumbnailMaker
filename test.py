from PIL import Image, ImageFont, ImageDraw

image = Image.open('template.png')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('FOT-Rodin Pro UB.otf',73)
smol = ImageFont.truetype('FOT-Rodin Pro UB.otf',60)

p1 = input("First player: ")
p2 = input("Second player: ")
round = input("Round: ")
msg2 = input("Message 2: ")
char1 = input("Char1: ")
char2 = input("Char2: ")

w1, h1 = draw.textsize(p1, font)
w2, h2 = draw.textsize(p2, font)
w3, h3 = draw.textsize(round, smol)
w4, h4 = draw.textsize(msg2, smol)


char1 = Image.open('chars/' + char1 + '.png')
char2 = Image.open('chars/' + char2 + '.png')

image.paste(char1, (0,111),mask=char1)
image.paste(char2, (639,111),mask=char2)

draw.text((13+((608-w1)/2),16),p1,fill="white",font=font,stroke_width=4,stroke_fill="black")

draw.text((659+((608-w2)/2),16),p2,fill="white",font=font,stroke_width=4,stroke_fill="black")

overlay = Image.open('template2.png')
image.paste(overlay, (0,0), mask=overlay)

draw.text((13+((608-w3)/2),629),round,fill="white",font=smol,stroke_width=4,stroke_fill="black")

draw.text((659+((608-w4)/2),629),msg2,fill="white",font=smol,stroke_width=4,stroke_fill="black")

image.show()

# 608x92 box
