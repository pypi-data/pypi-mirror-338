import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

def plot(
    filepath,
    components=["mx", "my", "mz"],
    title="Magnetization vs Time",
    xlabel="Time (s)",
    ylabel="Magnetization",
    colors=None,
    labels=None,
    grid=True,
    figsize=(10, 6),
    show=True,
    three_d=False
):
    try:
        # Open file manually, read header line
        with open(filepath, 'r') as f:
            header_line = f.readline().lstrip("#").strip()
            column_names = [col.strip().split()[0] for col in header_line.split('\t')]
    
        # Load data with cleaned column names
        df = pd.read_csv(filepath, sep=r'\s+', engine='python', skiprows=1, names=column_names)
        print("✅ Cleaned columns:", df.columns.tolist())
    except Exception as e:
        raise ValueError(f"❌ Failed to load file {filepath}: {e}")

    if three_d:
        title = 'Magnetization dynamics in 3d'
        if all(col in df.columns for col in ["mx", "my", "mz"]):
            fig = plt.figure(figsize=figsize)
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(df["mx"], df["my"], df["mz"], color='blue')
            ax.set_xlabel("Mx")
            ax.set_ylabel("My")
            ax.set_zlabel("Mz")
            ax.set_title(title)
            if grid:
                ax.grid(True)
            if show:
                plt.show()
        else:
            print("⚠️  Cannot plot in 3D. One or more of mx, my, mz not found in columns.")
        return

    # 2D plot path
    time_col = "t"
    time = df[time_col]

    plt.figure(figsize=figsize)

    for i, comp in enumerate(components):
        if comp in df.columns:
            color = colors[i] if colors and i < len(colors) else None
            label = labels[i] if labels and i < len(labels) else comp
            plt.plot(time, df[comp], label=str(label), color=color)
        else:
            print(f"⚠️  Warning: Component '{comp}' not found in columns.")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if grid:
        plt.grid(True)
    plt.legend()
    plt.tight_layout()
    if show:
        plt.show()

