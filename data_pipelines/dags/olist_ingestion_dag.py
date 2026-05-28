from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine

default_args = {
    'owner': 'geetha',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def ingest_orders():
    engine = create_engine("postgresql://analyst:analyst_secret@postgres:5432/analytics")
    df = pd.read_csv("/opt/airflow/data/olist_orders_dataset.csv")
    df.to_sql("orders", engine, if_exists="replace", index=False)
    print(f"✅ Orders loaded: {len(df)} rows")

def ingest_payments():
    engine = create_engine("postgresql://analyst:analyst_secret@postgres:5432/analytics")
    df = pd.read_csv("/opt/airflow/data/olist_order_payments_dataset.csv")
    df.to_sql("payments", engine, if_exists="replace", index=False)
    print(f"✅ Payments loaded: {len(df)} rows")

def ingest_customers():
    engine = create_engine("postgresql://analyst:analyst_secret@postgres:5432/analytics")
    df = pd.read_csv("/opt/airflow/data/olist_customers_dataset.csv")
    df.to_sql("customers", engine, if_exists="replace", index=False)
    print(f"✅ Customers loaded: {len(df)} rows")

def data_quality_check():
    engine = create_engine("postgresql://analyst:analyst_secret@postgres:5432/analytics")
    orders = pd.read_sql("SELECT COUNT(*) as cnt FROM orders", engine)
    payments = pd.read_sql("SELECT COUNT(*) as cnt FROM payments", engine)
    customers = pd.read_sql("SELECT COUNT(*) as cnt FROM customers", engine)
    print(f"✅ Quality check passed!")
    print(f"   Orders: {orders['cnt'][0]}")
    print(f"   Payments: {payments['cnt'][0]}")
    print(f"   Customers: {customers['cnt'][0]}")

with DAG(
    'olist_daily_ingestion',
    default_args=default_args,
    description='Daily ingestion of Olist ecommerce data',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['module1', 'ingestion'],
) as dag:

    t1 = PythonOperator(task_id='ingest_orders', python_callable=ingest_orders)
    t2 = PythonOperator(task_id='ingest_payments', python_callable=ingest_payments)
    t3 = PythonOperator(task_id='ingest_customers', python_callable=ingest_customers)
    t4 = PythonOperator(task_id='data_quality_check', python_callable=data_quality_check)

    t1 >> t2 >> t3 >> t4
