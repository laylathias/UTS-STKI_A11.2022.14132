# src/eval_ir.py

def precision_at_k(retrieved, relevant, k):
    retrieved_k = retrieved[:k]
    if k == 0:
        return 0.0
    return len(set(retrieved_k) & set(relevant)) / k

def recall(retrieved, relevant):
    if not relevant:
        return 0.0
    return len(set(retrieved) & set(relevant)) / len(relevant)

def f1_score(p, r):
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def average_precision(retrieved, relevant):
    score = 0.0
    hit = 0

    for i, doc in enumerate(retrieved, start=1):
        if doc in relevant:
            hit += 1
            score += hit / i

    if len(relevant) == 0:
        return 0.0

    return score / len(relevant)

def map_k(all_retrieved, all_relevant):
    total = 0
    for q in all_retrieved:
        ap = average_precision(all_retrieved[q], all_relevant[q])
        total += ap
    return total / len(all_retrieved)
