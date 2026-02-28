# Ilimi — School Management Platform

> Empowering schools across West Africa with smarter management tools.

Ilimi is a multi-tenant SaaS platform designed for multi-branch schools 
in Ghana and West Africa. It streamlines student management, attendance 
tracking, fee collection, and parent-teacher communication — all in one place.

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

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.0 (Python) |
| Database | PostgreSQL 15 |
| Frontend | Django Templates + Tailwind CSS |
| API | Django REST Framework |
| Cache / Queue | Redis + Celery |
| Payments | Paystack (Mobile Money support) |
| Containerization | Docker + Docker Compose |

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- Git

### Installation

\```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ilimi.git
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
\```

Visit `http://localhost:8000`

## 📁 Project Structure

\```
ilimi/
├── config/          # Django settings (base, dev, production)
├── apps/            # All Django applications
│   ├── accounts/    # Authentication & user management
│   ├── tenants/     # School & branch management
│   ├── students/    # Student enrollment
│   ├── attendance/  # Attendance tracking
│   ├── fees/        # Fee management & payments
│   └── ...
├── templates/       # HTML templates
├── static/          # CSS, JS, images
└── requirements/    # Split requirements files
\```

## 🗺️ Roadmap

- [x] Project architecture and planning
- [ ] Authentication and multi-tenant foundation
- [ ] Student and class management
- [ ] Attendance tracking
- [ ] Fee collection and Paystack integration
- [ ] Parent portal
- [ ] SMS notifications
- [ ] Reporting and analytics

## 🤝 Contributing

This project is currently in active early development. 
Contribution guidelines coming soon.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

## 📬 Contact

Built by [Your Name] — [khofiadjei@gmail.com](mailto:khofiadjei@gmail.com)
