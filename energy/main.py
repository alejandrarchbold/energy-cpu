import csv
import subprocess
import time


print('Empezar a ejecutar...')

time.sleep(120)

print('Comenzamos...')

# Define the pgrep names to filter by as a list
pgrep_names = ['ekf_lo', 'gazebo', 'gazebo_gui', 'joy_tel', 'robot', 'twist_', 'rostopic', 'nodo_position', 'ros', 'nodo_pid', 'pid', 'base', 'nodo_po', 'pos', 'move', 'pub', 'husk']


# Run the pgrep command to get the process IDs for the specified names
pgrep_pids = []
for pgrep_name in pgrep_names:
    pgrep_cmd = ['pgrep', pgrep_name]
    pgrep_proc = subprocess.run(pgrep_cmd, stdout=subprocess.PIPE, universal_newlines=True)
    pgrep_output = pgrep_proc.stdout.strip().split('\n')
    pgrep_pids += [pid for pid in pgrep_output]

# Remove any duplicate PIDs
pgrep_pids = list(set(pgrep_pids))

pgrep_pids = list(filter(bool, pgrep_pids))

pgrep_pids = [int(x) for x in pgrep_pids]
print(pgrep_pids)


# Build the top command
top_cmd = ['top', '-b', '-n', '1000', '-d', '1']
if pgrep_pids:
    top_cmd += ['-p', ','.join(str(pid) for pid in pgrep_pids)]

# Run the top command as a subprocess and print its output in real-time
top_proc = subprocess.Popen(top_cmd, stdout=subprocess.PIPE, universal_newlines=True)

# Parse the output of the top command and save it to a CSV file
with open('output2.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'S', '%CPU', '%MEM', 'TIME+', 'COMMAND'])
    for line in iter(top_proc.stdout.readline, ''):
        if not line.strip() or line.startswith('top'):
            continue
        row = [x.strip() for x in line.split() if x.strip()]
        if len(row) == 12 and row[0].isdigit() and int(row[0]) in pgrep_pids:
            csvwriter.writerow(row)

# Read the input CSV file
with open('output2.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)

# Compute the total cost for each row and add it as a new column
for row in rows:
    CPU = float(row[8])
    MEM = float(row[9])
    Energy = CPU * MEM/1000
    row.append(Energy)

# Write the output CSV file
with open('output2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers + ['Energy'])
    for row in rows:
        writer.writerow(row)
