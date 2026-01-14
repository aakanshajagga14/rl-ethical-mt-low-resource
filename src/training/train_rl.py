import torch
from models.rl_policy import RLPolicy
from models.reward_model import RewardModel

def train_rl(model, data, epochs):
    policy = RLPolicy(model)
    reward_model = RewardModel()
    optimizer = torch.optim.Adam(model.parameters())
    for _ in range(epochs):
        for state, ref in data:
            action = policy.act(state)
            reward = reward_model.compute(action, ref)
            loss = -reward
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
