import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime
from .models import PlotType, ActionType
from .plotter import PLOT_DATA
from .fetch import CANDLESTICK_DATA
from .strategy import STRATEGY_DATA

COLOR_PALETTE = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]

ARROW_COLORS = {
    ActionType.LONG: "blue",
    ActionType.SHORT: "red",
}

ASSIGNED_COLORS = {}


def get_color(label):
    """Assign a consistent random color for each label."""
    if label not in ASSIGNED_COLORS:
        ASSIGNED_COLORS[label] = random.choice(COLOR_PALETTE)
    return ASSIGNED_COLORS[label]


def draw():
    """Draw all charts from the PLOT_DATA and CANDLESTICK_DATA."""
    fig, ax = plt.subplots(figsize=(12, 6))

    def convert_timestamp(timestamp):
        if isinstance(timestamp, str):
            return mdates.date2num(datetime.fromisoformat(timestamp))
        return mdates.date2num(timestamp)

    plotted_histograms = set()
    for plot in PLOT_DATA.get(PlotType.HISTOGRAM, []):
        timestamps = [convert_timestamp(item["timestamp"]) for item in plot["data"]]
        values = [item["value"] for item in plot["data"]]

        if len(timestamps) > 1:
            bar_width = (max(timestamps) - min(timestamps)) / len(timestamps) * 0.8
        else:
            bar_width = 0.5

        label = (
            plot["label"] if plot["label"] not in plotted_histograms else "_nolegend_"
        )
        plotted_histograms.add(plot["label"])

        ax.bar(
            timestamps,
            values,
            label=label,
            color=get_color(plot["label"]),
            width=bar_width,
            alpha=0.6,
        )

    for plot in PLOT_DATA.get(PlotType.LINE, []):
        timestamps = [convert_timestamp(item["timestamp"]) for item in plot["data"]]
        values = [item["value"] for item in plot["data"]]
        ax.plot(
            timestamps,
            values,
            label=plot["label"],
            color=get_color(plot["label"]),
            lw=2,
        )

    for plot in PLOT_DATA.get(PlotType.AREA, []):
        timestamps = [convert_timestamp(item["timestamp"]) for item in plot["data"]]
        values = [item["value"] for item in plot["data"]]
        ax.fill_between(
            timestamps,
            values,
            label=plot["label"],
            color=get_color(plot["label"]),
            alpha=0.3,
        )

    candle_lut = {}
    for item in CANDLESTICK_DATA:
        timestamp_numeric = convert_timestamp(item["timestamp"])
        color = "green" if item["close"] > item["open"] else "red"
        ax.vlines(timestamp_numeric, item["low"], item["high"], color=color, lw=1)
        ax.vlines(timestamp_numeric, item["open"], item["close"], color=color, lw=4)
        candle_lut[item["timestamp"]] = (timestamp_numeric, item["high"], item["low"])

    for action in STRATEGY_DATA:
        ts = action["timestamp"]
        action_type = action["value"]
        if action_type == ActionType.HOLD:
            continue

        if ts in candle_lut:
            x, high, low = candle_lut[ts]
            y = high + 1 if action_type == ActionType.LONG else low - 1
            dy = 0.5 if action_type == ActionType.LONG else -0.5

            ax.annotate(
                "↑" if action_type == ActionType.LONG else "↓",
                xy=(x, y),
                textcoords="offset points",
                xytext=(0, 0),
                ha="center",
                fontsize=12,
                color=ARROW_COLORS.get(action_type, "black"),
                weight="bold",
            )

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_title("Market Data Visualizations")
    ax.legend()

    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.xticks(rotation=30, ha="right")

    plt.tight_layout()
    plt.show()
