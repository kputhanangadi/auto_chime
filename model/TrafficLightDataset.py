import os
from PIL import Image
import torch
from torch.utils.data import Dataset

class TrafficLightDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_filenames = [os.path.join(root_dir, label, f) for label in os.listdir(root_dir) for f in os.listdir(os.path.join(root_dir, label)) if f.endswith('.jpg')]

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        img_path = self.image_filenames[idx]
        image = Image.open(img_path).convert('RGB')
        label = int(os.path.basename(os.path.dirname(img_path)))
        if self.transform:
            image = self.transform(image)
        return image, label