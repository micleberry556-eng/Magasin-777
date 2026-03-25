#!/bin/bash
set -e

# ============================================
# LocalMarket - Инициализация базы данных
# ============================================
# Этот скрипт выполняется автоматически внутри контейнера
# PostgreSQL при первом запуске (docker-entrypoint-initdb.d).

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

    -- ==========================================
    -- Таблица пользователей
    -- ==========================================
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255),
        role VARCHAR(50) DEFAULT 'buyer',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- ==========================================
    -- Таблица категорий
    -- ==========================================
    CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        slug VARCHAR(255) UNIQUE NOT NULL,
        parent_id INTEGER REFERENCES categories(id)
    );

    -- ==========================================
    -- Таблица товаров
    -- ==========================================
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        price NUMERIC(10, 2) NOT NULL,
        category_id INTEGER REFERENCES categories(id),
        seller_id INTEGER REFERENCES users(id),
        rating NUMERIC(3, 2) DEFAULT 0.00,
        sales_count INTEGER DEFAULT 0,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- ==========================================
    -- Таблица заказов
    -- ==========================================
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        buyer_id INTEGER REFERENCES users(id),
        status VARCHAR(50) DEFAULT 'pending',
        total_amount NUMERIC(10, 2) DEFAULT 0.00,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- ==========================================
    -- Таблица позиций заказа
    -- ==========================================
    CREATE TABLE IF NOT EXISTS order_items (
        id SERIAL PRIMARY KEY,
        order_id INTEGER REFERENCES orders(id),
        product_id INTEGER REFERENCES products(id),
        quantity INTEGER NOT NULL DEFAULT 1,
        price NUMERIC(10, 2) NOT NULL
    );

    -- ==========================================
    -- Seed Data: Пользователи
    -- ==========================================
    INSERT INTO users (email, role) VALUES
        ('admin@local.market', 'admin'),
        ('seller@local.market', 'seller'),
        ('buyer@local.market', 'buyer')
    ON CONFLICT (email) DO NOTHING;

    -- ==========================================
    -- Seed Data: Категории
    -- ==========================================
    INSERT INTO categories (name, slug) VALUES
        ('Электроника', 'electronics'),
        ('Одежда', 'clothing'),
        ('Продукты питания', 'food'),
        ('Товары для дома', 'home')
    ON CONFLICT (slug) DO NOTHING;

    -- ==========================================
    -- Seed Data: Товары
    -- ==========================================
    INSERT INTO products (name, description, price, category_id, seller_id, rating, sales_count) VALUES
        ('Смартфон X', 'Флагманский смартфон с AMOLED экраном', 699.99, 1, 2, 4.7, 150),
        ('Ноутбук Pro', 'Профессиональный ноутбук для разработчиков', 1299.50, 1, 2, 4.9, 85),
        ('Беспроводные наушники', 'Наушники с активным шумоподавлением', 199.00, 1, 2, 4.3, 320)
    ON CONFLICT DO NOTHING;

EOSQL

echo "=== Database initialized successfully ==="
