#!/bin/sh
# wait-for-it.sh - Ожидает доступности хоста и порта

set -e

host="$1"
shift
cmd="$@"

until nc -z "$host" 5432; do
  echo "Ждём доступности $host:5432..."
  sleep 1
done

exec $cmd
