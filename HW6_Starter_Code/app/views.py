from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
from .models import * # Access the models file to use SQL functions

@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = form.first_name.data
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        phone = form.phone.data
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        insert_customer(first_name, last_name, company, email, phone)
        insert_address(street_address, city, state, country, zip_code)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html', customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    orderForm = OrderForm()
    customer_id = value
    if orderForm.validate_on_submit():
        name_of_part = orderForm.name_of_part.data
        manufacturer_of_part = orderForm.manufacturer_of_part.data
        insert_order(name_of_part, manufacturer_of_part, customer_id)
        return redirect('/customers')
    return render_template('order.html', form=orderForm)
