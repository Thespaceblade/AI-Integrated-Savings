from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
from datetime import datetime
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='.')
CORS(app)

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Initialize DataFrame with columns
df = pd.DataFrame(columns=[
    'name',
    'purchase_type',
    'rate',
    'price',
    'date',
    'category'
])

@app.route('/')
def serve_index():
    return send_from_directory('.', 'Index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/purchases', methods=['GET', 'POST'])
def handle_purchases():
    global df
    
    if request.method == 'POST':
        data = request.json
        new_row = pd.DataFrame([{
            'name': data['name'],
            'purchase_type': data['purchase_type'],
            'rate': data['rate'],
            'price': float(data['price']),
            'date': data['date'],
            'category': data['category']
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        return jsonify({"message": "Purchase added successfully"})
    
    elif request.method == 'GET':
        purchases = df.to_dict('records')
        return jsonify(purchases)

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    global df
    
    if df.empty:
        return jsonify({
            'total_price': 0,
            'monthly_price': 0,
            'weekly_price': 0,
            'category_totals': {
                'entertainment': 0,
                'health': 0,
                'productivity': 0,
                'other': 0
            }
        })
    
    # Calculate total price based on frequency
    df['annual_price'] = df.apply(lambda row: 
        row['price'] * 52 if row['rate'] == 'weekly' else
        row['price'] * 12 if row['rate'] == 'monthly' else
        row['price'] if row['rate'] == 'yearly' else
        row['price'], axis=1)
    
    total_price = df['annual_price'].sum()
    monthly_price = total_price / 12
    weekly_price = total_price / 52
    
    # Calculate category totals
    category_totals = df.groupby('category')['annual_price'].sum().to_dict()
    
    return jsonify({
        'total_price': round(total_price, 2),
        'monthly_price': round(monthly_price, 2),
        'weekly_price': round(weekly_price, 2),
        'category_totals': category_totals
    })

@app.route('/api/analyze', methods=['GET'])
def analyze_purchases():
    global df
    
    if df.empty:
        return jsonify({"analysis": "No purchase data available for analysis."})
    
    try:
        # Prepare data for analysis
        analysis_data = {
            "total_purchases": len(df),
            "categories": df['category'].value_counts().to_dict(),
            "total_annual_spending": df['annual_price'].sum(),
            "average_purchase": df['price'].mean(),
            "recurring_vs_one_time": df['purchase_type'].value_counts().to_dict()
        }
        
        # Create prompt for Gemini
        prompt = f"""
        Analyze this purchase data and provide insights:
        {analysis_data}
        
        Please provide:
        1. Overall spending patterns
        2. Category distribution analysis
        3. Recommendations for potential savings
        4. Any interesting trends or observations
        
        Keep the response concise and focused on actionable insights.
        """
        
        # Get response from Gemini
        response = model.generate_content(prompt)
        
        return jsonify({
            "analysis": response.text,
            "data": analysis_data
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 