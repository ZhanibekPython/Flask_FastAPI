from flask import Flask, render_template


shop = Flask(__name__)

@shop.route('/main/')
@shop.route('/')
def main_page():
    return render_template('shop.html')

@shop.route('/clothes')
@shop.route('/category/clothes')
def clothes():
    return render_template('clothes.html')

@shop.route('/shoes')
@shop.route('/category/shoes')
def shoes():
    return render_template('shoes.html')

@shop.route('/jackets')
@shop.route('/category/jackets')
def jackets():
    return render_template('jackets.html')

if __name__ == '__main__':
    shop.run()