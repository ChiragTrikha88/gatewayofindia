
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cart', methods=['POST'])
def cart():
    items = request.form.getlist('items')
    prices = {'Basmati Rice': 5.00, 'Maggi Noodles': 1.50, 'Amul Butter': 3.00}
    total = sum(prices.get(item, 0) for item in items)
    return render_template('cart.html', cart_items=items, total=total)

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/events')
def events():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
