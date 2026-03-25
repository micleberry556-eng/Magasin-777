# LocalMarket

Микросервисная платформа маркетплейса с Docker Compose оркестрацией.

---

## Структура проекта

```
localmarket/
├── docker-compose.yml          # Основной файл оркестрации
├── .env.example                # Шаблон конфигурации
├── deploy.sh                   # Скрипт развертывания
├── services/
│   ├── gateway/                # API Gateway (Nginx)
│   │   └── nginx.conf
│   ├── auth/                   # Auth Service (заглушка)
│   ├── catalog/                # Catalog Service (заглушка)
│   ├── evaluator/              # Web-сервис оценки/процентов (Python/FastAPI)
│   │   ├── Dockerfile
│   │   └── app/
│   │       ├── main.py
│   │       └── requirements.txt
├── frontend/                   # Next.js приложение
│   ├── Dockerfile
│   ├── package.json
│   ├── next.config.js
│   └── pages/
│       └── index.js
├── scripts/
│   ├── init_db.sh              # Инициализация БД (таблицы + seed-данные)
│   └── backup.sh               # Скрипт резервного копирования БД
└── data/                       # Тома для данных (создаются автоматически)
```

---

## Требования

- **Docker** >= 20.10
- **Docker Compose** >= 2.0 (или `docker-compose` v1.29+)

Установка Docker:
- Linux: https://docs.docker.com/engine/install/
- macOS: https://docs.docker.com/desktop/install/mac-install/
- Windows: https://docs.docker.com/desktop/install/windows-install/

---

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/micleberry556-eng/Magasin-777.git
cd Magasin-777
```

### 2. Настройка окружения

Скопируйте шаблон конфигурации и при необходимости измените значения:

```bash
cp .env.example .env
```

Основные переменные в `.env`:

| Переменная              | По умолчанию | Описание                                      |
|-------------------------|--------------|-----------------------------------------------|
| `DB_USER`               | `admin`      | Пользователь PostgreSQL                       |
| `DB_PASSWORD`           | `secret`     | Пароль PostgreSQL                             |
| `DB_NAME`               | `localmarket`| Имя базы данных                               |
| `MINIO_ROOT_USER`       | `minioadmin` | Логин MinIO                                   |
| `MINIO_ROOT_PASSWORD`   | `minioadmin` | Пароль MinIO                                  |
| `EVALUATOR_EXTERNAL_URL`| _(пусто)_    | URL внешнего сервиса оценки (опционально)     |

> **Важно:** Для продакшен-среды обязательно измените пароли по умолчанию.

### 3. Запуск (автоматический)

```bash
chmod +x deploy.sh scripts/init_db.sh scripts/backup.sh
./deploy.sh
```

Скрипт автоматически:
1. Проверит наличие Docker и Docker Compose
2. Создаст `.env` из шаблона (если не существует)
3. Соберет все контейнеры
4. Запустит сервисы
5. Дождется готовности базы данных

### 4. Запуск (ручной)

Если вы предпочитаете запускать вручную:

```bash
cp .env.example .env
docker compose build
docker compose up -d
```

---

## Доступ к сервисам

После запуска доступны следующие адреса:

| Сервис            | URL                          | Описание                        |
|-------------------|------------------------------|---------------------------------|
| Frontend          | http://localhost:3000         | Web-интерфейс (Next.js)        |
| API Gateway       | http://localhost:8080         | Единая точка входа (Nginx)     |
| Evaluator API     | http://localhost:8001         | Прямой доступ к сервису оценки |
| MinIO Console     | http://localhost:9001         | Консоль объектного хранилища   |
| PostgreSQL        | `localhost:5432`             | База данных                     |
| Redis             | `localhost:6379`             | Кэш / очереди                  |

---

## API: Сервис оценки

### POST `/api/v1/evaluate`

Оценка товара и расчет комиссии.

**Запрос:**

```bash
curl -X POST http://localhost:8080/api/v1/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "base_price": 1000.0,
    "params": {
      "rating": 4.8,
      "sales_velocity": 50,
      "category": "electronics"
    }
  }'
