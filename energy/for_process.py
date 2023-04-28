import psutil
import os
import subprocess
# Define the pgrep name to filter by
pgrep_name = 'chrome'

# Run the pgrep command to get the process IDs for the specified name
pgrep_cmd = ['pgrep', pgrep_name]
pgrep_proc = subprocess.run(pgrep_cmd, stdout=subprocess.PIPE, universal_newlines=True)
pgrep_output = pgrep_proc.stdout.strip().split('\n')
pgrep_pids = [int(pid) for pid in pgrep_output]
print(pgrep_pids)


process = psutil.Process(8578)
energy_usage = process.cpu_percent() * psutil.cpu_freq().current * psutil.cpu_count()
print('energy_usage', energy_usage)
energy_usage_wh = energy_usage / 3600
print('energy_usage_wh', energy_usage_wh)