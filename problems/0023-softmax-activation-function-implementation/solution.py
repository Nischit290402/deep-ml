import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    s = np.array(scores)
    shift = s - np.max(s)
    ex = np.exp(shift)
    ans = ex / np.sum(ex)
    return ans.tolist()
    pass