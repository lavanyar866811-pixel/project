import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\ELCOT\Downloads\HR data analysis\data\HR_Analytics.csv")

print(df.head())


dept_count = df['Department'].value_counts()

print("\nDepartment Count:")
print(dept_count)


gender_count = df['Gender'].value_counts()

print("\nGender Count:")
print(gender_count)


attrition = df['Attrition'].value_counts()

print("\nAttrition:")
print(attrition)

dept_count.plot(kind='bar', figsize=(10,5))

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("department_chart.png")

plt.show()


gender_count.plot(kind='pie', autopct='%1.1f%%')

plt.title("Gender Distribution")

plt.ylabel('')

plt.tight_layout()

plt.savefig("gender_chart.png")

plt.show()
