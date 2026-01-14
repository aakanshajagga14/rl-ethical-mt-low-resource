import torch
import torch.optim as optim
from models.transformer_mt import TransformerMT

def train(model, data, epochs):
    optimizer = optim.Adam(model.parameters())
    loss_fn = torch.nn.CrossEntropyLoss()
    for _ in range(epochs):
        for x, y in data:
            optimizer.zero_grad()
            out = model(x)
            loss = loss_fn(out.view(-1, out.size(-1)), y.view(-1))
            loss.backward()
            optimizer.step()
