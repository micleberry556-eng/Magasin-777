# LocalMarket — Интернет-магазин

Полнофункциональный интернет-магазин с админ-панелью, 300 темами оформления, мультиязычностью (13 языков), учетом товаров и SEO.

---

## Возможности

**Магазин (Frontend):**
- Главная страница с hero-секцией, категориями и рекомендуемыми товарами
- Каталог с фильтрацией по категориям и поиском
- Карточка товара с описанием, ценой, остатками, SEO
- Корзина с изменением количества
- Оформление заказа с формой доставки
- CMS-страницы (О нас, Контакты и любые другие)
- Мультиязычность: 13 языков (RU, EN, KK, UZ, TG, KY, AZ, TR, ZH, MS, TH, VI, ID)
- Динамическая тема оформления (цвета, шрифты, скругления, layout)

**Админ-панель (`/admin`):**
- Авторизация с JWT-токеном
- Dashboard со статистикой
- Управление товарами (CRUD, SEO, изображения, featured)
- Управление категориями
- Управление заказами (просмотр, смена статуса)
- Учет товаров / складской учет (приход, расход, корректировки, история)
- CMS-страницы (создание, редактирование, HTML-контент)
- 300 тем оформления (8 категорий: светлые, темные, яркие, минималистичные, неоновые, пастельные, корпоративные, градиентные)
- Настройки сайта: название, описание, логотип, фавикон, фон
- SEO: title, description, keywords, аналитика
- Загрузка изображений (логотип, фон, товары)
- Смена пароля администратора
- Выбор языка по умолчанию и валюты

---

## Структура проекта

```
Magasin-777/
├── docker-compose.yml              # Оркестрация всех сервисов
├── .env.example                    # Шаблон конфигурации
├── deploy.sh                       # Скрипт развертывания
├── services/
│   ├── gateway/
│   │   └── nginx.conf              # API Gateway
│   └── evaluator/
│       ├── Dockerfile
│       └── app/
│           ├── main.py             # Точка входа FastAPI
│           ├── requirements.txt
│           ├── core/
│           │   ├── config.py       # Конфигурация
│           │   ├── database.py     # SQLAlchemy engine
│           │   ├── security.py     # JWT, bcrypt
│           │   ├── i18n.py         # 13 языков перевода
│           │   └── themes_generator.py  # Генератор 300 тем
│           ├── models/             # SQLAlchemy модели
│           │   ├── user.py
│           │   ├── product.py      # Product, Category, StockMovement
│           │   ├── order.py        # Order, OrderItem
│           │   └── site.py         # SiteSettings, Page, Theme
│           ├── schemas/            # Pydantic схемы
│           │   ├── auth.py
│           │   ├── product.py
│           │   ├── order.py
│           │   └── site.py
│           └── routers/            # API эндпоинты
│               ├── admin_auth.py
│               ├── products.py
│               ├── categories.py
│               ├── orders.py
│               ├── pages.py
│               ├── settings.py
│               ├── themes.py
│               ├── stock.py
│               └── upload.py
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── next.config.js
│   ├── styles/
│   │   ├── globals.css             # Стили магазина (CSS Variables)
│   │   └── admin.css               # Стили админ-панели
│   ├── lib/
│   │   ├── api.js                  # API клиент
│   │   ├── useCart.js              # Контекст корзины
│   │   ├── useLang.js             # Контекст мультиязычности
│   │   ├── useTheme.js            # Контекст темы оформления
│   │   └── useAdmin.js            # Контекст авторизации админа
│   ├── components/
│   │   ├── Layout.js              # Основной layout магазина
│   │   ├── ProductCard.js         # Карточка товара
│   │   └── admin/
│   │       └── AdminLayout.js     # Layout админ-панели
│   └── pages/
│       ├── _app.js                # Провайдеры (Cart, Lang, Theme)
│       ├── index.js               # Главная страница
│       ├── catalog/
│       │   ├── index.js           # Каталог
│       │   └── [slug].js          # Карточка товара
│       ├── cart/index.js          # Корзина
│       ├── checkout/index.js      # Оформление заказа
│       ├── page/[slug].js         # CMS-страница
│       └── admin/
│           ├── index.js           # Логин
│           ├── dashboard.js       # Dashboard
│           ├── products.js        # Управление товарами
│           ├── categories.js      # Управление категориями
│           ├── orders.js          # Управление заказами
│           ├── stock.js           # Учет товаров
│           ├── pages.js           # CMS-страницы
│           ├── themes.js          # 300 тем оформления
│           ├── settings.js        # Настройки сайта / SEO
│           └── password.js        # Смена пароля
└── scripts/
    ├── backup.sh                  # Резервное копирование БД
    └── init_db.sh                 # (legacy) Инициализация БД
```

