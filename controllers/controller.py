from flask import render_template
from app import app
from models.orders import orders

@app.route('/orders')
def index():
    return render_template("index.html", title= "Home", orders=orders)

@app.route('/orders/<index>')
def order_view(index):
        order_to_view = orders[int(index) - 1]
        return render_template("order.html", title= "View Order", order=order_to_view)