#!/usr/bin/env bash
# Simple wait-for script: wait-for.sh host port timeout_seconds
set -e
host=$1
port=$2
timeout=${3:-30}

start=$(date +%s)
while ! (echo > /dev/tcp/$host/$port) >/dev/null 2>&1; do
  now=$(date +%s)
  if [ $((now-start)) -ge $timeout ]; then
    echo "Timeout waiting for $host:$port"
    exit 1
  fi
  sleep 1
done

exit 0
