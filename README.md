# 🌐 Local DevOps Project with Ansible & Docker

Автоматизация локальной микросервисной инфраструктуры через **Ansible** и **Docker**: Flask, PostgreSQL, Nginx.

## 📦 Сервисы
- **Nginx** — reverse proxy (порт 80)  
- **Flask** — Python веб-приложение  
- **PostgreSQL** — база данных  

## 🚀 Быстрый старт
```bash
cd local-ansible

# Собрать Docker образ Flask
cd app
docker build -t my_flask_image:latest .
cd ..

# Запустить инфраструктуру
ansible-playbook playbooks/site.yml
docker ps — контейнеры: postgres, flask_app, nginx
curl http://localhost — ответ Flask приложения
