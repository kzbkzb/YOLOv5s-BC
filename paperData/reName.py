import os

# 1. 获取一个要重命名的文件夹的名称：
folder_name = "./Annotations/"

# 2. 获取那个文件夹中所有的文件名字：
file_names = os.listdir(folder_name)

# 3. 循环用新名字代替旧名字
for name in file_names:
    old_file_name = os.path.join(folder_name, name)
    new_file_name = os.path.join(folder_name, name.split('图片')[1])
    os.rename(old_file_name, new_file_name)