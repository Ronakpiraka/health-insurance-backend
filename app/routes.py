# app/routes.py
from flask import request, jsonify
from app import app, mongo
from app.premium_calculator import calculate_premium
from app.config import MONGO_URI  # Update import path

@app.route('/calculate_premium', methods=['POST'])
def calculate_premium_route():
    data = request.json  # Expecting age, sum_insured, city_tier, and tenure
    premium = calculate_premium(data)  # Implement this function
    return jsonify({"premium": premium})

# Add other routes for getting sum insured, city tier, and tenure options
