import torch

class RewardModel:
    def compute(self, prediction, reference):
        return (prediction == reference).float().mean()
