import psutil
import time

# Run the Python program
start_time = time.time()
# Replace 'your_python_program.py' with the name of your Python program
# and 'your_program_args' with any arguments that it requires
process = psutil.Popen(['python3', 'main-2.py', ''])

end_time = time.time()

# Calculate the time taken to run the program
time_taken = end_time - start_time
print(time_taken)
# Get the CPU and memory usage of the process
try:
    pid = process.pid
    cpu_usage = psutil.Process(pid).cpu_percent(interval=time_taken)
    mem_usage = psutil.Process(pid).memory_info().rss

    # Estimate the energy consumption
    energy_consumption = cpu_usage * (mem_usage/1000)

    # Display the estimated energy consumption
    print(f"Estimated energy consumption of the Python program: {energy_consumption:.2f}")
except psutil.NoSuchProcess:
    print("The process has already terminated.")

# Display the estimated energy consumption
print(f"Estimated energy consumption of the Python program: {energy_consumption:.2f}")


