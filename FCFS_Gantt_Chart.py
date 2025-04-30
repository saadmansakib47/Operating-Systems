import matplotlib.pyplot as plt

# FCFS Gantt chart timeline data
processes = [
    ("P1", 0, 5),
    ("P2", 5, 8),
    ("P3", 8, 16),
    ("P4", 16, 22)
]

# Assign colors to each process
colors = {
    "P1": "skyblue",
    "P2": "lightgreen",
    "P3": "salmon",
    "P4": "plum"
}

# Create the figure
fig, ax = plt.subplots(figsize=(10, 2))

# Draw each bar (process execution slice)
for i, (proc, start, end) in enumerate(processes):
    ax.barh(0, end - start, left=start, color=colors[proc], edgecolor='black')
    ax.text((start + end) / 2, 0, proc, ha='center', va='center', color='black')

# Formatting
ax.set_yticks([])
ax.set_xlim(0, max(end for _, _, end in processes) + 1)
ax.set_xlabel("Time (ms)")
ax.set_title("Gantt Chart - FCFS Scheduling")
plt.tight_layout()
plt.show()
