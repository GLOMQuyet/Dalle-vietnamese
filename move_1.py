import os
import shutil

def move_files(source_directory, destination_directory):
    # Kiểm tra xem thư mục đích có tồn tại chưa, nếu chưa thì tạo mới
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Duyệt qua tất cả các thư mục con trong thư mục nguồn
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_directory, file)

            # Di chuyển file
            shutil.move(source_path, destination_path)
            print(f"Đã di chuyển '{file}' từ '{source_path}' đến '{destination_path}'")

# Thay đổi đường dẫn của thư mục nguồn và thư mục đích theo nhu cầu của bạn
source_directory = 'data\images'
destination_directory = 'data\\text_c10'

move_files(source_directory, destination_directory)
