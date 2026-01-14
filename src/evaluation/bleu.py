from sacrebleu import corpus_bleu

def compute_bleu(preds, refs):
    return corpus_bleu(preds, [refs]).score
