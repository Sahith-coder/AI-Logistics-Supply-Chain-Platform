# AI-Powered Logistics & Supply Chain Intelligence Platform

## 1. Project Overview

An AI-powered logistics and supply chain management platform designed to help businesses manage customers, orders, warehouses, drivers, vehicles, assignments, and delivery operations from a centralized system.

The platform is being developed in stages, starting with a reliable Django and PostgreSQL backend and gradually adding REST APIs, a modern frontend, logistics optimization, AI/ML capabilities, cloud deployment, and a mobile application.

---

## 2. Problem Statement

Traditional logistics operations often depend on manual coordination between customers, warehouses, drivers, and vehicles. This can lead to:

- Delayed deliveries
- Poor vehicle and driver utilization
- Manual assignment errors
- Limited visibility into order status
- Difficulty handling delivery constraints
- Lack of intelligent decision support

This project aims to provide a centralized and intelligent platform for improving logistics operations.

---

## 3. Proposed Solution

The platform will provide:

- Centralized order management
- Warehouse management
- Driver and vehicle management
- Driver and vehicle assignment
- Order status tracking
- Role-based access
- REST APIs for application integration
- Route and assignment optimization
- AI/ML-based logistics intelligence
- Real-time tracking and decision support in later phases

---

## 4. Key Features

### Currently Implemented

- Django backend
- PostgreSQL database
- Custom user model with roles:
  - Customer
  - Driver
  - Admin
- Warehouse management
- Customer profiles
- Driver management
- Vehicle management
- Order management
- Order priorities
- Driver and vehicle assignment
- Driver availability validation
- Vehicle availability validation
- Automatic order status update after assignment
- Order status transition validation
- Django Admin interface
- Environment-based database configuration
- Git and GitHub version control

### Planned Features

- Django REST Framework APIs
- Authentication and role-based API permissions
- React web frontend
- Interactive maps and route visualization
- Automatic driver assignment
- Route optimization
- Vehicle-capacity and vehicle-type constraints
- Traffic and road-condition considerations
- Delivery ETA prediction
- Delay prediction
- Demand forecasting
- AI logistics assistant
- Real-time delivery tracking
- Cloud deployment
- React Native mobile application

---

## 5. Current Order Workflow

The current order lifecycle is:

```text
PENDING
   ↓
ASSIGNED
   ↓
PICKED_UP
   ↓
IN_TRANSIT
   ↓
OUT_FOR_DELIVERY
   ↓
DELIVERED
```

Cancellation is supported from appropriate early stages.

Invalid status jumps are rejected by the backend business logic.

---

## 6. System Architecture

The planned high-level architecture is:

```text
                 Web / Mobile Users
                        |
                React / React Native
                        |
                 Django REST API
                        |
                 Django Backend
              /          |                       /           |                 PostgreSQL     Logistics      AI/ML
       Database      Algorithms      Services
                         |
                   Maps / Routing
                         |
                   Cloud Services
```

The project is being developed incrementally. The current implementation focuses on the Django + PostgreSQL backend foundation.

---

## 7. Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| API | Django REST Framework |
| Database | PostgreSQL |
| Initial Admin UI | Django Admin |
| Planned Web Frontend | React |
| Planned Styling | Tailwind CSS |
| Planned Mobile App | React Native |
| AI/ML | Python ML ecosystem |
| Maps/Routing | OpenStreetMap / OSRM or suitable mapping APIs |
| Version Control | Git + GitHub |
| Planned Deployment | Cloud platform / AWS, Azure or GCP |

---

## 8. Project Structure

Current backend structure:

```text
backend/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── .gitignore
├── manage.py
└── requirements.txt
```

The local `.env` file is intentionally excluded from GitHub.

---

## 9. Database Entities

The current backend contains these core entities:

```text
User
 ├── Customer
 └── Driver

Warehouse
Vehicle
Order
Assignment
```

### Main relationships

```text
Customer
   |
   └── Order
          |
          ├── Warehouse
          |
          └── Assignment
                  ├── Driver
                  └── Vehicle
```

---

## 10. Local Setup

### Prerequisites

Install:

- Python 3.x
- PostgreSQL
- Git

### Clone the repository

```bash
git clone https://github.com/Sahith-coder/AI-Logistics-Supply-Chain-Platform.git
cd AI-Logistics-Supply-Chain-Platform
```

### Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root:

```env
DB_NAME=logistics_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

Never commit the real `.env` file to GitHub.

### Run migrations

```bash
python manage.py migrate
```

### Create an admin user

```bash
python manage.py createsuperuser
```

### Start the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## 11. Team Git Workflow

The `main` branch is protected.

Developers should create feature branches instead of working directly on `main`.

Example:

```bash
git checkout main
git pull origin main

git checkout -b feature/api-orders
```

After completing the work:

```bash
git add .
git commit -m "Add order API"
git push -u origin feature/api-orders
```

Then create a Pull Request targeting `main`.

### Recommended branch naming

```text
feature/api
feature/frontend
feature/auth
feature/ai
feature/routing
fix/order-validation
```

### Workflow

```text
main
  |
  +---- feature branch
  |          |
  |       development
  |          |
  |       Pull Request
  |          |
  +------ Review ------+
                       |
                    main
```

Do not commit passwords, API keys, `.env` files, virtual environments, or local database files.

---

## 12. Development Roadmap

### Phase 1 — Backend Foundation
- [x] Django project setup
- [x] PostgreSQL integration
- [x] Core database models
- [x] Django Admin
- [x] Initial business validations
- [x] GitHub repository

### Phase 2 — REST API
- [ ] Django REST Framework API structure
- [ ] Customer APIs
- [ ] Order APIs
- [ ] Warehouse APIs
- [ ] Driver APIs
- [ ] Vehicle APIs
- [ ] Assignment APIs

### Phase 3 — Authentication & Roles
- [ ] Authentication
- [ ] Customer permissions
- [ ] Driver permissions
- [ ] Admin permissions

### Phase 4 — Web Application
- [ ] React frontend
- [ ] Customer dashboard
- [ ] Admin dashboard
- [ ] Driver dashboard
- [ ] Order tracking UI

### Phase 5 — Smart Logistics
- [ ] Route calculation
- [ ] Driver assignment optimization
- [ ] Vehicle constraint handling
- [ ] Distance and delivery-time optimization
- [ ] Map integration

### Phase 6 — AI/ML Intelligence
- [ ] ETA prediction
- [ ] Delay prediction
- [ ] Demand forecasting
- [ ] AI logistics assistant

### Phase 7 — Deployment & Mobile
- [ ] Cloud deployment
- [ ] CI/CD
- [ ] Monitoring
- [ ] React Native mobile application

---

## 13. Project Status

**Current stage: Backend Foundation + Team GitHub Setup**

The core Django/PostgreSQL foundation has been implemented and tested. The next major development milestone is building the REST API layer using Django REST Framework.

---

## 14. Team

This project is being developed collaboratively using GitHub with protected `main` branch and feature-branch based development.

---

## License

This project is currently intended as an academic/project development platform. Licensing can be added when the project requirements are finalized.
