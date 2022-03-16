"""
nutrition = [タンパク質, 脂質, 炭水化物, 食物繊維, 
K, Ca, Mg, P, 
Fe, Zn, Cu, Mn, I, Se, Cr, モリブテン, 
ビタミンA, D, E, K, B1, B2, ナイアシン, 
B6, B12, 葉酸, 
パントテン酸, ビオチン, C]
"""
nutrition_facts = {
    "あおさ":[2, 0, 0, 5, 5, 3, 5, 0, 3, 0, 4, 5, 5, 1, 5, 4, 1, 0, 1, 0, 0, 1, 4, 0, 3, 3, 0, 3, 1],
    "のり"  :[3, 0, 0, 5, 5, 1, 5, 3, 5, 1, 3, 4, 5, 1, 2, 3, 5, 0, 3, 3, 4, 5, 5, 2, 5, 5, 1, 3, 4],
    "こんぶ":[0, 0, 0, 5, 5, 4, 5, 0, 3, 0, 0, 0, 5, 5, 5, 4, 0, 0, 0, 3, 1, 0, 0, 0, 0, 3, 0, 3, 0],
    "昆布":[0, 0, 0, 5, 5, 4, 5, 0, 3, 0, 0, 0, 5, 5, 5, 4, 0, 0, 0, 3, 1, 0, 0, 0, 0, 3, 0, 3, 0],
    "ひじき":[0, 0, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 5, 3, 2, 1, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    "わかめ":[0, 0, 0, 2, 2, 2, 3, 0, 1, 0, 0, 2, 5, 4, 4, 4, 2 ,0, 0, 3, 0, 0, 0, 1, 2, 0, 0, 3, 0],
    "いんげんまめ":[0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 2, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    "えんどう":[2, 1, 0, 3, 1, 0, 1, 1, 3, 1, 2, 5, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
    "エンドウ":[2, 1, 0, 3, 1, 0, 1, 1, 3, 1, 2, 5, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
    "そらまめ":[2, 1, 0, 2, 0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    "そら豆":[2, 1, 0, 2, 0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    "大豆":[3, 2, 0, 4, 3, 0, 3, 2, 4, 1, 5, 2, 0, 0, 0, 0, 5, 0, 0, 2, 0, 3, 0, 1, 2, 0, 5, 1, 2, 0],
    "だいず":[3, 2, 0, 4, 3, 0, 3, 2, 4, 1, 5, 2, 0, 0, 0, 0, 5, 0, 0, 2, 0, 3, 0, 1, 2, 0, 5, 1, 2, 0],
    "なっとう":[1, 0, 0, 1, 1, 0, 1, 1, 2, 0, 2, 0, 0, 1, 0, 5, 0, 0, 0, 5, 0, 1, 0, 0, 0, 2, 2, 0, 0],
    "納豆":[1, 0, 0, 1, 1, 0, 1, 1, 2, 0, 2, 0, 0, 1, 0, 5, 0, 0, 0, 5, 0, 1, 0, 0, 0, 2, 2, 0, 0],
    "たまご":[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 2, 0],
    "タマゴ":[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 2, 0],
    "卵":[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 2, 0],
    "あじ":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 5, 0, 0, 0, 0],
    "アジ":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 5, 0, 0, 0, 0],
    "あなご":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 3, 0, 2, 0, 0, 0, 1, 0, 5, 0, 0, 0, 0],
    "いしだい":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 1, 3, 0, 0, 0, 0],
    "いわし":[5, 1, 0, 0, 2, 5, 3, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 5, 0, 1, 0, 0],
    "イワシ":[5, 1, 0, 0, 2, 5, 3, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 5, 0, 1, 0, 0],
    "しらす":[3, 0, 0, 0, 0, 3, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 5, 1, 0, 0, 0],
    "うなぎ":[2, 2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 3, 5, 0, 0, 5, 0, 4, 0, 3, 2, 2, 0, 5, 0, 1, 1, 0],
    "かつお":[2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 5, 0, 0, 0, 0],
    "かます":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 5, 0, 0, 0, 0],
    "かれい":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 5, 0, 0, 2, 0],
    "かんぱち":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 5, 0, 0, 0, 0],
    "きす":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5, 0, 0, 0, 0],
    "きびなご":[4, 0, 0, 0, 1, 5, 2, 5, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 1, 5, 0, 1, 0, 0],
    "金目鯛":[1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0],
    "キンメダイ":[1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0],
    "ぎんざけ":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 5, 0, 1, 0, 0],
    "銀鮭":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 5, 0, 1, 0, 0],
    "紅鮭":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 2, 5, 0, 1, 0, 0],
    "マサバ":[2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 1, 1, 5, 2, 5, 0, 0, 0, 0],
    "まさば":[2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 1, 1, 5, 2, 5, 0, 0, 0, 0],
    "さんま":[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 2, 0, 0, 0, 3, 2, 5, 0, 0, 0, 0],
    "サンマ":[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 2, 0, 0, 0, 3, 2, 5, 0, 0, 0, 0],
    "ししゃも":[2, 1, 0, 0, 0, 2, 0, 2, 1, 1, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1, 1, 0],
    "シシャモ":[2, 1, 0, 0, 0, 2, 0, 2, 1, 1, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1, 1, 0],
    "しまあじ":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 4, 2, 5, 0, 0, 0, 0],
    "シマアジ":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 4, 2, 5, 0, 0, 0, 0],
    "真鯛":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 1, 0, 0],
    "まだい":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 1, 0, 0],
    "太刀魚":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
    "すけとうだら":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
    "たらこ":[2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 5, 5, 0, 0, 0, 0, 5, 0, 3, 1, 5, 1, 5, 1, 3, 1, 1],
    "タラコ":[2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 5, 5, 0, 0, 0, 0, 5, 0, 3, 1, 5, 1, 5, 1, 3, 1, 1],
    "辛子明太子":[2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1, 1, 5, 0, 5, 0, 2, 0, 3],
    "真鱈":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    "にしん":[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 2, 5, 0, 1, 0, 0],
    "数の子":[2, 0, 0, 0, 0, 0, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 5, 2, 1, 0, 0],
    "ひらめ":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 1, 3, 2, 3, 0, 0, 1, 0],
    "ヒラメ":[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 1, 3, 2, 3, 0, 0, 1, 0],
    "ブリ":[2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 1, 1, 4, 2, 5, 0, 1, 0, 0],
    "ぶり":[2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 1, 1, 4, 2, 5, 0, 1, 0, 0],
    "ほっけ":[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 5, 0, 1, 0, 0],
    "鮪":[2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 3, 0, 0, 0, 0],
    "まぐろ":[2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 3, 0, 0, 0, 0],
    "マグロ":[2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 3, 0, 0, 0, 0],
    "あさり":[2, 0, 0, 0, 0, 0, 1, 0, 5, 1, 1, 1, 2, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 2, 0],
    "アサリ":[2, 0, 0, 0, 0, 0, 1, 0, 5, 1, 1, 1, 2, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 2, 0],
    "アワビ":[3, 0, 0, 0, 0, 0, 1, 1, 1, 0, 4, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0, 0, 0],
    "牡蠣":[0, 0, 0, 0, 0, 0, 1, 0, 1, 5, 5, 0, 3, 5, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
    "サザエ":[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 4, 3, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    "シジミ":[0, 0, 0, 0, 0, 1, 0, 0, 5, 1, 2, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 5, 0, 0, 0, 0],
    "しじみ":[0, 0, 0, 0, 0, 1, 0, 0, 5, 1, 2, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 5, 0, 0, 0, 0],
    "蛤":[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
    "ホタテ":[1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0, 0, 0],
    "アボカド":[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    "イチゴ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3],
    "いちご":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3],
    "苺":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3],
    "梅干":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "柿":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 3],
    "みかん":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "蜜柑":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "グレープフルーツ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "ゆず":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    "レモン":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    "キウイ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    "パイン":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "バナナ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "サツマイモ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    "さつまいも":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    "里芋":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "サトイモ":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ジャガイモ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "じゃがいも":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "アスパラガス":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    "いんげん":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "インゲン":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "枝豆":[1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 5, 0, 0, 0, 1, 1, 0, 0, 0, 0, 5, 0, 1, 1],
    "豆苗":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 3, 5, 1, 0, 0, 0, 0, 2, 0, 0, 3],
    "オクラ":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    "かぼちゃ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "カボチャ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "カリフラワー":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 4],
    "キャベツ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 2],
    "きゅうり":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "キュウリ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ごぼう":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "ゴボウ":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "小松菜":[0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 5, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    "しそ":[0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 3, 2, 0, 0, 0, 5, 5, 0, 3, 5, 0, 1, 0, 0, 0, 2, 0, 0, 1],
    "春菊":[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1, 5, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    "生姜":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ズッキーニ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "そら豆":[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1],
    "タケノコ":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "玉ねぎ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "チンゲンサイ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    "トマト":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "白菜":[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 0, 0, 4],
    "なす":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ナス":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "茄子":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ニガウリ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 3],
    "ゴーヤ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 3],
    "ニラ":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "人参":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    "にんじん":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    "ニンジン":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    "ニンニク":[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 2, 0, 0, 0],
    "ピーマン":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5],
    "ブロッコリー":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 5, 0, 0, 0, 1, 0, 4, 1, 0, 5],
    "ほうれん草":[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 5, 0, 0, 0, 0, 0, 4, 0, 0, 1],
    "ホウレンソウ":[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 5, 0, 0, 0, 0, 0, 4, 0, 0, 1],
    "もやし":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "レタス":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "レンコン":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    "ブドウ":[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ぶどう":[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "薄力粉":[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "強力粉":[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "お好み焼":[1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 5, 1, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "ホットケーキ":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "パン":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "うどん":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "そうめん":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "マカロニ":[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "スパゲッティ":[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "パスタ":[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "米":[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "蕎麦":[1, 0, 1, 1, 0, 0, 3, 1, 1, 1, 3, 1, 0, 1, 1, 5, 0, 0, 0, 0, 2, 0, 2, 1, 0, 1, 1, 1, 0],
    "そば":[1, 0, 1, 1, 0, 0, 3, 1, 1, 1, 3, 1, 0, 1, 1, 5, 0, 0, 0, 0, 2, 0, 2, 1, 0, 1, 1, 1, 0],
    "ソバ":[1, 0, 1, 1, 0, 0, 3, 1, 1, 1, 3, 1, 0, 1, 1, 5, 0, 0, 0, 0, 2, 0, 2, 1, 0, 1, 1, 1, 0],
    "牛肩ロース":[1, 5, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
    "サーロイン":[1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0],
    "牛モモ":[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
    "ローストビーフ":[2, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 0, 0, 0, 0],
    "豚肩ロース":[1, 5, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 3, 0, 1, 1, 1, 0, 1, 0, 0],
    "豚ロース":[2, 2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 3, 0, 3, 1, 0, 0, 0, 0, 0],
    "豚バラ":[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 1, 0, 0, 0, 0],
    "豚もも":[2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5, 0, 4, 1, 0, 0, 0, 0, 0],
    "ロースハム":[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 2],
    "生ハム":[2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 2, 0, 0, 1, 0, 0],
    "ベーコン":[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 1],
    "ウィンナー":[1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0],
    "ソーセージ":[1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0],
    "手羽":[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    "鶏むね":[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0, 0, 0, 0, 0],
    "鶏もも":[2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 0, 1, 0, 2, 0, 0],
    "ささ身":[2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 0, 0, 1, 0, 0],
    "クリーム":[0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "チーズ":[2, 2, 0, 0, 0, 4, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 5, 0, 0, 0, 0],
    "アイス":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "えのき":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 1, 1, 1, 0],
    "しいたけ":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    "椎茸":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    "しめじ":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0],
    "エリンギ":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 1, 0, 0],
    "マッシュルーム":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    "えび":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, ],
    "エビ":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, ],
    "海老":[2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, ],
    "イカ":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    "タコ":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
}