def self_critical_step(model, reward_fn, sample, reference):
    baseline = reward_fn(model(sample), reference)
    sampled = reward_fn(model(sample), reference)
    return sampled - baseline
