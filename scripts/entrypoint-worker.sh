#!/usr/bin/env bash
set -e

/bin/bash ./scripts/wait-for.sh ${REDIS_HOST:-redis} ${REDIS_PORT:-6379} 30

exec celery -A config worker -l info
