import unittest
import matplotlib.dates as mdates

from unittest.mock import patch, MagicMock
from datetime import datetime, time
from openstoxlify.models import PlotType
from openstoxlify.draw import draw
from openstoxlify.fetch import fetch
from openstoxlify.output import output
from openstoxlify.plotter import PLOT_DATA


class TestDrawFunction(unittest.TestCase):
    @patch("matplotlib.pyplot.show")  # Mocking `show` to prevent actual rendering
    @patch("matplotlib.axes.Axes.plot")  # ✅ Mocking `plot` at the correct level
    @patch("matplotlib.axes.Axes.bar")  # ✅ Mocking `bar` at the correct level
    @patch("matplotlib.pyplot.fill_between")
    @patch("matplotlib.pyplot.vlines")
    def test_draw(self, mock_vlines, mock_fill_between, mock_bar, mock_plot, mock_show):
        """Test the draw function to ensure that plotting methods are called correctly."""

        # Simulate adding data to PLOT_DATA for different plot types
        timestamp = datetime(2025, 3, 26, 0, 0, 0)
        PLOT_DATA[PlotType.HISTOGRAM] = [
            {"label": "histogram", "data": [{"timestamp": timestamp, "value": 100}]}
        ]
        PLOT_DATA[PlotType.LINE] = [
            {"label": "line", "data": [{"timestamp": timestamp, "value": 200}]}
        ]
        PLOT_DATA[PlotType.AREA] = [
            {"label": "area", "data": [{"timestamp": timestamp, "value": 300}]}
        ]
        PLOT_DATA[PlotType.CANDLESTICK] = [
            {
                "label": "candlestick",
                "data": [
                    {
                        "timestamp": timestamp,
                        "open": 10,
                        "high": 15,
                        "low": 5,
                        "close": 12,
                    }
                ],
            }
        ]

        # Call the draw function
        draw()

        expected_timestamp = mdates.date2num(datetime(2025, 3, 26, 0, 0, 0))

        mock_plot.assert_called_with(
            [expected_timestamp], [200], label="line", color="green", lw=2
        )

        # Assert histogram bar is drawn
        mock_bar.assert_called_with(
            expected_timestamp, 100, label="histogram", color="blue", width=0.5
        )


if __name__ == "__main__":
    unittest.main()
