import sqlite3
import pandas as pd 


def read_order():
    conn = sqlite3.connect('dags/desafioAirflow/data/Northwind_small.sqlite')
    df = pd.read_sql_query('SELECT * FROM "order";',conn)
    df.to_csv('dags/desafioAirflow/data/output_orders.csv')
    conn.close()
    return  

def  read_orderDetail():
    conn = sqlite3.connect('dags/desafioAirflow/data/Northwind_small.sqlite')
    df_orderDetail = pd.read_sql_query('SELECT * FROM orderDetail;',conn)
    df_order = pd.read_csv('dags/desafioAirflow/data/output_orders.csv')
    df = df_order.merge(df_orderDetail, left_on='Id',right_on='OrderId')
    resultado = df[df['ShipCity']=='Rio de Janeiro']['Quantity'].sum()
    with open('dags/desafioAirflow/data/count.txt', 'w') as f:
        f.write(str(resultado))
    conn.close()
    return 



    
    
