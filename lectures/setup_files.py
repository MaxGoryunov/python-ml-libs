import os
import random
import shutil
from pathlib import Path

def split_dataset(source_dir, train_dir, val_dir, num_samples_per_class=250):
    os.makedirs(os.path.join(train_dir, 'cat'), exist_ok=True)
    os.makedirs(os.path.join(train_dir, 'dog'), exist_ok=True)
    os.makedirs(os.path.join(val_dir, 'cat'), exist_ok=True)
    os.makedirs(os.path.join(val_dir, 'dog'), exist_ok=True)

    cat_files = [f for f in os.listdir(Path(source_dir)) if f.startswith('cat.') and f.endswith('.jpg')]
    dog_files = [f for f in os.listdir(Path(source_dir)) if f.startswith('dog.') and f.endswith('.jpg')]
    print(len(cat_files), len(dog_files))
    # return

    if len(cat_files) < num_samples_per_class * 2 or len(dog_files) < num_samples_per_class * 2:
        raise ValueError(f"Недостаточно файлов. Нужно как минимум {num_samples_per_class * 2} файлов каждого класса.")

    random.shuffle(cat_files)
    random.shuffle(dog_files)

    train_cat = cat_files[:num_samples_per_class]
    val_cat = cat_files[num_samples_per_class:num_samples_per_class*2]
    
    train_dog = dog_files[:num_samples_per_class]
    val_dog = dog_files[num_samples_per_class:num_samples_per_class*2]

    for filename in train_cat:
        src = os.path.join(source_dir, filename)
        dst = os.path.join(train_dir, 'cat', filename)
        shutil.copy2(src, dst)

    for filename in val_cat:
        src = os.path.join(source_dir, filename)
        dst = os.path.join(val_dir, 'cat', filename)
        shutil.copy2(src, dst)

    for filename in train_dog:
        src = os.path.join(source_dir, filename)
        dst = os.path.join(train_dir, 'dog', filename)
        shutil.copy2(src, dst)

    for filename in val_dog:
        src = os.path.join(source_dir, filename)
        dst = os.path.join(val_dir, 'dog', filename)
        shutil.copy2(src, dst)

    print(f"Скопировано {num_samples_per_class} изображений каждого класса в train_data")
    print(f"Скопировано {num_samples_per_class} изображений каждого класса в val_data")


source_directory = './lectures/train/'
train_directory = './lectures/data/train_data'
val_directory = './lectures/data/val_data'

split_dataset(source_directory, train_directory, val_directory, num_samples_per_class=250)
