# ALX Project Nexus – Backend System

## 📌 Overview

**ALX Project Nexus** is a production-ready backend system built with **Django** and **Django REST Framework**, designed to manage structured business workflows such as **orders, approvals, trials, and notifications**.

The system follows **real-world backend engineering practices**, including:
- Clean domain modeling
- Role-based workflows
- Asynchronous background processing
- Containerized deployment
- API documentation and testing


## 🧱 Core Tech Stack

- **Python 3**
- **Django**
- **Django REST Framework (DRF)**
- **PostgreSQL** (primary database)
- **Celery** (asynchronous task processing)
- **Redis** (message broker & result backend)
- **Docker & Docker Compose**
- **Swagger**
- **JWT Authentication**

---

## 🧠 High-Level Architecture
```
Client (Postman / Frontend)
        ↓
Django REST API (DRF)
        ↓
Business Logic & Workflows
        ↓
PostgreSQL Database
        ↓
Django Signals
        ↓
Celery Tasks
        ↓
Redis (Message Broker)
        ↓
Asynchronous Notifications
```

Key architectural decisions:
- **Models first, APIs second**
- **Synchronous APIs, asynchronous side effects**
- **Loose coupling via signals and Celery**
- **Production parity using Docker**

---

## 🧩 Project Structure (Simplified)
```text
alx-project-nexus/
│
├── prodexa/                     # Django project configuration
│   ├── __init__.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Root URL configuration
│   ├── celery.py                # Celery application setup
│   └── wsgi.py
│
├── approvals/                   # Approval workflows
│   ├── __init__.py
│   ├── models.py                # Approval-related models
│   ├── signals.py               # Triggers async notifications
│
├── orders/                      # Orders & change logs
│   ├── __init__.py
│   ├── models.py                # Order domain models
│   ├── signals.py               # Order lifecycle events
│
├── notifications/               # Notification system
│   ├── __init__.py
│   ├── models.py                # Notification records
│   ├── tasks.py                 # Celery async tasks
│
├── docker-compose.yml           # Multi-container setup
├── Dockerfile                   # Django application image
├── requirements.txt             # Python dependencies
└── README.md
```
---

## 🧭 Development Timeline & Methodology

### Models 
Models were designed before APIs to ensure:
- Correct relationships
- Accurate business rules
- Stable data contracts

> APIs, Swagger, and Docker all depend on models — not the other way around.

---

### Django Admin Registration
All models were registered early in Django Admin to:
- Validate relationships visually
- Catch modeling mistakes early
- Debug data faster


---

### Superuser & Data Validation
Before writing APIs:
- Sample data was created
- Relationships were validated
- ERD assumptions were verified

This prevented incorrect API logic later.

---

### Django REST Framework APIs
APIs were added in this order:
1. **Serializers**
2. **Views (APIView / ViewSet)**
3. **URLs / Routers**

Focus areas:
- CRUD operations
- Role-based access
- Clear request/response contracts

---

### Swagger / OpenAPI
Swagger was introduced **after APIs existed**, not before.

Why?
- Swagger **documents** APIs
- It does not generate them

Swagger is used as:
- API contract
- Testing console
- Documentation for reviewers and interviewers

---

### 🐳 Dockerization
Docker was added **only after**:
- App worked locally
- APIs were stable
- Swagger was verified

Docker setup includes:
- Django app
- PostgreSQL
- Redis
- Celery worker

This ensures **production parity**.

---

###  Celery & Redis
Celery was introduced **after core APIs**, not at the beginning.

Used for:
- Notifications
- Background side effects
- Non-blocking workflows

Key principle:
> APIs should respond fast — side effects run asynchronously.

---

## 🔔 Notification System Design

### Why Asynchronous Notifications?
- Avoid blocking API responses
- Improve performance
- Enable retries and fault tolerance

### How It Works
1. Business event occurs (approval, order change, etc.)
2. Django signal is triggered
3. Signal dispatches a **Celery task**
4. Celery worker creates the notification
5. Redis handles task queuing

### Example
```python
send_notification.delay(
    recipient_id=user.id,
    notification_type="ORDER_UPDATE",
    message="Your order was approved"
) 
```
---
## 💻 Running the Project Locally (Docker)

### 1️⃣ Prerequisites
Ensure having the following installed:
* **Docker** & **Docker Compose**
* **Git**

### 2️⃣ Clone the Repository
```bash
git clone [https://github.com/Asmaa-Mahgoub/alx-project-nexus](https://github.com/Asmaa-Mahgoub/alx-project-nexus)
cd alx-project-nexus

### 3️⃣ Environment Variables

Create a .env file (or set variables in your shell):

DJANGO_SETTINGS_MODULE=prodexa.settings
DEBUG=True

POSTGRES_DB=prodexa
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

CELERY_BROKER_URL=redis://redis:6379/0

### 4️⃣ Build and Start Containers
docker compose build
docker compose up

This will start:

Django API
PostgreSQL database
Redis
Celery worker

### 5️⃣ Apply Migrations

In a new terminal:
docker compose exec web python manage.py migrate

### 6️⃣ Create Superuser (Optional)
docker compose exec web python manage.py createsuperuser


## 🔒 Authentication & Security

### 🔑 Authentication
* **Framework:** Powered by **Django REST Framework (DRF)**.
* **Methods:** Supports both **Token-based (JWT)** and **Session-based** authentication.
* **Requirements:** All protected endpoints require valid authentication headers (e.g., `Authorization: Bearer <token>`).

### 🛡️ Authorization
* **API Level:** Permissions are strictly enforced at the view level.
* **Role-Based Access Control (RBAC):** Can be implemented using:
    * **Django Groups:** For high-level role management.
    * **Custom DRF Permissions:** For fine-grained, logic-based access control.

### 🚀 Security Best Practices
* **Environment Isolation:** All secrets, keys, and sensitive credentials are stored in `.env` files and never committed to version control.
* **Database Security:** Database credentials are dynamically loaded via environment variables; **no hardcoding**.
* **Host Validation:** `ALLOWED_HOSTS` is explicitly configured to prevent HTTP Host header attacks in production.
* **Process Separation:** Asynchronous tasks (Celery) are fully isolated from the request/response lifecycle to ensure performance and reliability.
* **Ephemeral Broker:** Redis is utilized strictly as a message broker for task distribution, ensuring it is not used for persistent data storage.

## 📖 API Documentation

The project features interactive API documentation powered by **drf-spectacular**. You can explore the endpoints, view request/response schemas, and test the API directly from your browser.

### 🚀 Interactive Documentation
* **Swagger UI:** [https://alx-project-nexus-j3g2.onrender.com/api/docs/](https://alx-project-nexus-j3g2.onrender.com/api/docs/)

## 🌐 Live Deployment

The project is currently deployed and hosted on **Render**. You can access the live API and the base deployment at the link below:

**Base URL:** [https://alx-project-nexus-j3g2.onrender.com/](https://alx-project-nexus-j3g2.onrender.com/)

---





