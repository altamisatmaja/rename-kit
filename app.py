import os
import shutil

image_directory = 'vendor'
image_names = [
    'thumbnail_vendor_1_1.jpg', 'thumbnail_vendor_1_2.jpg', 'thumbnail_vendor_1_3.jpg', 'thumbnail_vendor_1_4.jpg','thumbnail_vendor_1_5.jpg', 'thumbnail_vendor_1_6.jpg', 'thumbnail_vendor_1_6.jpg', 'thumbnail_vendor_1_7.jpg', 'thumbnail_vendor_1_8.jpg',
    'thumbnail_vendor_2_1.jpg', 'thumbnail_vendor_2_2.jpg', 'thumbnail_vendor_2_3.jpg', 'thumbnail_vendor_2_4.jpg','thumbnail_vendor_2_5.jpg', 'thumbnail_vendor_2_6.jpg', 'thumbnail_vendor_2_6.jpg', 'thumbnail_vendor_2_7.jpg', 'thumbnail_vendor_2_8.jpg',
    'thumbnail_vendor_3_1.jpg', 'thumbnail_vendor_3_2.jpg', 'thumbnail_vendor_3_3.jpg', 'thumbnail_vendor_3_4.jpg','thumbnail_vendor_3_5.jpg', 'thumbnail_vendor_3_6.jpg', 'thumbnail_vendor_3_6.jpg', 'thumbnail_vendor_3_7.jpg', 'thumbnail_vendor_3_8.jpg',
]

total_images = 96

def generate_new_names(total_images):
    new_names = []
    for i in range(1, total_images + 1):
        category = (i - 1) // 4 + 1 
        image_num = (i - 1) % 4 + 1
        new_names.append(f'image_{category}_{image_num}.jpg')
    return new_names

new_image_names = generate_new_names(total_images)

for i, new_name in enumerate(new_image_names):
    old_name = image_names[i % len(image_names)]
    old_path = os.path.join(image_directory, old_name)
    new_path = os.path.join(image_directory, new_name)
    
    if os.path.exists(old_path):
        shutil.copy2(old_path, new_path)
        print(f'Copied and renamed {old_name} to {new_name}')
    else:
        print(f'File {old_name} does not exist')
