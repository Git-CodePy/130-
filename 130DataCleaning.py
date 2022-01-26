import pandas as pd 
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)

x = float("nan")

i = pd.read_csv("total_stars.csv")
new_i = [x for x in i if pd.isnull(x) == False]

del df["luminosity"]
del df["Unnamed: 6"]
del df["Unnamed: 0"]

print(list(df))

d1 = []
d2 = []

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

p_d = []

p_d = []

for i in p_d1:
    p_d.append(i)

for j in p_d2:
    p_d.append(j)

with open("total_stars_1.csv",'w',encoding = 'utf8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerow(p_d)
