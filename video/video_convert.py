# 先用 ffmpeg 等工具将视频转换为图片（每张图片对应视频的一帧），再运行

from PIL import Image
import os

frames_dir = "frames" # 存放视频帧的文件夹
txt_dir = "txt_files" # 存放 txt 文件的文件夹
char_w = 16 # 字符宽度
char_h = 32 # 字符高度

def convert_image(path, save_path):
    """转换为黑白图片"""
    img = Image.open(path)
    img = img.convert("L")

    color_v = []
    for i in range(256):
        if i <= 80:
            color_v.append(0)
        else:
            color_v.append(1)
    img = img.point(color_v, "1")

    img.save(save_path)

# 确保程序目录下有用于存放 txt 文件的文件夹
if not os.path.isdir(txt_dir):
    if os.path.isfile(txt_dir):
        os.remove(txt_dir)
    os.mkdir(txt_dir)

# 更改图片颜色, 转换图片到黑白并保存
frames_list = os.listdir(frames_dir)
for i in range(len(frames_list)):
    print(
        "(1/2) 更改图片颜色 ({}%)".format(
            round(
                i / (len(frames_list) - 1) * 100
            )
        ),
        end="\r",
        flush=True
    )
    convert_image(
        os.path.join(frames_dir, frames_list[i]), 
        os.path.join(txt_dir, str(i + 1)) + os.path.splitext(frames_list[i])[1]
    )

# 将黑白图片转换为 txt
frames_list = os.listdir(txt_dir)
for i in range(len(frames_list)):
    print(
        "(2/2) 转换图片 ({}%)".format(
            round(
                i / (len(frames_list) - 1) * 100
            )
        ),
        end="\r",
        flush=True
    )
    img = Image.open(os.path.join(txt_dir, frames_list[i]))
    image_size_x = img.size[0]
    image_size_y = img.size[1]
    img = img.convert("RGB")

    text = ""
    for y in range(0, image_size_y, char_h):
        for x in range(0, image_size_x, char_w):
            if img.load()[x, y][0] == 255:
                text += "0"
            else:
                text += "1"
        text += "\n"
    
    os.remove(os.path.join(txt_dir, frames_list[i]))
    with open(
        os.path.join(
            txt_dir, 
            os.path.splitext(
                frames_list[i]
            )[0] + ".txt"
        ),
        "w", 
        encoding="utf-8"
    ) as f_obj:
        f_obj.write(text)
