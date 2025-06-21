from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageFont, ImageDraw
import uuid

app = Flask(__name__)

req = 0

chars_file = open("smash_characters.txt","r")
chars = chars_file.read().split('\n')
chars_file.close()

thumbs_file = open("thumbs_styles.txt","r")
thumbs = thumbs_file.read().split('\n')
thumbs_file.close()

@app.route('/')
def index():
    return render_template('index.html',chars=chars,thumbs=thumbs)

@app.route('/bulk')
def bulk():
    return render_template('bulk.html')

@app.route('/create', methods=['POST'])
def create():
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    char1 = request.form.get('char1').strip()
    char2 = request.form.get('char2').strip()
    left = request.form.get('left')
    right = request.form.get('right')
    thumbstyle = request.form.get('thumbstyle').strip()
    output_img = gen(p1,p2,left,right,char1,char2,thumbstyle)
    return render_template('create.html', output_img=output_img, prev_form=request.form,chars=chars,thumbs=thumbs)

def gen(p1,p2,round,msg2,char1,char2,thumbstyle):
    image = Image.open('thumbnail_styles/' + thumbstyle + '/back.png')
    draw = ImageDraw.Draw(image)
    f1=f2 = ImageFont.truetype('FOT-Rodin Pro UB.otf',73)
    f3=f4 = ImageFont.truetype('FOT-Rodin Pro UB.otf',65)

    w1, h1 = draw.textsize(p1, f1)
    dif1 = 0
    while w1 > 630:
        f1 = ImageFont.truetype('FOT-Rodin Pro UB.otf',f1.size-2)
        dif1 = dif1 + 1
        w1, h1 = draw.textsize(p1, f1)

    w2, h2 = draw.textsize(p2, f2)
    dif2 = 0
    while w2 > 630:
        f2 = ImageFont.truetype('FOT-Rodin Pro UB.otf',f2.size-2)
        dif2 = dif2 + 1
        w2, h2 = draw.textsize(p2, f2)

    w3, h3 = draw.textsize(round, f3)
    dif3 = 0
    while w3 > 630:
        f3 = ImageFont.truetype('FOT-Rodin Pro UB.otf',f3.size-2)
        dif3 = dif3 + 1
        w3, h3 = draw.textsize(round, f3)

    w4, h4 = draw.textsize(msg2, f4)
    dif4 = 0
    while w4 > 630:
        f4 = ImageFont.truetype('FOT-Rodin Pro UB.otf',f4.size-2)
        dif4 = dif4 + 1
        w4, h4 = draw.textsize(round, f4)

    char1 = Image.open('chars/' + char1 + '.png')
    char2 = Image.open('chars/' + char2 + '.png')
    image.paste(char1, (0,0),mask=char1)
    image.paste(char2, (639,0),mask=char2)
    
    overlay = Image.open('thumbnail_styles/' + thumbstyle + '/front.png')
    image.paste(overlay, (0,0), mask=overlay)
    draw.text((14+((608-w1)/2),16+dif1),p1,fill="white",font=f1,stroke_width=4,stroke_fill="black")
    draw.text((659+((608-w2)/2),16+dif2),p2,fill="white",font=f2,stroke_width=4,stroke_fill="black")
    draw.text((14+((608-w3)/2),629+dif3),round,fill="white",font=f3,stroke_width=4,stroke_fill="black")
    draw.text((659+((608-w4)/2),629+dif4),msg2,fill="white",font=f4,stroke_width=4,stroke_fill="black")
    filename = "generated/" + str(uuid.uuid4()) + ".png"
    image.save('static/' + filename)
    return url_for('static',filename=filename)
