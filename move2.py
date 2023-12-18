import os
import shutil

def move_images(src_folder, dest_folder):
    for filename in os.listdir(src_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Kiểm tra nếu file là ảnh
            shutil.move(os.path.join(src_folder, filename), dest_folder)  # Di chuyển file

src_folder = 'data\\text_img'
dest_folder = 'data\yu'
move_images(src_folder, dest_folder)