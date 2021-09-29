#!/bin/bash
. /root/env.sh
python /load_json.py >> /var/log/cron.log
