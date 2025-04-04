from torch.utils.data import DataLoader
from .datasets import TextDataset

def load_data(data_path):
    with open(data_path, "r") as f:
        data = f.readlines()
    return data

def create_dataloader(data, batch_size, seq_len):
    dataset = TextDataset(data, seq_len=seq_len)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False, drop_last=True)
    return dataloader
