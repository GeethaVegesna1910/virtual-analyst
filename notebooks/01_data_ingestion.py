import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://analyst:analyst_secret@localhost:5432/analytics"
)

orders = pd.read_csv("/Users/raj/Downloads/olist_data/olist_orders_dataset.csv")
customers = pd.read_csv("/Users/raj/Downloads/olist_data/olist_customers_dataset.csv")
products = pd.read_csv("/Users/raj/Downloads/olist_data/olist_products_dataset.csv")
payments = pd.read_csv("/Users/raj/Downloads/olist_data/olist_order_payments_dataset.csv")
sellers = pd.read_csv("/Users/raj/Downloads/olist_data/olist_sellers_dataset.csv")
order_items = pd.read_csv("/Users/raj/Downloads/olist_data/olist_order_items_dataset.csv")

orders.to_sql("orders", engine, if_exists="replace", index=False)
customers.to_sql("customers", engine, if_exists="replace", index=False)
products.to_sql("products", engine, if_exists="replace", index=False)
payments.to_sql("payments", engine, if_exists="replace", index=False)
sellers.to_sql("sellers", engine, if_exists="replace", index=False)
order_items.to_sql("order_items", engine, if_exists="replace", index=False)

print("✅ All tables loaded successfully!")
print(f"Orders: {len(orders)} rows")
print(f"Customers: {len(customers)} rows")
print(f"Products: {len(products)} rows")
print(f"Payments: {len(payments)} rows")
print(f"Sellers: {len(sellers)} rows")
print(f"Order items: {len(order_items)} rows")
