# 🚀 Flask Todo App on Azure Kubernetes Service (AKS)

A full-stack **Todo Application** deployed on **Azure Kubernetes Service (AKS)** using Python Flask and PostgreSQL.

## ✨ Live Demo
**URL:** http://20.164.108.179

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud**: Microsoft Azure AKS

## 📸 Screenshots

![Web Application](screenshots/web-interface.png)
*Clean Todo Web Interface*

![Kubernetes Pods](screenshots/kubectl-get-all.png)
*Running Pods on AKS*

![Azure Cluster](screenshots/azure-aks.png)
*Azure Kubernetes Service Cluster*

## 📁 Project Structure

```bash
flask-todo-aks/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── k8s/
│   ├── namespace.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── flask-deployment.yaml
│   └── flask-service.yaml
└── README.md


 Features Demonstrated

Multi-tier architecture (Backend + Database)

Docker containerization

Kubernetes Deployments, Services, and LoadBalancer

Persistent storage with PostgreSQL

Deployed on real cloud (Azure AKS)



 What I Learned

Deploying stateful applications on Kubernetes

Connecting services using DNS names

Troubleshooting common issues (CrashLoopBackOff, image pulling, templates)

Managing resources on Azure AKS

