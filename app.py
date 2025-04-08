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
    
    # Ensure 'annual_price' column exists
    if 'annual_price' not in df.columns:
        df['annual_price'] = df.apply(lambda row: 
            row['price'] * 52 if row['rate'] == 'weekly' else
            row['price'] * 12 if row['rate'] == 'monthly' else
            row['price'] if row['rate'] == 'yearly' else
            row['price'], axis=1)
    
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
        You are a personal finance advisor. Review this user's spending data:

        {analysis_data}

        Please analyze this and provide:
        1. Patterns in how they spend (e.g., what categories dominate, how recurring vs one-time costs compare)
        2. Any unnecessary or high-frequency purchases
        3. Budgeting advice — how could they reduce costs while maintaining lifestyle?
        4. Red flags or risks (e.g., too much in entertainment or subscriptions)
        5. One-sentence takeaway they should remember this month

        Be clear and conversational, not robotic.
        """
        
        # Get response from Gemini
        response = model.generate_content(prompt)
        
        # Structure response for frontend
        sections = response.text.split('\n\n')
        structured_response = {
            "summary": sections[0] if len(sections) > 0 else "",
            "advice": [section.strip() for section in sections[1:] if section.strip()],
            "raw_text": response.text
        }

        return jsonify({
            "analysis": structured_response,
            "data": analysis_data
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)