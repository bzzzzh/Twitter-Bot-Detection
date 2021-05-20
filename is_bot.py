import numpy as np
import pandas as pd

user = pd.read_json("result.json")
varify = pd.read_csv("twitter_human_bots_dataset.csv", sep=',')

user.insert(0, "is_bot", 1)
count = 0

for i in user.index:
    for j in varify.index:
        if user["id"][i] == varify["id"][j]:
            if varify["account_type"][j] == "human":
                user["is_bot"][i] = 0
            else:
                user["is_bot"][i] = 1
    print("count:",count)
    count = count + 1

user.to_csv('step1.csv')
print("finish writing to file")
