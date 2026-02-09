# 🏦 Django Bank API

Welcome to the **Django Bank API**! This is a robust banking system backend built with Django and Django Rest Framework (DRF). It provides secure and scalable endpoints for managing user accounts, transactions, and financial analytics. 🚀

---

## 🌟 Features

### 🔐 Authentication & Security
- **JWT Authentication**: Secure login and registration using `SimpleJWT`.
- **Token Refresh**: Seamless session management with refresh tokens.
- **User Registration**: Easy sign-up process for new users.

### 💰 Banking Operations
- **Account Management**: View account details and balance.
- **Deposits**: Add funds to your account instantly. 💸
- **Withdrawals**: Securely withdraw funds with balance checks. 🏧
- **Transfers**: Transfer money to other users within the system. 🔄

### 📊 Analytics & History
- **Transaction History**: Detailed log of all deposits, withdrawals, and transfers. 📜
- **Spending Summary**: Get insights into your spending habits with categorized summaries. 📈

### 📚 Documentation
- **Swagger UI**: Interactive API documentation for easy testing and integration.
- **ReDoc**: Clean and organized API reference.

---

## 🛠️ Tech Stack

- **Backend Framework**: [Django](https://www.djangoproject.com/) 🐍
- **API Framework**: [Django Rest Framework (DRF)](https://www.django-rest-framework.org/) 🌐
- **Authentication**: [SimpleJWT](https://github.com/jazzband/djangorestframework-simplejwt) 🔑
- **Database**: PostgreSQL (via `psycopg2-binary`) 🗄️
- **Documentation**: [drf-spectacular](https://drf-spectacular.readthedocs.io/) 📖
- **Utilities**: `django-filter`, `python-decouple`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL (or SQLite for local dev)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Tariel1997/django-bank-api.git
    cd bank_api
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Run the detailed server**:
    ```bash
    python manage.py runserver
    ```

---

## 📡 API Endpoints

### **Authentication**
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/register/` | Register a new user |
| `POST` | `/api/login/` | Obtain access & refresh tokens |
| `POST` | `/api/token/refresh/` | Refresh access token |

### **Accounts**
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/account/` | Get current user's account details |
| `POST` | `/api/deposit/` | Deposit funds |
| `POST` | `/api/withdraw/` | Withdraw funds |
| `POST` | `/api/transfer/` | Transfer funds to another user |

### **Transactions & Analytics**
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/transactions/` | View transaction history |
| `GET` | `/api/analytics/` | Get spending summary by category |

### **Documentation**
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/schema/` | Download API Schema (YAML) |
| `GET` | `/api/docs/` | Interactive Swagger UI |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---
