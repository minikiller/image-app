from PIL import Image


def sign_img(img_obj, logo_img_obj):
    final_img = Image.new("RGBA", img_obj.size, None)
    final_img.paste(img_obj)
    # final_img.save("first.png")
    h, w = img_obj.size
    h1, w1 = logo_img_obj.size
    logo_img_box = h-h1, w-w1
    final_img.alpha_composite(logo_img_obj, logo_img_box)

    return final_img


image1 = Image.open("static/img/woman1.png")
image2 = Image.open("img/stage.jpg")
h, w = image1.size
h1, w1 = image2.size
print(image1.size)
print(image2.size)
img1 = image1.convert('RGBA')
img2 = image2.convert('RGBA')
print(img1)
print(img2)
# Image.blend(img1,img2,0).show()
sign_52 = sign_img(img2, img1)
sign_52.save("hello.png")
