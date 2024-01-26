from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import get_cities, get_box, watch_product, get_price_product, get_city_product, get_box_product, create_product, get_cost_product


@app.route('/', methods=['get', 'post'])
def index():
    conn = get_db_connection()
    df_cities = get_cities(conn)
    df_box = get_box(conn)
    df_product = watch_product(conn)
    price = 0
    city = ''
    box = ''
    city_id = request.values.get('cities')
    box_id= request.values.get('box')
    session['box_id'] = box_id
    name = ''
    ID_cost = 0
    type_p = 0



    if request.values.get('name_product') and request.values.get('cities') and request.values.get('box'):
        name = request.values.get('name_product')
        weight = request.values.get('weight_product')
        volume = request.values.get('volume_product')
        ID_costt = get_cost_product(conn, box_id, city_id)
        ID_cost = ID_costt['ID_cost_calculation'][0]
        type_p = request.values.get('type_p')
        if (type_p == "usual"):
            ID_type = 1
        elif(type_p == "fragile"):
            ID_type = 2
        elif(type_p == "danger"):
            ID_type = 3
        #create_product(conn, ID_cost, ID_type, name, weight, volume)
        print('id')
        print(ID_cost)


    if request.values.get('cities') and request.values.get('box'):
        pricee = get_price_product(conn, city_id, box_id)
        price = pricee['price_product'][0]
        cityy = get_city_product(conn, city_id)
        city = cityy['city'][0]
        boxx = get_box_product(conn, box_id)
        box = boxx['box_name'][0]

    html = render_template(
        'index.html',
        com_cities = df_cities,
        com_box = df_box,
        com_product = df_product,
        city_id = city_id,
        price = price,
        city = city,
        box = box,
        len=len
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)