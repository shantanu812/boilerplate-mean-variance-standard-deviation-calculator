import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError ("List must contain nine numbers.")
    arr=np.array(list)
    brr=arr.copy()
    arr=arr.reshape(3,3)
    mn=[arr.mean(axis=0).tolist(),arr.mean(axis=1).tolist(),brr.mean()]
    vr=[arr.var(axis=0).tolist(),arr.var(axis=1).tolist(),brr.var()]
    std=[arr.std(axis=0).tolist(),arr.std(axis=1).tolist(),brr.std()]
    mx=[arr.max(axis=0).tolist(),arr.max(axis=1).tolist(),brr.max()]
    mini=[arr.min(axis=0).tolist(),arr.min(axis=1).tolist(),brr.min()]
    sm=[arr.sum(axis=0).tolist(),arr.sum(axis=1).tolist(),brr.sum()]
    calculations={
        'mean': mn,
        'variance': vr,
        'standard deviation': std,
        'max': mx,
        'min': mini,
        'sum': sm
    }

    return calculations
