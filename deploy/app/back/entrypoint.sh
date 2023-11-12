#!/usr/bin/env bash
sleep 5

#накатываем миграции
python manage.py migrate --noinput

#генерируем статику
python manage.py collectstatic --noinput

#Запуск команды переданной из CMD/command
exec "$@"