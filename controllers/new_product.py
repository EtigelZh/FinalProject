from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.new_product_model import get_type, get_box_product, get_city_product, get_cost_product, create_product, get_price_product

@app.route('/new_product', methods=['GET', 'POST'])
def new_product():
    conn = get_db_connection()
    type_product = get_type(conn)
    ID_type = 0
    city = ''
    box = ''
    price = 0
    type_p = 'usual'
    ID_cost = 0
    name = 'письмо'
    weight = 0
    volume = 0
    session['city_id'] = request.form.get('cities')
    session['box_id']= request.form.get('box')
    city = get_city_product(conn, session['city_id'])
    box = get_box_product(conn, session['box_id'])
    price = get_price_product(conn, session['box_id'], session['city_id'])
    if request.values.get('name_product') and request.values.get('weight') and request.values.get('volume'):
        session['city_id'] = request.form.get('cities')
        session['box_id']= request.form.get('box')
        city = get_city_product(conn, session['city_id'])
        box = get_box_product(conn, session['box_id'])
        price = get_price_product(conn, session['box_id'], session['city_id'])
        type_p = request.values.get('type_p')
        ID_costt = get_cost_product(conn, session['box_id'], session['city_id'])
        ID_cost = ID_costt['ID_cost_calculation'][0]
        name = request.values.get('name_product')
        weight = request.values.get('weight_product')
        volume = request.values.get('volume_product')
        if (type_p == "usual"):
            ID_type = 1
        elif(type_p == "fragile"):
            ID_type = 2
        elif(type_p == "danger"):
            ID_type = 3
        create_product(conn, ID_cost, ID_type, name, weight, volume)
        


    html = render_template(
        'new_product.html',
        len=len,
        city = city,
        box = box,
        type_product = type_product,
        price = price
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)