#!/bin/bash

# Get current date for log file
DATE=$(date +%F)
PROCESS_LOG="process_log_$DATE.log"
HIGH_MEM_LOG="high_mem_processes.log"

# 1. Log Running Processes
echo "í³‹ Logging all running processes to $PROCESS_LOG..."
ps aux > "$PROCESS_LOG"

# 2. Check for High Memory Usage
echo "í´ Checking for high memory usage..."
high_mem_procs=$(ps aux --sort=-%mem | awk '$4 > 30')

if [[ -n "$high_mem_procs" ]]; then
    echo "âš ï¸ WARNING: Processes using more than 30% memory found!"
    echo "$high_mem_procs" >> "$HIGH_MEM_LOG"
else
    echo "âœ… No high memory usage processes detected."
fi

# 3. Check Disk Space on Root (/)
echo "í²½ Checking disk space on / ..."
disk_usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [[ "$disk_usage" -gt 80 ]]; then
    echo "âš ï¸ WARNING: Disk usage on / is above 80% ($disk_usage%)"
else
    echo "âœ… Disk usage on / is normal ($disk_usage%)"
fi

# 4. Summary
total_procs=$(ps aux | wc -l)
high_mem_count=$(echo "$high_mem_procs" | wc -l)

echo ""
echo "í³Š --- SYSTEM SUMMARY ---"
echo "Total running processes: $total_procs"
echo "Processes using >30% memory: $high_mem_count"
echo "Disk usage on /: $disk_usage%"
echo "Processes using >30% memory: $high_mem_count"
echo "Disk usage on /: $disk_usage%"
echo "Processes using >30% memory: $high_mem_count"
echo "Disk usage on /: $disk_usage%"
