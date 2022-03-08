# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df,'\n', df.shape[0] )


# print(df['calories'],'\n')

# print(df.loc["day2"],'\n')
# print(df.iloc[1],'\n')

# print(df.loc[:,'duration'],'\n')

# print(df.loc["day2",'calories'],'\n')
# print(df.iloc[1,0],'\n')

mystr ='hello its me i was wondering'
index=mystr.find('}')

mystr= mystr[:index+1]
print(mystr)