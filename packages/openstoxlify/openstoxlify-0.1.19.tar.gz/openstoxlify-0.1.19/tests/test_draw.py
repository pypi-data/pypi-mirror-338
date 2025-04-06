import unittest
import matplotlib.dates as mdates

from unittest.mock import patch, ANY
from datetime import datetime
from openstoxlify.models import PlotType, ActionType
from openstoxlify.draw import draw
from openstoxlify.plotter import PLOT_DATA
from openstoxlify.fetch import CANDLESTICK_DATA
from openstoxlify.strategy import STRATEGY_DATA


class TestDrawFunction(unittest.TestCase):
    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.axes.Axes.arrow")  # Mock arrow
    @patch("matplotlib.axes.Axes.vlines")
    @patch("matplotlib.axes.Axes.plot")
    @patch("matplotlib.axes.Axes.bar")
    @patch("matplotlib.axes.Axes.fill_between")
    def test_draw(
        self, mock_fill_between, mock_bar, mock_plot, mock_vlines, mock_arrow, mock_show
    ):
        """Test the draw function to ensure all plotting methods, including arrows, are called."""

        timestamp = datetime(2025, 3, 26, 0, 0, 0)
        expected_timestamp = mdates.date2num(timestamp)

        # Populate PLOT_DATA with test values
        PLOT_DATA[PlotType.HISTOGRAM] = [
            {"label": "histogram", "data": [{"timestamp": timestamp, "value": 100}]}
        ]
        PLOT_DATA[PlotType.LINE] = [
            {"label": "line", "data": [{"timestamp": timestamp, "value": 200}]}
        ]
        PLOT_DATA[PlotType.AREA] = [
            {"label": "area", "data": [{"timestamp": timestamp, "value": 300}]}
        ]

        # Populate CANDLESTICK_DATA with test values
        CANDLESTICK_DATA.append(
            {"timestamp": timestamp, "open": 100, "close": 200, "low": 50, "high": 250}
        )

        STRATEGY_DATA["strategy"] = []
        STRATEGY_DATA["strategy"].append(
            {"timestamp": timestamp, "value": ActionType.LONG}
        )

        draw()

        # Verify plot, bar, and fill_between calls
        mock_plot.assert_called_with(
            [expected_timestamp], [200], label="line", color=ANY, lw=2
        )
        mock_bar.assert_called_with(
            [expected_timestamp],
            [100],
            label="histogram",
            color=ANY,
            width=0.5,
            alpha=0.6,
        )
        mock_fill_between.assert_called_with(
            [expected_timestamp], [300], label="area", color=ANY, alpha=0.3
        )

        # Verify arrows are drawn
        mock_arrow.assert_called()  # Ensures at least one arrow is drawn


if __name__ == "__main__":
    unittest.main()
