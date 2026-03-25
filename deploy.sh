#!/bin/bash
set -e

echo "============================================"
echo "  LocalMarket - Deployment Script"
echo "============================================"
echo ""

# ------------------------------------------
# 1. Проверка зависимостей
# ------------------------------------------
echo "[1/5] Проверка зависимостей..."

if ! command -v docker &> /dev/null; then
    echo "ОШИБКА: Docker не установлен."
    echo "Установите Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! docker compose version &> /dev/null && ! command -v docker-compose &> /dev/null; then
    echo "ОШИБКА: Docker Compose не установлен."
    echo "Установите Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# Определяем команду compose
COMPOSE_CMD="docker compose"
if ! docker compose version &> /dev/null; then
    COMPOSE_CMD="docker-compose"
fi

echo "  Docker: $(docker --version)"
echo "  Compose: $($COMPOSE_CMD version 2>/dev/null || echo 'installed')"
echo ""

# ------------------------------------------
# 2. Настройка окружения
# ------------------------------------------
echo "[2/5] Настройка окружения..."

if [ ! -f .env ]; then
    echo "  Создание .env из .env.example..."
    cp .env.example .env
    echo "  ВНИМАНИЕ: Измените пароли в .env перед использованием в продакшене!"
else
    echo "  Файл .env уже существует."
fi
echo ""

# ------------------------------------------
# 3. Создание директорий для данных
# ------------------------------------------
echo "[3/5] Подготовка директорий..."
mkdir -p data
echo "  Директории готовы."
echo ""

# ------------------------------------------
# 4. Сборка контейнеров
# ------------------------------------------
echo "[4/5] Сборка контейнеров..."
$COMPOSE_CMD build
echo ""

# ------------------------------------------
# 5. Запуск сервисов
# ------------------------------------------
echo "[5/5] Запуск сервисов..."
$COMPOSE_CMD up -d

# Ожидание готовности БД
echo ""
echo "Ожидание готовности базы данных..."
for i in $(seq 1 30); do
    if docker exec lm_postgres pg_isready -U admin -d localmarket &> /dev/null; then
        echo "  База данных готова!"
        break
    fi
    if [ "$i" -eq 30 ]; then
        echo "  ПРЕДУПРЕЖДЕНИЕ: БД не ответила за 30 секунд. Проверьте логи: docker logs lm_postgres"
    fi
    sleep 1
done

echo ""
echo "============================================"
echo "  Развертывание завершено!"
echo "============================================"
echo ""
echo "  Frontend:       http://localhost:3000"
echo "  API Gateway:    http://localhost:8080"
echo "  Evaluator API:  http://localhost:8001"
echo "  MinIO Console:  http://localhost:9001"
echo "    (логин: minioadmin / пароль: minioadmin)"
echo ""
echo "  Проверка сервиса оценки:"
echo "    curl -X POST http://localhost:8080/api/v1/evaluate \\"
echo "      -H 'Content-Type: application/json' \\"
echo "      -d '{\"base_price\": 1000, \"params\": {\"rating\": 4.8, \"sales_velocity\": 50, \"category\": \"electronics\"}}'"
echo ""
echo "  Логи:           $COMPOSE_CMD logs -f"
echo "  Остановка:      $COMPOSE_CMD down"
echo "============================================"
