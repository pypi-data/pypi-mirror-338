def add_fitter(img, fit_img, output_img):
    from PIL import Image
    import math
    flag = Image.open(fit_img)
    file = img
    if file:
        head = Image.open(file)
        width, height = flag.size
        flag2 = flag.crop((66, 0, height+66, height))
        for i in range(height):
            for j in range(height):
                color = flag2.getpixel((i, j))
                distance = int(math.sqrt(i**2+j**2))
                alpha = 255-distance//4
                if alpha<0:
                    alpha = 0
                new_color = color[0:-1]+(alpha, )
                flag2.putpixel((i, j), new_color)
        flag_new = flag2.resize(head.size)
        head.paste(flag_new, (0, 0), flag_new)
        head.save(output_img)

def text_painting(img, char:list, output:str=None):
    from PIL import Image

    img = Image.open(img)
    img = img.resize((60,60))
    img = img.convert('L')
    txt = ''
    for i in range(60):
        for j in range(60):
            txt += char[int(len(char) * (img.getpixel((j,i)) / 256))]
        txt += "\n"
    if output is not None:
        result=open(output,"w")
        result.write(txt)
        result.close()
    else:
        print(txt)