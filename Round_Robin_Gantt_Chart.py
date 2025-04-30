import matplotlib.pyplot as plt

# Sample Gantt chart data
processes = [
    ("P1", 0, 4),
    ("P2", 4, 8),
    ("P3", 8, 12),
    ("P4", 12, 16),
    ("P1", 16, 18),
    ("P2", 18, 20)
]

# Colors for each process (can be customized)
colors = {
    "P1": "skyblue",
    "P2": "lightgreen",
    "P3": "salmon",
    "P4": "plum"
}

fig, ax = plt.subplots(figsize=(10, 2))

for i, (proc, start, end) in enumerate(processes):
    ax.barh(0, end - start, left=start, color=colors[proc], edgecolor='black')
    ax.text((start + end) / 2, 0, proc, ha='center', va='center', color='black')

# Aesthetic setup
ax.set_yticks([])
ax.set_xlim(0, max(end for _, _, end in processes) + 1)
ax.set_xlabel("Time (ms)")
ax.set_title("Gantt Chart - Round Robin Scheduling (q=4ms)")
plt.tight_layout()
plt.show()
