from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.search_model import getproduct


@app.route('/search', methods=['get', 'post'])
def search():
    conn = get_db_connection()
    product = ''
    if request.values.get('search'):
        id_search = int(request.values.get('search'))
        productt = getproduct(conn, id_search)
        product = productt['name'][0]
    html = render_template(
        'search.html',
        len=len,
        product = product
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)