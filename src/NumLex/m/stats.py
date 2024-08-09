import math

def ungrp_mean(data: list[float]) -> float:
    res = 0
    for i in data:
        res = res + i
    return (res/len(data))

def grp_mean(xi: list[float], fi: list[float]) -> float:
    total_fi = 0
    for i in fi:
        total_fi = total_fi + i

    xifi = []
    for i,j in zip(xi,fi):
        xifi.append(i * j)

    total_xifi = 0
    for i in xifi:
        total_xifi = total_xifi + i

    return (total_xifi/total_fi)

def median(data: list[float]) -> float:
    no_obs = "even" if len(data) % 2 == 0 else "odd"

    if no_obs == "odd":
        term = (len(data) + 1) / 2
        data.sort()
        return data[math.floor(term) - 1]
    else:
        term = ((len(data) / 2) + ((len(data) + 1) / 2)) / 2
        data.sort()
        return data[math.floor(term) - 1]
    
def ungrp_mode(xi: list[float],fi: list[float]) -> float:
    max_key = 0
    cnt = 0
    for i,j in zip(xi,fi):
        if max_key == 0:
            max_key = cnt
        if j > fi[max_key]:
            max_key = cnt
        cnt += 1
    return xi[max_key]

def raw_mode(data: list[float]) -> float:
    mode = 0
    for item in data:
        if item > mode:
            mode = item
    return mode

def var(data: list[float]) -> float:
    mean = ungrp_mean(data)
    deviations = []
    for i in data:
        deviations.append((i - mean))
    
    squared_deviations = []
    for i in deviations:
        squared_deviations.append((i * i))

    total_sqaured_deviations = 0
    for i in squared_deviations:
        total_sqaured_deviations = total_sqaured_deviations + i
    
    return (total_sqaured_deviations/len(data))

def std_dev(data: list[float]) -> float:
    mean = ungrp_mean(data)
    deviations = []
    for i in data:
        deviations.append((i - mean))
    
    squared_deviations = []
    for i in deviations:
        squared_deviations.append((i * i))

    total_sqaured_deviations = 0
    for i in squared_deviations:
        total_sqaured_deviations = total_sqaured_deviations + i
    
    return ((total_sqaured_deviations/len(data)) ** 0.5)