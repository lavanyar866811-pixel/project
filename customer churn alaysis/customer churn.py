import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\ELCOT\Downloads\customer churn alaysis\data\dataset.csv")


print(df.head())

churn_count = df['Churn'].value_counts()

print("\nChurn Count:")
print(churn_count)

gender_churn = df.groupby('gender')['Churn'].value_counts()

print("\nGender-wise Churn:")
print(gender_churn)


contract_churn = df.groupby('Contract')['Churn'].value_counts()

print("\nContract-wise Churn:")
print(contract_churn)


churn_count.plot(kind='bar', figsize=(6,5))

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("churn_distribution.png")

plt.show()


contract_count = df['Contract'].value_counts()

contract_count.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))

plt.title("Contract Type Distribution")

plt.ylabel('')

plt.tight_layout()

plt.savefig("contract_distribution.png")

plt.show()