---

## Требования

- **Docker** >= 20.10
- **Docker Compose** >= 2.0

---

## Установка и запуск

### 1. Клонирование

```bash
git clone https://github.com/micleberry556-eng/Magasin-777.git
cd Magasin-777
```

### 2. Настройка

```bash
cp .env.example .env
```

Отредактируйте `.env` при необходимости:

| Переменная       | По умолчанию              | Описание                          |
|------------------|---------------------------|-----------------------------------|
| `DB_USER`        | `admin`                   | Пользователь PostgreSQL           |
| `DB_PASSWORD`    | `secret`                  | Пароль PostgreSQL                 |
| `SECRET_KEY`     | `change-me-in-production` | Секретный ключ JWT                |
| `ADMIN_EMAIL`    | `admin@localmarket.com`   | Email администратора              |
| `ADMIN_PASSWORD` | `admin123`                | Пароль администратора             |

> **Важно:** Для продакшена обязательно измените `SECRET_KEY`, `DB_PASSWORD` и `ADMIN_PASSWORD`.

### 3. Запуск

```bash
chmod +x deploy.sh
./deploy.sh
```

Или вручную:

```bash
docker compose build
docker compose up -d
```

### 4. Первый запуск

При первом запуске автоматически:
- Создаются все таблицы в БД
- Создается администратор (из `.env`)
- Генерируются 300 тем оформления
- Создаются демо-категории и товары

---

## Доступ

| Сервис          | URL                      | Описание                    |
|-----------------|--------------------------|-----------------------------|
| Магазин         | http://localhost:8080     | Главная страница магазина   |
| Админ-панель    | http://localhost:8080/admin | Вход в админку            |
| API (прямой)    | http://localhost:8001     | FastAPI backend             |
| MinIO Console   | http://localhost:9001     | Объектное хранилище         |

**Вход в админ-панель:**
- Email: `admin@localmarket.com`
- Пароль: `admin123`

---

## Админ-панель — Возможности

### Dashboard
Обзор: количество товаров, общий остаток на складе, товары с низким остатком.

### Товары
- Создание, редактирование, удаление товаров
- Поля: название, slug, описание, цена, старая цена, SKU, остаток, категория, изображение
- SEO: title и description для каждого товара
- Флаги: активный, рекомендуемый

### Категории
- CRUD категорий с slug и сортировкой

### Заказы
- Просмотр всех заказов с фильтрацией по статусу
- Детали заказа: клиент, товары, суммы
- Смена статуса: new → processing → shipped → delivered / cancelled

### Учет товаров (Inventory)
- Сводка: общее количество товаров, общий остаток, товары с низким остатком
- Запись движений: приход (purchase), возврат (return), корректировка (adjustment), ручная продажа (sale)
- История всех движений

### CMS-страницы
- Создание произвольных страниц (О нас, Контакты, Доставка и т.д.)
- HTML-редактор контента
- SEO для каждой страницы
- Публикация / снятие с публикации

### Темы оформления (300 шт.)
- 8 категорий: светлые, темные, яркие, минималистичные, неоновые, пастельные, корпоративные, градиентные
- Каждая тема: цвета (primary, secondary, accent, bg, text, header, footer), шрифт, скругления, layout
- Визуальный превью каждой темы
- Активация темы одним кликом — мгновенно применяется на сайте

