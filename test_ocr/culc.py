from dict import nutrition_facts
def culculation(text):
    # nutrition = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nutrition = [0] * 29
    for k, v in nutrition_facts.items():
        if k in text:
            for i in range(len(v)):
                nutrition[i] += v[i]
    protein = nutrition[0]
    carbon = nutrition[2]
    fat = nutrition[1]
    mineral = sum(nutrition[4:16])/12
    vitamin = sum(nutrition[16:29])/13
    fiber = nutrition[3]
    nutrition_list = [protein, carbon, fat, mineral, vitamin, fiber]
    return nutrition_list
