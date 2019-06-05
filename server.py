from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    id_from_form = request.form['student_id']
    strawberry_from_form = request.form['strawberry']
    raspberry_from_form = request.form['raspberry']
    apple_from_form = request.form['apple']
    blackberry_from_form = request.form['blackberry']
    sum_of_fruits = int(request.form['strawberry']) + int(request.form['blackberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    ugly_today_date = datetime.now()
    today_date = ugly_today_date.strftime("%d %b, %Y at %I:%M %p")
    return render_template("checkout.html", first_name_from_template = first_name_from_form,
    last_name_from_template = last_name_from_form, id_from_template = id_from_form,
    strawberry_from_template = strawberry_from_form, raspberry_from_template=raspberry_from_form,
    apple_from_template = apple_from_form, blackberry_from_template = blackberry_from_form,
    sum_of_fruits = sum_of_fruits, today_date = today_date)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
