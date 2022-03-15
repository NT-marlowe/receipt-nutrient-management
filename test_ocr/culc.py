from dict import nutrition_facts
def culculation(text):
    nutrition = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for k, v in nutrition_facts.items():
        if k in text:
            for i in range(len(v)):
                nutrition[i] += v[i]
    return nutrition