### Настройки сайта
- Название и описание сайта
- Логотип, фавикон, фоновое изображение (загрузка файлов)
- SEO: title, description, keywords, код аналитики
- Язык по умолчанию (13 языков)
- Валюта (14 валют: USD, EUR, RUB, KZT, UZS, TJS, KGS, AZN, TRY, CNY, MYR, THB, VND, IDR)
- Контактная информация

### Смена пароля
- Изменение пароля администратора из панели

---

## Мультиязычность

Поддерживаемые языки:

| Код | Язык              |
|-----|-------------------|
| ru  | Русский           |
| en  | English           |
| kk  | Қазақша           |
| uz  | O'zbek            |
| tg  | Тоҷикӣ            |
| ky  | Кыргызча          |
| az  | Azərbaycan        |
| tr  | Türkçe            |
| zh  | 中文              |
| ms  | Bahasa Melayu     |
| th  | ไทย               |
| vi  | Tiếng Việt        |
| id  | Bahasa Indonesia  |

Переключение языка — в шапке сайта. Выбор сохраняется в localStorage.

---

## API

### Публичные эндпоинты

```
GET  /api/products              — Список товаров (фильтры: category_id, featured, search)
GET  /api/products/{slug}       — Товар по slug
GET  /api/categories            — Список категорий
GET  /api/categories/{slug}     — Категория по slug
POST /api/orders                — Создание заказа
GET  /api/pages                 — Список опубликованных страниц
GET  /api/pages/{slug}          — Страница по slug
GET  /api/settings              — Настройки сайта
GET  /api/themes                — Список тем (фильтр: category)
GET  /api/themes/categories     — Категории тем с количеством
GET  /api/themes/{id}           — Тема по ID
GET  /api/i18n                  — Список языков
GET  /api/i18n/{lang}           — Переводы для языка
GET  /health                    — Health check
```

### Админ эндпоинты (требуют JWT)

```
POST   /api/admin/login                    — Авторизация
POST   /api/admin/change-password          — Смена пароля
GET    /api/admin/me                       — Информация об админе
GET    /api/admin/products                 — Все товары
POST   /api/admin/products                 — Создать товар
PATCH  /api/admin/products/{id}            — Обновить товар
DELETE /api/admin/products/{id}            — Удалить товар
POST   /api/admin/categories              — Создать категорию
PATCH  /api/admin/categories/{id}         — Обновить категорию
DELETE /api/admin/categories/{id}         — Удалить категорию
GET    /api/admin/orders                  — Список заказов
GET    /api/admin/orders/{id}             — Детали заказа
PATCH  /api/admin/orders/{id}/status      — Обновить статус заказа
GET    /api/admin/pages                   — Все страницы
POST   /api/admin/pages                   — Создать страницу
PATCH  /api/admin/pages/{id}             — Обновить страницу
DELETE /api/admin/pages/{id}             — Удалить страницу
PATCH  /api/admin/settings               — Обновить настройки сайта
POST   /api/admin/themes/{id}/activate   — Активировать тему
GET    /api/admin/stock                  — История движений
POST   /api/admin/stock                  — Записать движение
GET    /api/admin/stock/summary          — Сводка по складу
POST   /api/admin/upload                 — Загрузка файла
```

---

## Управление

```bash
# Статус контейнеров
docker compose ps

# Логи
docker compose logs -f

# Перезапуск
docker compose restart

# Остановка
docker compose down

# Пересборка
docker compose up -d --build

# Бэкап БД
./scripts/backup.sh
```

---

## Технологии

- **Backend:** Python 3.11, FastAPI, SQLAlchemy 2.0, Pydantic v2
- **Frontend:** Next.js 14, React 18
- **Database:** PostgreSQL 14
- **Cache:** Redis 7
- **Storage:** MinIO (S3-compatible)
- **Gateway:** Nginx
- **Auth:** JWT + bcrypt
- **Container:** Docker Compose

---

## Лицензия

MIT
