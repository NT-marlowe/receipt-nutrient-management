from dict import nutrition_facts
def culculation(text):
    # nutrition = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nutrition = [0] * 29
    for k, v in nutrition_facts.items():
        if k in text:
            for i in range(len(v)):
                nutrition[i] += v[i]
    protein = nutrition[0]
    carbohydrate = nutrition[2]
    lipid = nutrition[1]
    inorganic = sum(nutrition[4:16])/12
    vitamin = sum(nutrition[16:29])/13
    fiber = nutrition[3]
    nutrition_dict = {
        "タンパク質":protein,
        "炭水化物":carbohydrate,
        "脂質":lipid,
        "無機質":inorganic,
        "ビタミン":vitamin,
        "食物繊維":fiber,
    }
    return nutrition_dict
