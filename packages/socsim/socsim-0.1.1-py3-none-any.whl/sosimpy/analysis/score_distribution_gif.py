import json
import sqlite3
import os
from collections import Counter
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def fetch_agent_table(conn: sqlite3.Connection, iter_idx: int, columns=None):
    """
    Fetch agent data from the AgentLog table for a specific iteration.
    """
    if columns is None:
        columns = ["agent_id", "questionnaire_r"]
    cursor = conn.cursor()
    column_str = ", ".join(columns)
    cursor.execute(f"""
        SELECT {column_str}
        FROM AgentLog
        WHERE iter_idx = ?
    """, (iter_idx,))
    return cursor.fetchall()


def compute_openness_distribution(all_responses, mask):
    """
    From a list of response JSON strings, compute how many agents have each possible score.
    """
    agent_scores = []
    for response in all_responses:
        response = json.loads(response)
        if isinstance(response, list):  # Only proceed if it's a valid list
            # Sum over just the relevant indices
            score = sum(response[m_idx] for m_idx in mask)
            agent_scores.append(score)

    # Count occurrences of each score
    score_counts = Counter(agent_scores)

    # The maximum possible score is len(mask)
    max_score = len(mask)
    # Make an array from 0 .. max_score inclusive
    dist_array = np.array([score_counts.get(s, 0) for s in range(max_score + 1)])
    return dist_array


def update(
        frame_idx,
        bar_container,
        all_distributions,
        max_score,
        pause_frames,
        ax
):
    """
    Update function for FuncAnimation:
      - If 'frame_idx' < actual_iterations, display that iteration's data
      - Otherwise, display the final iteration's distribution
      - After the final iteration, draw the horizontal line + text for the "pause" portion
    """

    # Number of real frames (excluding the pause).
    real_frames = all_distributions.shape[0]  # e.g., len(iter_range)


    # The last real frame is real_frames - 1
    last_frame_idx = real_frames - 1

    # If we're in the final frames, just reuse the last distribution
    if frame_idx >= last_frame_idx:
        frame_idx = last_frame_idx

    dist = all_distributions[frame_idx]
    score_indices = np.arange(dist.size)  # [0, 1, 2, ..., max_score]
    total_agents = dist.sum()
    weighted_sum = np.dot(score_indices, dist)
    mean_score = weighted_sum / total_agents

    # Update bar heights
    for rect, h in zip(bar_container, dist):
        rect.set_height(h)

    # Title labeling
    if frame_idx < last_frame_idx:
        ax.set_title(f"Distribution of Agent Openness Scores - Iteration {frame_idx}")
    else:
        # For final iteration/pause frames
        ax.set_title(f"Distribution of Agent Openness Scores - Iteration {last_frame_idx}")


    for ln in ax.lines:
        ln.remove()
    for txt in ax.texts:
        txt.remove()

    # Place text in top-left corner in Axes coordinates
    ax.text(
        0.05, 0.95,
        f"Mean Agreement Score: {mean_score:.2f}",
        transform=ax.transAxes,
        verticalalignment='top',
        fontsize=10,
        color='green'
    )


def generate_openness_distribution_gif(
        db_path,
        mask_indices,
        iter_range,
        output_path="openness_distribution.gif",
        fps=2,
        pause_frames=10,
):
    """
    Main function to:
    1. Read from the database for each iteration in `iter_range`,
    2. Compute and store the score distribution,
    3. Create a bar chart animation (one frame per iteration + paused end),
    4. Save as a GIF.
    5. Draw a horizontal line + text for the mean score during the paused portion.
    """

    # Collect distributions for each iteration
    all_distributions = []
    max_score = len(mask_indices)  # The highest total possible in mask

    with sqlite3.connect(db_path) as conn:
        for i in iter_range:
            ret = fetch_agent_table(conn, i)
            # ret is a list of (agent_id, response_json)
            # we only need the response_json for distribution
            responses = [row[1] for row in ret]  # row[1] => the questionnaire_r
            dist_array = compute_openness_distribution(responses, mask_indices)
            all_distributions.append(dist_array)

    all_distributions = np.array(all_distributions)  # shape: [num_iters, max_score+1]
    real_frames = len(all_distributions)

    # ---------- Setup the figure and initial bar plot ----------
    fig, ax = plt.subplots(figsize=(8, 5))
    score_range = np.arange(max_score + 1)  # 0..max_score
    # Initial data for iteration 0
    dist_init = all_distributions[0]
    bar_container = ax.bar(score_range, dist_init, tick_label=score_range)

    ax.set_xlabel('Total Agent Openness Score')
    ax.set_ylabel('Number of Agents')
    ax.set_title('Distribution of Agent Openness Scores - Iteration 0')
    ax.set_xticks(score_range)
    ax.set_ylim(0, max(dist_init.max(), 1) * 1.1)  # a bit of headroom

    # ---------- Frame Generation ----------
    # We want to create extra frames for the pause.
    # We'll construct a list of frames: [0, 1, 2, ..., real_frames-1] + repeated final
    frames_list = list(range(real_frames)) + [real_frames - 1] * pause_frames

    # ---------- Create the animation ----------
    ani = FuncAnimation(
        fig,
        update,
        frames=frames_list,  # includes the pause frames
        interval=1000 // fps,  # ms per frame
        repeat=False,
        fargs=(
            bar_container,
            all_distributions,
            max_score,
            pause_frames,
            ax
        )
    )

    # ---------- Save as GIF ----------
    writer = PillowWriter(fps=fps)
    ani.save(output_path, writer=writer, dpi=200)
    plt.close(fig)

    print(f"Saved animation to {output_path}")


# ---------- Usage Example ----------
if __name__ == "__main__":
    # Suppose your database is here:
    db_path = "/home/robert/society-simulation/simulations/2025-02-25 20:09:15.537650/simulation_logs/logs.db"

    # Indices that are related to openness
    OPENNESS_INDICES = [40, 41, 42, 43, 44, 45, 46, 47, 48]

    # Choose which iterations you want to animate (0..N)
    iteration_range = range(0, 100)

    # Example mean score you want to highlight with a horizontal line
    # (You could compute this from the data as well.)

    # Generate the animated distribution GIF
    generate_openness_distribution_gif(
        db_path=db_path,
        mask_indices=OPENNESS_INDICES,
        iter_range=iteration_range,
        output_path="../simulations/2025-02-25 20:09:15.537650/openness_distribution_32_100.gif",
        fps=3,  # 2 frames per second
        pause_frames=15,  # Pause ~15 frames after last iteration
    )
