import torch

def tensor_to_float(tensor_list):
    """
    Convert a list of tensors to a list of list(type: float)
    """
    return [[float(val) for val in sub_list] for sub_list in tensor_list.tolist()]

def tensor_list_to_int(tensor_list: torch.Tensor):   
    """
    Convert elements from float to int
    """
    return [int(val) for val in tensor_list.tolist()]