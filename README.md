# Local DevOps Stack (Ansible)

Небольшой учебный проект для практики **Linux, сетей, Docker и Ansible**.  
Проект создаёт локальную инфраструктуру и управляет сервисами через Ansible.

## Цель

Изучить:

- управление системой через Ansible
- контейнеризацию с Docker
- сетевое взаимодействие сервисов
- структуру DevOps проекта уровня 

## Что сделано

1. Подготовлено окружение Linux
2. Установлены:
   - Ansible
   - Docker
3. Настроен запуск Docker без `sudo`
4. Создана структура Ansible проекта
5. Настроен **inventory** для локального хоста
6. Добавлены **group_vars** для переменных проекта
7. Созданы базовые **roles**:
   - docker — установка и запуск Docker
   - network — создание docker сети
   - db — будущая роль базы данных
   - app — роль приложения
   - nginx — роль веб-сервера
8. Подготовлен основной playbook `site.yml`

## Проверка работы
ansible-inventory -i inventories/dev/hosts.yml --list
ansible all -i inventories/dev/hosts.yml -m ping
