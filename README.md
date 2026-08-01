# 🚀 AI Career Copilot

An AI-powered career assistant that helps users explore career paths, generate personalized roadmaps, and receive intelligent guidance using the **Groq API**. The application provides an interactive and user-friendly interface to assist students and professionals in planning their careers efficiently.

---

## 📌 Features

* 🤖 AI-powered career guidance
* 🎯 Personalized career recommendations
* 🛣️ Step-by-step learning roadmap generation
* 💬 Interactive chatbot interface
* ⚡ Fast responses using the Groq LLM API
* 🎨 Clean and responsive web interface
* 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### AI

* Groq API
* Large Language Model (LLM)

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* SQLite

---

## 📂 Project Structure

```text
AI_CAREER_COPILOT/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── requirements.txt
├── .env                 # Not included in Git
├── .gitignore
├── static/
├── templates/
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mdsaquibcodin/AI_career_copilot.git
```

### 2. Move into the project directory

```bash
cd AI_career_copilot
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows**

```bash
env\Scripts\activate
```

**Linux / macOS**

```bash
source env/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

> **Note:** Never commit your `.env` file to GitHub.

### 7. Run the application

```bash
python app.py
```


## 🔒 Security

This project uses environment variables to securely store API keys.

The `.env` file is excluded from version control through `.gitignore`, ensuring that sensitive credentials are never exposed.

---

## 📈 Future Improvements

* Resume Analyzer
* Job Recommendation System
* Interview Preparation Module
* Skill Gap Analysis
* Resume Builder
* Learning Resource Recommendations
* Authentication System
* Deployment on Render or Vercel

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Mohd Saquib**

* GitHub: https://github.com/mdsaquibcodin

---

⭐ If you found this project useful, please consider giving it a **Star** on GitHub!
