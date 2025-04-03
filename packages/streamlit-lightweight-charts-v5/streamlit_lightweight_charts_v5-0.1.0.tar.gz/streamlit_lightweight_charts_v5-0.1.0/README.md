# Streamlit Lightweight Charts v5

A Streamlit component that integrates TradingView's Lightweight Charts v5 library, providing interactive financial charts with multi-pane support for technical analysis.

## Overview

Streamlit Lightweight Charts v5 is built around version 5 of the TradingView Lightweight Charts library, which introduces powerful multi-pane capabilities perfect for technical analysis. This component allows you to create professional-grade financial charts with multiple indicators stacked vertically, similar to popular trading platforms.

Key features:

- Multi-pane chart layouts for price and indicators
- Customizable themes and styles
- Technical indicators (RSI, MACD, Volume, Williams %R)
- Advanced overlay indicators (AVWAP, Pivot Points)
- Yield curve visualization
- Screenshot functionality

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/locupleto/streamlit-lightweight-charts-v5.git --force-reinstall
```

## Quick Start

```python
import streamlit as st
from lightweight_charts_v5 import lightweight_charts_v5_component

# Create a simple chart
result = lightweight_charts_v5_component(
    name="My Chart",
    charts=[{
        "chart": {"layout": {"background": {"color": "#FFFFFF"}}},
        "series": [{
            "type": "Line",
            "data": [
                {"time": "2023-01-01", "value": 100},
                {"time": "2023-01-02", "value": 120},
                {"time": "2023-01-03", "value": 110}
            ],
            "options": {"color": "#2962FF"}
        }],
        "height": 300
    }],
    height=300
)
```
## Demo Application

The package includes a demo application in the chart_demo.py module that showcases:

- Stock chart visualization with multiple indicators
- Theme customization (Light, Dark, Black, Custom)
- Different price chart styles (Candlestick, Bar, Line)
- Technical indicators in separate panes
- Overlay indicators to price charts
- Yield curve visualization
- Screenshot functionality
- Creating markers for significant points such as Buy-/Sell-points
- Implementing custom themes

## Test the Demo Application

```bash
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/locupleto/streamlit-lightweight-charts-v5.git --force-reinstall
pip install streamlit
pip install yfinance
```

Create a simple Python script file:
```python
from lightweight_charts_v5.chart_demo import main

if __name__ == "__main__":
    main()
```

## License
