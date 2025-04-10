# AI Integrated Savings

This project is a demo frontend for a savings tool built to help users reduce unnecessary expenses and learn more about AI-driven financial insights. It was originally designed as part of a hackathon and continues to be improved as a standalone project. The site contains multiple informational pages that help users learn how AI can be used to evaluate subscriptions, track spending, and recommend savings strategies.

The goal was to build a professional, multi-page site that shares a unified brand across all pages using a shared navigation bar and consistent design system. This project showcases skills in frontend development (HTML, CSS, JS) and basic Flask backend setup.

---

## 🌐 Live Demo

Explore the project live on GitHub Pages:  
🔗 [https://thespaceblade.github.io/AI-Integrated-Savings/](https://thespaceblade.github.io/AI-Integrated-Savings/)

---

## 📄 Available Pages

- [Home](https://thespaceblade.github.io/AI-Integrated-Savings/index.html)
- [About Us](https://thespaceblade.github.io/AI-Integrated-Savings/About-Us.html)
- [Expense Safety](https://thespaceblade.github.io/AI-Integrated-Savings/Expense-Safety.html)
- [Subscription Safety](https://thespaceblade.github.io/AI-Integrated-Savings/Subscription-Safety.html)

Each page features a consistent layout and branding system via the shared navigation bar.

---

## 🗂️ Project Structure

```
AI-Integrated-Savings/
├── .vscode/
├── Images/
├── styles/
├── .gitignore
├── About-Us.html
├── About-Us.css
├── Expense-Safety.html
├── Expense-Safety.css
├── Homepage_s.css
├── README.md
├── Subscription-Safety.html
├── Subscription-Safety.css
├── app.py
├── file_structure.txt
├── frontend.js
├── index.html
├── index_s.css
├── navbar.html
└── requirements.txt
```

---

## 🛠️ Technologies Used

- **HTML5 & CSS3** – Core structure and responsive design
- **JavaScript** – Interactive behaviors and dynamic page elements
- **Python (Flask)** – Simple local server simulation (`app.py`)
- **VS Code** – Development environment

---

## ⚙️ How to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Thespaceblade/AI-Integrated-Savings.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd AI-Integrated-Savings
   ```

3. **(Optional) Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App**:
   ```bash
   python app.py
   ```

6. **Visit in Browser**:
   Open `http://localhost:5000` to view the homepage and explore the rest of the site.

---

## 🐞 Known Issues & Future Improvements

- [ ] **Fix page routing on GitHub Pages** — navigation bar may not work as expected due to relative paths
- [ ] **Unify CSS files** — consolidate repeated styles into a shared stylesheet
- [ ] **Enhance mobile responsiveness** — some layouts break on smaller screens
- [ ] **Refactor `navbar.html`** — ensure better modular reuse and avoid duplication
- [ ] **Add form elements** — build interactive input features (e.g., savings estimators)
- [ ] **Add accessibility features** — improve contrast, alt tags, and ARIA roles
- [ ] **Optimize image sizes** — compress images for faster load times
- [ ] **Deploy Flask backend online** — transition from static demo to full-stack app

---

## 🤝 Contributions

Feel free to fork the repo and submit pull requests with ideas, improvements, or new features.

---

## ❗ Notes

- This repo no longer references any branded content or partnerships from previous versions.
- Future plans include converting this into a full-stack project with backend integration for real-time financial recommendations.
