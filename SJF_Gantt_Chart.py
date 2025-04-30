import matplotlib.pyplot as plt

# SJF Gantt chart timeline data
processes = [
    ("P2", 0, 3),
    ("P1", 3, 8),
    ("P4", 8, 14),
    ("P3", 14, 22)
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
ax.set_title("Gantt Chart - SJF Scheduling")
plt.tight_layout()
plt.show()
