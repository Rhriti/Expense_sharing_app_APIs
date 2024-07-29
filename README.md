# Expense Sharing App

This API allow users to add expenses and split bills according to different methods: equally, by exact amounts, or by percentage. It uses Flask for the creating APIs and MongoDB for data storage.

## Features

- Add expenses
- Split bills equally, by exact amounts, or by percentage
- Retrieve user-specific expenses
- Download balance sheet as a CSV file

## Requirements

- Python 3.7 or higher
- Flask
- MongoDB
- pymongo
- Flask-PyMongo

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/expense-sharing-app.git
cd expense-sharing-app
```

### 2. Set Up a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

Make sure you have MongoDB installed and running on your local machine. By default, the app expects MongoDB to be running on `localhost:27017`. If your MongoDB server is running on a different host or port, update the MongoDB URI in the `config.py` file.

### 5. Run the Application

Start the Flask application:

```bash
flask run
```
OR
```bash
python app.py
```

The app should now be running on `http://127.0.0.1:5000`.

## API Endpoints

### Add Expense

- **URL**: `/api/expenses`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "amount": 3000,
        "payer": "user1",
        "participants": ["user1", "user2", "user3"],
        "split_type": "EQUAL",
        "splits":[]
    }
    ```
- **Response**:
    ```json
    {
        "message": "Expense added successfully",
        "id": "60d21baee37c9f3f64ff4c4a"
    }
    ```

### Get User Expenses

- **URL**: `/api/expenses/<user_name> [will rectify this for email]
- **Method**: `GET`
- **Response**:
    ```json
    [
        {
            "_id": "60d21baee37c9f3f64ff4c4a",
            "amount": 3000,
            "payer": "user1",
            "participants": ["user1", "user2", "user3"],
            "split_type": "EQUAL"
        }
    ]
    ```

### Get Balance Sheet

- **URL**: `/api/balance_sheet`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "user2": -1000,
        "user3": -1000,
        "user1": 2000
    }
    ```

### Download Balance Sheet

- **URL**: `/api/balance-sheet_download`
- **Method**: `GET`
- **Response**: A CSV file with the balance sheet information.

## Example Scenarios

### 1. Equal Split

Scenario: You go out with 3 friends. The total bill is 3000. Each friend owes 1000.

#### POST Request to create a user

```python
import requests

# Base URL of your Flask app
base_url = 'http://127.0.0.1:5000'

# Example GET request
def test_get_request():
    response = requests.get(f'{base_url}/api/users/hritijrana07@gmail.com')
    print(f"GET Response Status: {response.status_code}")
    print(f"GET Response Content: {response.json()}")

# Example POST request
def test_post_request():
    data = {
        'email': 'hritijrana07@gmail.com',
        'name': 'Hritij',
        'mobile_number': '9122346494'
    }
    response = requests.post(f'{base_url}/api/users', json=data)
    print(f"POST Response Status: {response.status_code}")
    print(f"POST Response Content: {response.json()}")

# Run the tests

if __name__ == '__main__':
    test_post_request()
    test_get_request()
```

### POST request to add expense 
```python
# Define the expense data for equal split
expense_data_equal = {
    "amount": 4000,
    "payer": "Hritij",
    "participants": ["Ayank", "raw", "ks", "jake"],
    "split_type": "EQUAL",
    
}

# Send a POST request to add the expense
response = requests.post('http://localhost:5000/api/expenses', json=expense_data_equal)

# Print the response
print(response.json())
```

#### API Request

```python
import requests

url = "http://127.0.0.1:5000/api/expenses"
data = {
    "amount": 4299,
    "description": "Shopping",
    "payer": "user1",
    "participants": ["user1", "user2", "user3"],
    "split_type": "EXACT",
    "splits": [1500, 799, 2000]
}

response = requests.post(url, json=data)
print(response.json())
```

### GET expense 

```python
response = requests.get('http://localhost:5000/api/expenses/Hritij')

# Print the response
print(response.json())
```

#### GET balance_sheet

```python
response = requests.get('http://localhost:5000/api/balance_sheet',params={'payer':'Hritij'})

# Print the response
print(response.json())

```
### GET balance sheet csv
```python
response = requests.get('http://localhost:5000/api/balance_sheet_download')

# Print the response
with open('bb.csv', 'w') as f:
    f.write(response.content.decode('utf-8'))
```

### POST and GET bill in exact distribution
```python
expense_data_equal = {
    "amount": 4000,
    "payer": "Karans",
    "participants": ["Arjun", "Binod", "Ayank", "Raw"],
    "split_type": "EXACT",
    'splits':[2000,1000,1000,0]    
}

# Send a POST request to add the expense
response = requests.post('http://localhost:5000/api/expenses', json=expense_data_equal)

# Print the response
print(response.json())
response = requests.get('http://localhost:5000/api/balance_sheet',params={'payer':'Karans'})

# Print the response
print(response.json())
```


## Additional Informatin

- Make sure MongoDB is running before starting the Flask application.
- Ensure all required dependencies are installed.

## License

This project is licensed under the MIT License.
