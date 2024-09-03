# Food Truck API

This Django-based API helps users discover nearby food trucks in San Francisco based on their location. It uses Django's GIS features to perform accurate geospatial queries.

## Features

- **Location-Based Search**: Find the nearest food trucks by specifying latitude and longitude.
- **Geospatial Queries**: Utilizes PostgreSQL with PostGIS for accurate distance calculations.
- **REST API**: Built with Django REST Framework.

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework
- PostgreSQL 12+
- PostGIS extension

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/food-truck-api.git
cd food-truck-api

```
### 3. Set Up a Virtual Environment
Copy code
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Install PostgreSQL and PostGIS and create DB
brew install postgresql
brew install postgis

psql -c "CREATE DATABASE food_truck_db;"
psql -d food_truck_db -c "CREATE EXTENSION postgis;"


### 5. Apply Migrations 
python manage.py migrate


### 6. Load Food Truck Data
python manage.py load_food_truck_data

### 7. Run The development server
python manage.py runserver


API Endpoint
Get Nearby Food Trucks
Endpoint: /api/nearby-food-trucks/
Method: GET

Parameters:

latitude: The latitude of your current location.
longitude: The longitude of your current location.