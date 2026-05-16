import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\ELCOT\Downloads\sales data analysis\data\Sales_Data.csv", encoding='latin1')


print(df.head())


total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)


product_sales = df.groupby('Product')['Sales'].sum()

print("\nSales by Product Line:")
print(product_sales)

product_sales.plot(kind='bar', figsize=(12,6))

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("product_sales.png")

plt.show()

top_products = product_sales.sort_values(ascending=False).head(5)

print(top_products)

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line')

plt.show()

city_sales = df.groupby('City')['Sales'].sum()

city_sales.plot(kind='bar')

plt.show()

