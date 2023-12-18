import os
import shutil

folder1 = 'Data\images'
folder2 = 'Data\\text_c10'

# Lặp qua tất cả các thư mục con trong folder1 và folder2
for subfolder1, subfolder2 in zip(os.listdir(folder1), os.listdir(folder2)):
    subfolder1_path = os.path.join(folder1, subfolder1)
    subfolder2_path = os.path.join(folder2, subfolder2)

    # Kiểm tra xem cả hai thư mục con có cùng tên không
    if subfolder1 == subfolder2:
        # Lặp qua tất cả các tệp trong thư mục con của folder2
        for file in os.listdir(subfolder2_path):
            file_path = os.path.join(subfolder2_path, file)
            # Di chuyển tệp sang thư mục con tương ứng của folder1
            shutil.move(file_path, subfolder1_path)
        shutil.rmtree(subfolder2_path)