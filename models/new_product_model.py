import pandas

def get_price_product(conn, box, city):
    return pandas.read_sql(f'''
    SELECT price_product
    FROM cost_calculation
    WHERE ID_box = {box} AND ID_distance = {city}
 ''', conn)
def get_cost_product(conn, box, city):
    return pandas.read_sql(f'''
    SELECT ID_cost_calculation
    FROM cost_calculation
    WHERE ID_box = {box} AND ID_distance = {city}
 ''', conn)
def get_type(conn):
    return pandas.read_sql('''
    SELECT name FROM type_product
''', conn)
def get_city_product(conn, id):
    return pandas.read_sql(f'''
    SELECT city from distance_cities where ID_distance = {id}
 ''', conn)

def get_box_product(conn, id):
    return pandas.read_sql(f'''
    SELECT box_name from box WHERE ID_box = {id}
 ''', conn)
def create_product(conn, ID_cost, ID_type, name, weight, volume):
    cur = conn.cursor()
    cur.execute(
        '''
            INSERT INTO product (ID_cost_calculation, ID_type_product, name, weight, volume)
            VALUES (:ID_cost, :ID_type, :name, :weight, :volume)
        ''',
        {"ID_cost": ID_cost, "ID_type": ID_type, "name": name, "weight": weight, "volume": volume}
    )
    conn.commit()
    return cur.lastrowid