```

**Ответ:**

```json
{
  "score": 77.6,
  "recommended_price": 1077.6,
  "commission_percent": 9.5,
  "rationale": "Score calculated: rating=4.8 (weight 0.6), sales_velocity=50 (weight 0.4). Category 'electronics' base commission 10.0%. Loyalty discount applied."
}
```

**Параметры запроса:**

| Поле          | Тип    | Обязательное | Описание                              |
|---------------|--------|:------------:|---------------------------------------|
| `product_id`  | string | Нет          | ID товара                             |
| `seller_id`   | string | Нет          | ID продавца                           |
| `base_price`  | float  | Да           | Базовая цена товара                   |
| `params`      | object | Нет          | Дополнительные параметры              |

**Параметры `params`:**

| Поле             | Тип    | По умолчанию | Описание                          |
|------------------|--------|:------------:|-----------------------------------|
| `rating`         | float  | `4.0`        | Рейтинг товара/продавца (0-5)    |
| `sales_velocity` | int    | `10`         | Продаж в месяц                    |
| `category`       | string | `"default"`  | Категория (`electronics`, `clothing`, `food`) |

### GET `/health`

Проверка работоспособности сервиса.

```bash
curl http://localhost:8080/api/v1/health
```

---

## Алгоритм оценки

Встроенный алгоритм (раздел 13 ТЗ):

1. **Score (0-100):**
   - `score = (rating / 5.0 * 100) * 0.6 + (sales_velocity / 100 * 100) * 0.4`

2. **Комиссия:**
   - Базовая ставка зависит от категории: `electronics` = 10%, `clothing` = 12%, `food` = 8%, остальные = 15%
   - Скидка за лояльность: -5% к комиссии при рейтинге > 4.5

3. **Рекомендуемая цена:**
   - `recommended_price = base_price * (1 + score / 1000)`

Для использования внешнего сервиса оценки укажите его URL в переменной `EVALUATOR_EXTERNAL_URL` в файле `.env`. При ошибке внешнего сервиса система автоматически переключится на встроенный алгоритм (fallback).

---

## База данных

При первом запуске автоматически создаются таблицы и seed-данные:

**Таблицы:**
- `users` — пользователи (admin, seller, buyer)
- `categories` — категории товаров
- `products` — товары
- `orders` — заказы
- `order_items` — позиции заказов

**Seed-данные:**
- Администратор: `admin@local.market`
- Продавец: `seller@local.market`
- Покупатель: `buyer@local.market`
- 3 демо-товара в категории "Электроника"

Подключение к БД напрямую:

```bash
docker exec -it lm_postgres psql -U admin -d localmarket
```

---

## Резервное копирование

Создание бэкапа базы данных:

```bash
./scripts/backup.sh
```

Бэкапы сохраняются в директорию `./backups/` с меткой времени. Бэкапы старше 30 дней удаляются автоматически.

Восстановление из бэкапа:

```bash
gunzip -c backups/localmarket_YYYYMMDD_HHMMSS.sql.gz | \
  docker exec -i lm_postgres psql -U admin -d localmarket
```

---

## Управление сервисами

```bash
# Просмотр статуса контейнеров
docker compose ps

# Просмотр логов всех сервисов
docker compose logs -f

# Логи конкретного сервиса
docker compose logs -f evaluator-service

# Перезапуск сервиса
docker compose restart evaluator-service

# Остановка всех сервисов
docker compose down

# Остановка с удалением данных (volumes)
docker compose down -v

# Пересборка и перезапуск
docker compose up -d --build
```

---

## Архитектура

```
┌─────────────┐     ┌──────────────────┐     ┌───────────────────┐
│   Browser    │────>│  Nginx Gateway   │────>│ Evaluator Service │
│  :3000/:8080 │     │     :80 (8080)   │     │   (FastAPI :8000) │
└─────────────┘     └──────────────────┘     └───────────────────┘
                            │                         │
                            │                         │
                    ┌───────▼────────┐       ┌────────▼────────┐
                    │   Frontend     │       │   PostgreSQL    │
                    │  (Next.js)     │       │    :5432        │
                    │   :3000        │       └─────────────────┘
                    └────────────────┘
                                             ┌─────────────────┐
                                             │     Redis       │
                                             │    :6379        │
                                             └─────────────────┘

                                             ┌─────────────────┐
                                             │     MinIO       │
                                             │  :9000 / :9001  │
                                             └─────────────────┘
```

---

## Что реализовано (MVP)

- **Микросервисная архитектура** в Docker Compose с единой сетью
- **PostgreSQL** с автоматическим созданием таблиц и seed-данными
- **Сервис оценки (Evaluator)** на FastAPI — полный алгоритм расчета score, комиссии и рекомендуемой цены
- **API Gateway (Nginx)** с маршрутизацией к микросервисам и поддержкой WebSocket
- **Frontend (Next.js)** с тестовой страницей и кнопкой проверки API
- **MinIO** — объектное хранилище (S3-совместимое)
- **Redis** — кэш и очереди сообщений
- **Скрипты:** автоматическое развертывание, инициализация БД, резервное копирование
- **Офлайн-режим:** все образы кэшируются локально после первой сборки
- **Безопасность:** переменные окружения вынесены в `.env`

## Заглушки для будущей разработки

- `POST /api/catalog` — сервис каталога
- `POST /api/auth` — сервис авторизации

---

## Лицензия

MIT
