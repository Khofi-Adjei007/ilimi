# Ilimi — School Management Platform

> Empowering schools across West Africa with smarter management tools.

Ilimi is a multi-tenant SaaS platform designed for multi-branch schools in Ghana and West Africa. It streamlines student management, attendance tracking, fee collection, and parent-teacher communication — all in one place.

---

## ✨ Features

- 🏫 Multi-branch school management
- 👨‍🎓 Student enrollment and profiles
- 📋 Attendance tracking
- 💳 Fee collection with Mobile Money (Paystack)
- 👨‍👩‍👧 Parent portal and communication
- 📊 Reports and analytics dashboards
- 🔔 SMS and in-app notifications
- 🔐 Role-based access control

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 5.0 (Python) |
| Database | PostgreSQL 15 |
| Frontend | Django Templates + Tailwind CSS |
| API | Django REST Framework |
| Cache / Queue | Redis + Celery |
| Payments | Paystack (Mobile Money support) |
| Containerization | Docker + Docker Compose |

---

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Khofi-Adjei007/ilimi.git
cd ilimi

# Copy environment variables
cp .env.example .env
# Edit .env with your values

# Build and start containers
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

Visit `http://localhost:8000`

---

## 📁 Project Structure

```
ilimi/
├── config/                  # Django settings (base, dev, production)
│   └── settings/
│       ├── base.py
│       ├── development.py
│       └── production.py
├── apps/                    # All Django applications
│   ├── public/              # Landing page and marketing
│   ├── accounts/            # Authentication & user management
│   ├── tenants/             # School & branch management
│   ├── academics/           # Academic year, terms, classes
│   ├── students/            # Student enrollment & profiles
│   ├── teachers/            # Teacher profiles & assignments
│   ├── parents/             # Parent portal & communication
│   ├── attendance/          # Attendance tracking
│   ├── fees/                # Fee management & payments
│   ├── notifications/       # SMS & in-app notifications
│   ├── reports/             # Reports & analytics
│   └── dashboard/           # Role-based dashboards
├── templates/               # HTML templates
├── static/                  # CSS, JS, images
├── requirements/            # Split requirements files
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── .env.example             # Environment variable template
├── Dockerfile
└── docker-compose.yml
```

---

## 🗺️ Roadmap

- [x] Project architecture and planning
- [ ] Authentication and multi-tenant foundation
- [ ] School and branch management
- [ ] Student enrollment and profiles
- [ ] Class and grade management
- [ ] Attendance tracking
- [ ] Fee collection and Paystack integration
- [ ] Parent portal
- [ ] SMS notifications (Arkesel integration)
- [ ] Reports and analytics dashboards
- [ ] Landing page

---

## 🏗️ Architecture Overview

Ilimi is built on a **shared-schema multi-tenancy** model. Each school is an isolated tenant — a teacher or student at School A can never access School B's data. Tenant isolation is enforced at the ORM level through scoped query managers on every model.

The permission system uses **role-based access control (RBAC)** with the following roles:

| Role | Scope |
|------|-------|
| Platform Super Admin | Full platform access |
| School Owner | All branches within their school |
| School Administrator | All branches, day-to-day operations |
| Branch Manager | Single branch only |
| Teacher | Assigned classes within a branch |
| Accountant | Fee management within a branch |
| Parent | Their own child(ren)'s data only |
| Student | Their own profile and records only |

---

## 🌍 Built for West Africa

Ilimi is designed specifically for the West African education market:

- **Mobile Money payments** via Paystack (MTN MoMo, Vodafone Cash, AirtelTigo)
- **SMS notifications** via Arkesel for parents who are more reachable by phone than email
- **Three-term academic calendar** matching Ghana's academic year structure
- **Multi-component fee structures** supporting tuition, PTA levy, feeding fees and more — paid by installment per term

---

## 🤝 Contributing

This project is currently in active early development. Contribution guidelines coming soon.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 📬 Contact

Built by Khofi Adjei — [khofiadjei@gmail.com](mailto:khofiadjei@gmail.com)

---

*Ilimi — from the Hausa word for knowledge and education.*
