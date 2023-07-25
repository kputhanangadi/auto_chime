import os
from PIL import Image
import torch
from torch.utils.data import Dataset


class TrafficLightDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_filenames = [
            os.path.join(root_dir, label, f)
            for label in os.listdir(root_dir)
            for f in os.listdir(os.path.join(root_dir, label))
            if f.endswith(".jpg")
        ]
        self.label_map = {"0_green": 0, "1_yellow": 1, "2_red": 2, "3_not": 3}

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        img_path = self.image_filenames[idx]
        image = Image.open(img_path).convert("RGB")
        label = os.path.basename(os.path.dirname(img_path))
        label = self.label_map[label]
        if self.transform:
            image = self.transform(image)
        return image, label
