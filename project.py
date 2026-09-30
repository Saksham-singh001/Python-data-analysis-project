import pandas as pd

df = pd.read_excel("Data.xlsx")
print(df.head())
print(df.shape)
print(df.columns)
print(df["Sales"].head())
print(df["profit"].head())


print(df["Sales"].sum())
print(df["Sales"].mean())

print(df["profit"].sum())
print(df["profit"].mean())

#REGION WISE TOTAL
region = df.groupby("Region")[["Sales","profit"]].sum()
print(region)
# REGION WISE AVERAGE
region_avg = df.groupby("Region")[["Sales","profit"]].mean()
print(region_avg)

import matplotlib.pyplot as plt
print("Matplotlib OK")


region["Sales"].plot(kind="bar")
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()


region["Sales"].plot(kind="line")
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()


region["Sales"].plot(kind="pie",autopct="%1.1f%%")
plt.title("Region-wise Sales Share")
plt.ylabel("")
plt.show()


df["Sales"].plot(kind="hist",bins=10)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()


province = df.groupby("Province")[["Sales","profit"]].sum()
print(province)


province_avg = df.groupby("Province")[["Sales","profit"]].mean()
print(province_avg)

category = df.groupby("Product Category")[["Sales","profit"]].sum()
print(category)


category_avg = df.groupby("Product Category")[["Sales","profit"]].mean()
print(category_avg)


category["Sales"].plot(kind="bar")
plt.title("Category-wise Sales")
plt.xlabel("Product Category")
plt.ylabel(("Sales"))
plt.show()


category["Sales"].plot(kind="line")
plt.title("Category-wise Sales")
plt.xlabel("Product Category")
plt.ylabel(("Sales"))
plt.show()


category["Sales"].plot(kind="pie",autopct="%1.1f%%")
plt.title("Category-wise Sales Share")
plt.ylabel((""))
plt.show()


df["Sales"].plot(kind="hist",bins=10)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel(("Frequency"))
plt.show()



ship_category = pd.crosstab(df["Product Category"],df["Ship Mode"])
print(ship_category)


ship_category.plot(kind="bar",stacked=True)
plt.title("Ship Mode By Product Category")
plt.xlabel("Product Category")
plt.ylabel("Number Of Orders")
plt.legend(title="Ship Mode")
plt.show()