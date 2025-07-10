import torch
from ultralytics.utils.torch_utils import select_device

print("Selected device:", select_device('0'))

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")

#py -3.12 gpu_checks.py