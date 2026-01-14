import torch

class RLPolicy:
    def __init__(self, model):
        self.model = model

    def act(self, state):
        logits = self.model(state)
        probs = torch.softmax(logits, dim=-1)
        return torch.multinomial(probs.view(-1, probs.size(-1)), 1)
