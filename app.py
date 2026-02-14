from flask import Flask, render_template, request, redirect, url_for
from models import db, Car
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arab_cars.db'
app.config['UPLOAD_FOLDER'] = 'static/'
db.init_app(app)

@app.route('/')
def index():
    search_query = request.args.get('search')
    if search_query:
        cars = Car.query.filter((Car.brand.contains(search_query)) | (Car.model.contains(search_query))).all()
    else:
        cars = Car.query.all()
    return render_template('index.html', cars=cars)

@app.route('/car/<int:car_id>')
def details(car_id):
    car = Car.query.get_or_404(car_id)
    return render_template('details.html', car=car)

@app.route('/admin_secret_99')
def admin_page():
    return render_template('add_car.html')

@app.route('/add_action', methods=['POST'])
def add_car_action():
    brand = request.form['brand']
    model = request.form['model']
    price = float(request.form['price'])
    file = request.files['image_file']
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_car = Car(brand=brand, model=model, price=price, image_url=filename)
        db.session.add(new_car)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # هنا التعديل عشان يشتغل على أي سيرفر أو موبايل
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)