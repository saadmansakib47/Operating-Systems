import matplotlib.pyplot as plt
import numpy as np

# Algorithms
algorithms = ['FCFS', 'SJF', 'RR (q=4ms)']

# Numeric metrics
avg_waiting_time = [5.75, 5.25, 9.25]
avg_turnaround_time = [11.25, 10.75, 14.75]

# Bar width and positions
x = np.arange(len(algorithms))
bar_width = 0.35

# Create the bar chart
plt.figure(figsize=(8, 5))
plt.bar(x - bar_width/2, avg_waiting_time, width=bar_width, label='Avg Waiting Time (ms)', color='#4caf50')
plt.bar(x + bar_width/2, avg_turnaround_time, width=bar_width, label='Avg Turnaround Time (ms)', color='#2196f3')

# Labels and formatting
plt.xlabel('Scheduling Algorithms')
plt.ylabel('Time (ms)')
plt.title('Performance Comparison of Scheduling Algorithms')
plt.xticks(x, algorithms)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the chart
plt.show()
