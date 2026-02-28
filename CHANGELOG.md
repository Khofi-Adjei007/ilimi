# Changelog

All notable changes to Ilimi will be documented here.

## [Unreleased]
- Initial project setup
- Core architecture planning
```

---

## GitHub Settings to Configure

Once the repo is created, go through these settings:

**General:**
- Add a social preview image (a simple branded banner with the Ilimi name — even a basic one made in Canva looks professional)
- Enable Issues
- Enable Discussions (great for community and feedback later)
- Disable Wiki (keep docs in the repo itself)

**Pages (optional but impressive):**
- You can host basic documentation on GitHub Pages later

**Secrets (Settings → Secrets → Actions):**
- Add your environment variables here when you set up CI/CD

---

## GitHub Issues — Set Up Labels Immediately

Good label organization makes the project look active and well-managed:
```
Type labels:
🐛 bug
✨ feature
📚 documentation
🔧 maintenance
🚀 enhancement

Module labels:
auth
students
attendance
fees
notifications
tenants

Priority labels:
🔴 priority: high
🟡 priority: medium
🟢 priority: low

Status labels:
in progress
blocked
needs review
```

---

## First Issues to Create

Right after setup, create these issues — it shows the project has active direction:
```
#1 — Project scaffold and Django setup
#2 — Custom User model and authentication
#3 — School and Branch (tenant) models
#4 — Role-based permission system
#5 — Student enrollment module
#6 — Attendance tracking module
#7 — Fee management and Paystack integration
#8 — Landing page design
```

This transforms the repo from "a folder of code" into "a project with a plan." Anyone landing on the Issues tab can immediately see the roadmap in motion.

---

## GitHub Projects Board

Create a Project board (the kanban view) with these columns:
```
Backlog → In Progress → In Review → Done
```

Link your issues to the board. This is what separates a side project from something that looks production-serious.

---

## The First Commit Message

When you push the initial scaffold, make the commit message intentional:
```
chore: initial project scaffold

- Django 5.0 project structure with config/ layout
- Split settings (base, development, production)
- Apps directory with all core modules scaffolded
- Docker and docker-compose configuration
- Tailwind CSS setup
- Requirements split into base, dev, production
- Environment variable configuration via django-environ
- Africa/Accra timezone set
- PostgreSQL as default database