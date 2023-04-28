import csv
import subprocess

# Define the pgrep name to filter by
pgrep_name = 'turtle'

# Run the pgrep command to get the process IDs for the specified name
pgrep_cmd = ['pgrep', pgrep_name]
pgrep_proc = subprocess.run(pgrep_cmd, stdout=subprocess.PIPE, universal_newlines=True)
pgrep_output = pgrep_proc.stdout.strip().split('\n')
pgrep_pids = [int(pid) for pid in pgrep_output]
print(pgrep_pids)
# Run the top command as a subprocess for the specified PIDs and print its output in real-time
top_cmd = ['top', '-b', '-n', '1000', '-d', '1', '-p', ','.join(str(pid) for pid in pgrep_pids)]
top_proc = subprocess.Popen(top_cmd, stdout=subprocess.PIPE, universal_newlines=True)
print('top_proc', top_proc)
# Parse the output of the top command and save it to a CSV file
with open('output.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'S', '%CPU', '%MEM', 'TIME+', 'COMMAND'])
    for line in iter(top_proc.stdout.readline, ''):
        if not line.strip() or line.startswith('top'):
            continue
        row = [x.strip() for x in line.split() if x.strip()]
        if len(row) == 12 and row[0].isdigit() and int(row[0]) in pgrep_pids:
            csvwriter.writerow(row)

# Read the input CSV file
with open('output.csv', 'r') as f:
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
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers + ['Energy'])
    for row in rows:
        writer.writerow(row)