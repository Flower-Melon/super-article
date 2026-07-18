from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm


columns = ["Simple", "Normal", "Hard", "Expert"]
rows = ["w/o Validation", "w/o Memory", "w/o Runtime Replanning"]

# Score change relative to the full DeepSeek V4 Pro configuration.
delta = np.array(
    [
        [-2.151, -2.329, -3.802, -2.0553],
        [-1.970, -0.690, -9.675, -15.4533],
        [-0.209, 0.512, -23.169, -24.5743],
    ]
)

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 11,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
    }
)

# Negative changes are red, values near zero are neutral, and improvements are green.
cmap = LinearSegmentedColormap.from_list(
    "ablation_delta", ["#A94442", "#E6A39A", "#F7F7F7", "#B8D9C2", "#4B9B78"]
)
norm = TwoSlopeNorm(vmin=-25, vcenter=0, vmax=5)

fig, ax = plt.subplots(figsize=(8.8, 3.7))
image = ax.imshow(delta, cmap=cmap, norm=norm, aspect="auto")

ax.set_xticks(range(len(columns)), columns)
ax.set_yticks(range(len(rows)), rows)
ax.set_xlabel("Difficulty Levels")

# Thin white separators keep the matrix readable without heavy cell borders.
ax.set_xticks(np.arange(-0.5, len(columns), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(rows), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=2)
ax.tick_params(which="minor", bottom=False, left=False)
ax.tick_params(axis="both", length=0)

for i in range(delta.shape[0]):
    for j in range(delta.shape[1]):
        value = delta[i, j]
        color = "white" if value <= -12 else "#222222"
        ax.text(
            j,
            i,
            f"{value:+.2f}",
            ha="center",
            va="center",
            color=color,
            fontsize=12,
            fontweight="bold" if abs(value) >= 9 else "normal",
        )

for spine in ax.spines.values():
    spine.set_visible(False)

colorbar = fig.colorbar(image, ax=ax, fraction=0.035, pad=0.035)
colorbar.set_label(r"Score change relative to Full ($\Delta S$)", rotation=270, labelpad=18)
colorbar.outline.set_visible(False)
colorbar.set_ticks([-25, -20, -15, -10, -5, 0, 5])

fig.tight_layout()
output = Path(__file__).resolve().parents[1] / "figures" / "ablation-score-delta-heatmap.png"
fig.savefig(output, dpi=300, bbox_inches="tight", facecolor="white")
plt.close(fig)
