# 💱 Currency Converter API

A FastAPI-based microservice that converts an amount from one currency to another using real-time exchange rates.

---

## 📌 Features

- `GET /convert?from=USD&to=EUR&amount=100`\
  → Returns the converted amount using current exchange rates.

- `GET /supported-currencies`\
  → Lists all supported currencies.

- Optional: Store historical conversions in a database (e.g., PostgreSQL).

---


## 🧠 What It Does

This service fetches real-time exchange rates using an external API (e.g., [ExchangeRate-API](https://www.exchangerate-api.com/)) and performs currency conversions. It's structured as a clean, testable, and containerized Python application.

---

## 💠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) for building REST API
- [Pydantic](https://docs.pydantic.dev/) for settings/config parsing
- [Docker](https://www.docker.com/) & Docker Compose for containerization
- [GitHub Actions](https://github.com/features/actions) for CI
- [Pytest](https://docs.pytest.org/) for unit tests

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```env
EXCHANGE_API_KEY=your_api_key_here
```

---

## 🧪 Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/dipakbadu/currency-converter.git
cd currency-converter
```

2. **Create a virtual environment and activate it:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the server:**

```bash
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for Swagger UI.

---

## 🐳 Run Using Docker

1. **Build the Docker image:**

```bash
docker build --build-arg EXCHANGE_API_KEY=your_api_key_here -t currency-converter .
```

2. **Run the container:**

```bash
docker run -p 8000:8000 -e EXCHANGE_API_KEY=your_api_key_here currency-converter
```

Visit `http://localhost:8000/docs` for API docs.

---

## ✅ Running Tests

Install dev dependencies and run tests:

```bash
pip install -r requirements.txt
pytest
```

---

## ⚙️ CI/CD with GitHub Actions

This project uses GitHub Actions to:

- Install dependencies
- Run tests
- Build Docker image

CI pipeline is defined in `.github/workflows/ci.yml` and runs on every push to `master`.

✅ Latest CI run:&#x20;

---

## 📂 Project Structure

```
currency-converter/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── service/
│   │   └── currency.py
├── Dockerfile
├── requirements.txt
├── .env (not committed)
└── .github/
    └── workflows/
        └── ci.yml
```

