import requests
from datetime import datetime

def create_sale(api_url, sale_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=sale_data, headers=headers)

    if response.status_code == 201:
        print("Sale created successfully!")
        return response.json()
    else:
        print(f"Failed to create sale. Status code: {response.status_code}, message: {response.text}")

# Usage
if __name__ == "__main__":
    api_url = "http://127.0.0.1:5000/api/sales"  # Update if your Flask app is running on a different port or host
    sale_data = {
        "customerName": "Jane Doe",
        "product": "Massage Chair Model X",
        "quantity": 1,
        "price": 3000,
        "contactInfo": "jane.doe@example.com",
        "date": datetime.utcnow().isoformat()
    }

    # Call the function to make a sale
    result = create_sale(api_url, sale_data)
    print(result)