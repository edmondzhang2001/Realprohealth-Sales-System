import os
from flask import Flask, send_from_directory, request, jsonify, abort
from flask_cors import CORS
#from extensions import db
from flask_sqlalchemy import SQLAlchemy
from models import Sales
import logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:54qmfmh8@localhost/Realprohealth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize logging
logging.basicConfig(level=logging.INFO)

db.init_app(app)

@app.route('/api/sales', methods=['GET', 'POST'])
def manage_sales():
    app.logger.info(f"Incoming request data: {request.data}")
    try:
        if request.method == 'GET':
            # Retrieve and return sales records
            print("hello")
            sales = Sales.query.all()
            return jsonify([{'id': sale.id, 'customerName': sale.customerName, 'product': sale.product, 'quantity': sale.quantity, 'price': sale.price, 'contactInfo': sale.contactInfo} for sale in sales])
        elif request.method == 'POST':
            # Add a new sale record
            data = request.get_json()
            if not data:
                return jsonify({"message": "No input data provided"}), 400
            try:
                # Here you might validate data and check if all fields exist
                new_sale = Sales(
                    customerName=data['customerName'],
                    product=data['product'],
                    quantity=data['quantity'],
                    price=data['price'],
                    contactInfo=data['contactInfo']
                )
                db.session.add(new_sale)
                db.session.commit()
                return jsonify({"message": "New sale record created"}), 201
            except KeyError as e:
                # If a field is missing in the data
                return jsonify({"message": f"Missing field: {e.args[0]}"}), 400
            except Exception as e:
                # For any other exceptions
                db.session.rollback()
                return jsonify({"message": "An error occurred while creating the record"}), 500
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")


def serve():
    return send_from_directory(app.static_folder, 'index.html')

with app.app_context():  # This line provides an application context
    # Attempt to connect to the database and log the outcome
    try:
        # Use a context manager to acquire a connection
        with db.engine.connect() as connection:
            # Connection succeeded
            app.logger.info("Database connection successful")
    except Exception as e:
        # Connection failed
        app.logger.error("Database connection failed: %s", e)
    
    # This would also be a good place to create tables if they don't exist
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    
import requests

def create_sale(api_url, sale_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=sale_data, headers=headers)
    
    if response.status_code == 201:
        print("Sale created successfully!")
        return response.json()
    else:
        print(f"Failed to create sale. Status code: {response.status_code}, message: {response.text}")

if __name__ == "__main__":
    # The API endpoint URL
    api_url = "http://127.0.0.1:5000/api/sales"