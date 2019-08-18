from PIL import Image
import os

def webp_to_jpg(img_url):
  im = Image.open(img_url)
  name = img_url.split("/")[-1]+'.jpg'
  image = im.save(name)
def download_img(img_url):
  try:
    img = requests.get(img_url)
    if img.status_code == 200:
      root = 'img//'
      path = img_url.split("/")[-1]
      with open(root+path,'wb') as f:
        f.write(img.content)
    else:
      print(img.status_code)
  except Exception as ex:
    print('---出错继续---')
    pass

def main():
  # url = 'https://i3.hoopchina.com.cn/hupuapp/bbs/119406715768253/thread_119406715768253_20181119235216_s_93998_o_w_720_h_1280_13439.jpg?x-oss-process=image/resize,w_800/format,webp'
  url = "thread_119406715768253_20181119235216_s_93998_o_w_720_h_1280_13439.webp"
  image = webp_to_jpg(url)

main()

