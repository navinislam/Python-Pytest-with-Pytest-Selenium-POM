#!/bin/bash
# wait-for-grid.sh

set -e
url="${HUB}/status" # for running locally switch to http://localhost:4444/wd/hub
wait_interval_in_seconds=1
max_wait_time_in_seconds=30
end_time=$((SECONDS + max_wait_time_in_seconds))
time_left=$max_wait_time_in_seconds

while [ $SECONDS -lt $end_time ]; do
    response=$(curl -sLf "$url" || echo "error")
    if [ "$response" != "error" ]; then
        ready=$(echo "$response" | jq -r '.value.ready')
        if [ "$ready" == "true" ]; then
            echo "Selenium Grid is up - executing tests"
            break
        fi
    fi
    echo "Waiting for the Grid. Sleeping for $wait_interval_in_seconds second(s). $time_left seconds left until timeout."
    sleep $wait_interval_in_seconds
    time_left=$((time_left - wait_interval_in_seconds))
done

if [ $SECONDS -ge $end_time ]; then
    echo "Timeout: The Grid was not started within $max_wait_time_in_seconds seconds."
    exit 1
fi
