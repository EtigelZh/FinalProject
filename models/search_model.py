import pandas
def getproduct(conn, id):
    return pandas.read_sql(f'''
    SELECT * from product where ID_product = {id}
 ''', conn)