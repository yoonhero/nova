import torch
import numpy as np

tensor = torch.ones(4,4)
print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last column: {tensor[..., -1]}")
tensor[:, 1] = 0
print(tensor)


t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)


# this computes the matrix multiplication between two tensors
y1 = torch.ones(2, 2)
y2 = torch.ones(2, 2)

y3 = torch.rand_like(tensor)

z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)

torch.mul(tensor, tensor, out=z3)

print(y1, y2, y3, z1, z2, z3)

print("\n\n\n\n\n\n")

t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

n = np.ones(5)
t = torch.from_numpy(n)

print(n, t)

