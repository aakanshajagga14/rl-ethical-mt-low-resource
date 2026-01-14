def coherence_score(sentences):
    return sum(len(s.split()) for s in sentences) / len(sentences)
