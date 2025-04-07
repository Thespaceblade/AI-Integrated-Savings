# Capital One Subscription Tracker 💳📊

A responsive front-end web tool built using **HTML**, **CSS**, and **JavaScript**, designed to help users easily track and visualize their **subscription** and **recurring expenses**. Created as part of a **Capital One Case Competition**, this project delivers a clean user interface and intuitive interaction for managing financial subscriptions and analyzing monthly costs.

## 🔍 Features

- Input interface for entering subscription names, prices, and frequencies
- Calculates and displays total recurring costs
- Modular navigation with separate HTML views (e.g. homepage, about us)
- Responsive design and styling using custom CSS
- Favicon and branding elements included

## 🛠️ Technologies Used

- HTML5
- CSS3
- JavaScript (client-side only)
- GitHub Pages for deployment

## 🚀 Live Site

You can access the live deployed version here:  
[https://thespaceblade.github.io/Capital-One-CC/](https://thespaceblade.github.io/Capital-One-CC/)

## 🧠 About the Project

This project was developed as a prototype solution for the **Capital One Case Competition**, where our team was challenged to present a tool that empowers users to understand and manage their digital financial commitments more clearly.

We focused on creating a visually clean and data-focused interface that could eventually be scaled to include real-time sync with banking APIs and machine learning predictions on future spending.

## 👥 Contributors

- Jason Charwin – Frontend Design, Project Lead
- Akshita, Chelsea, Haley, Josh, Nicolette – Team Members & UX Advisors

## 📁 Folder Structure

```
Capital-One-CC/
├── index.html
├── About-Us.html
├── Expense Safety.html
├── Subscription Safety.css
├── Homepage_s.css
├── navbar.html
├── Images/
│   └── [Team and branding assets]
```

## 🧩 Future Improvements

- Add backend support for saving user data
- Enable data visualization with charts
- Integrate OAuth and secure account syncing
- Mobile-friendly version with swipe UX

## 📄 License

This project is for educational and demonstration purposes. No commercial use is intended unless otherwise stated.

# SubCheckr - Purchase Tracker

A web application for tracking purchases and subscriptions with a Flask backend and Pandas DataFrame integration.

## Features

- Track one-time and recurring purchases
- View total, monthly, and weekly expenses
- Categorize purchases
- Visualize spending by category
- Demo mode for testing

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start the Flask server:
```bash
python app.py
```

3. Open `Index.html` in your web browser

## Architecture

- Frontend: HTML, CSS, JavaScript
- Backend: Flask with Pandas DataFrame
- Data Storage: In-memory DataFrame (resets on server restart)

## API Endpoints

- `GET /api/purchases`: Get all purchases
- `POST /api/purchases`: Add a new purchase
- `GET /api/statistics`: Get spending statistics

## Data Structure

Each purchase contains:
- name: Purchase name
- purchase_type: "oneTime" or "recurring"
- rate: "weekly", "monthly", "yearly", or "oneTime"
- price: Amount in dollars
- date: Purchase date
- category: "entertainment", "health", "productivity", or "other"