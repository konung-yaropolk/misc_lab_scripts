import os
import numpy as np
import matplotlib.pyplot as plt
import tifffile

def get_prefix_groups(names, min_len=4):
    """
    Return dict mapping prefix -> list of folder names sharing it.
    Only prefixes >= min_len are considered.
    """
    groups = {}
    for name in names:
        for other in names:
            if name == other:
                continue
            # Find common prefix
            i = 0
            while i < len(name) and i < len(other) and name[i] == other[i]:
                i += 1
            if i >= min_len:
                prefix = name[:i]
                if prefix not in groups:
                    groups[prefix] = set()
                groups[prefix].update([name, other])
    # Convert sets to lists
    return {k: list(v) for k, v in groups.items()}

def build_histogram_cdf(hist_alpha=0.5):
    # Directory where this script is located
    root_folder = os.path.dirname(os.path.abspath(__file__))

    # List subfolders
    subfolders = [f for f in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, f))]

    # Find groups with shared prefix >=4 chars
    prefix_groups = get_prefix_groups(subfolders, min_len=4)
    prefix_groups = {key: sorted(value) for key, value in prefix_groups.items()}
    grouped = set([f for g in prefix_groups.values() for f in g])

    # Map folder -> pixels
    folder_pixels = {}

    for sub in subfolders:
        sub_path = os.path.join(root_folder, sub)
        tiffs = [
            os.path.join(sub_path, f)
            for f in os.listdir(sub_path)
            if f.lower().endswith((".tif", ".tiff"))
        ]
        if not tiffs:
            print(f"No TIFFs found in {sub}")
            continue

        all_pixels = []
        for t in tiffs:
            img = tifffile.imread(t)
            all_pixels.append(img.flatten())
        all_pixels = np.concatenate(all_pixels)
        all_pixels = all_pixels[all_pixels > 0]  # exclude zeros
        folder_pixels[sub] = all_pixels


    # -------------------------
    # Plot grouped folders (same prefix) together
    # -------------------------
    for prefix, group in prefix_groups.items():
        fig, ax1 = plt.subplots(dpi=90, figsize=(6, 4))
        plt.style.use('default')

        ax2 = ax1.twinx()
        colors = plt.cm.Set1.colors
        # colors = ['C3', 'C0', 'C2', 'C1', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
        for i, sub in enumerate(group):
            pixels = folder_pixels[sub]
            # Histogram
            ax1.hist(pixels, bins=1024, alpha=hist_alpha, color=colors[i % len(colors)], label=f"{sub}")
            # CDF
            sorted_vals = np.sort(pixels)
            cdf = np.linspace(0, 1, len(sorted_vals))
            ax2.plot(sorted_vals, cdf, color=colors[i % len(colors)], linewidth=1.5, alpha=hist_alpha) # label=f"{sub}"

        ax1.set_xlabel("Resp. Relative Intensity")
        ax1.set_xlim(0, 3)
        # ax1.set_ylabel("Count")
        ax2.set_ylabel("Cumulative Probability")
        plt.title(f"Responses Distribution comparison: {prefix}")

        # Combine legends
        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax1.legend(h1 + h2, l1 + l2, loc="lower right", fontsize=8)

        fig.tight_layout()
        out_path = os.path.join(root_folder, f"{prefix}_comparison.png")
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        print(f"Saved grouped comparison: {out_path}")

    # -------------------------
    # Plot individual folders not in any group
    # -------------------------
    for sub in subfolders:
        if sub in grouped:
            continue
        pixels = folder_pixels.get(sub)
        if pixels is None:
            continue
        sorted_vals = np.sort(pixels)
        cdf = np.linspace(0, 1, len(sorted_vals))

        fig, ax1 = plt.subplots(dpi=90, figsize=(4, 3))
        ax2 = ax1.twinx()
        ax1.hist(pixels, bins=1024, alpha=hist_alpha, label=f"{sub} hist")
        ax2.plot(sorted_vals, cdf, color="C1", label=f"{sub} CDF", linewidth=1.5)

        ax1.set_xlabel("Resp. Relative Intensity")
        ax1.set_xlim(0, 3)
        ax1.set_ylabel("Count")
        ax2.set_ylabel("Cumulative Probability")
        plt.title(f"Histogram + CDF: {sub}")

        # Combine legends
        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=8)

        fig.tight_layout()
        out_path = os.path.join(root_folder, f"{sub}_hist.png")
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    build_histogram_cdf(hist_alpha=0.5)
