#!/bin/bash
set -e

# ============================================
# LocalMarket - Скрипт резервного копирования БД
# ============================================
# Использование: ./scripts/backup.sh
# Бэкап сохраняется в ./backups/ с меткой времени.

BACKUP_DIR="./backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/localmarket_${TIMESTAMP}.sql.gz"

# Загрузка переменных окружения
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

DB_USER="${DB_USER:-admin}"
DB_NAME="${DB_NAME:-localmarket}"
CONTAINER_NAME="lm_postgres"

# Создание директории для бэкапов
mkdir -p "$BACKUP_DIR"

echo "=== Starting backup: ${BACKUP_FILE} ==="

docker exec "$CONTAINER_NAME" \
    pg_dump -U "$DB_USER" "$DB_NAME" | gzip > "$BACKUP_FILE"

echo "=== Backup completed: ${BACKUP_FILE} ($(du -h "$BACKUP_FILE" | cut -f1)) ==="

# Удаление бэкапов старше 30 дней
find "$BACKUP_DIR" -name "*.sql.gz" -mtime +30 -delete
echo "=== Old backups cleaned up ==="
