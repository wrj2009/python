# 将每一帧的 txt 文件合并到一个 txt 文件里，这样就可以方便地导入 Scratch 列表
# 写得很烂
import os

files = []

for i in range(0, len(os.listdir("txt_files"))-1):
    with open("txt_files/{}.txt".format(i + 1), "r", encoding="utf-8") as f_obj:
        file = f_obj.read()
    file = file.replace("\n", "")
    files.append(file)
    print("处理了 {} 个文件, 剩余 {} 个".format(i + 1, 3150 - i), end="\r", flush=True)  # 这里是当时为了偷懒，直接把实际数量写进去，第 19 行也一样

with open("list.txt", "w", encoding="utf-8") as f_obj:
    f_obj.write("")
with open("list.txt", "a", encoding="utf-8") as f_obj:
    for i in range(len(files)):
        f_obj.write(files[i] + "\n")
        print("保存了 {} 个项目, 剩余 {} 个".format(i + 1, 3150 - i), end="\r", flush=True)
   
