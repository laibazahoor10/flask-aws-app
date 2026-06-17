# flask-aws-app

A Flask web application demonstrating a full DevOps workflow — 
from containerization to cloud deployment and CI/CD automation.

## What This Project Covers
- **AWS Deployment** — Deployed on both EC2 (IaaS) and Elastic Beanstalk (PaaS)
- **Docker** — Containerized using Dockerfile and Docker Compose with named volumes and Docker Secrets
- **CI/CD Pipeline** — 4-stage declarative Jenkins pipeline (Build → Unit Test → Containerized Deploy → Selenium Test) automated via GitHub Webhooks
- **Automated Testing** — Unit tests with pytest and end-to-end browser tests with Selenium WebDriver

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python / Flask 3.0 |
| Database | SQLite |
| Containerization | Docker, Docker Compose |
| CI/CD | Jenkins, GitHub Webhooks |
| Testing | pytest, Selenium WebDriver |
| Cloud | AWS EC2, Elastic Beanstalk, S3 |
| OS | Ubuntu 24.04 / Amazon Linux 2023 |
