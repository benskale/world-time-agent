# World Time Agent

An AI agent that tells you the current time in any city around the world.

## Features

- Get current time for any city worldwide
- Supports timezone lookup by city name
- Simple command-line interface
- Handles timezone conversions automatically

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the agent from the command line:

```bash
python time_agent.py "New York"
python time_agent.py "Tokyo"
python time_agent.py "London"
python time_agent.py "Sydney"
```

Or use it interactively:

```bash
python time_agent.py
```

Then enter city names when prompted.

## How It Works

The agent uses:
- `geopy` for geocoding city names to coordinates
- `timezonefinder` to determine the timezone from coordinates
- `pytz` for accurate timezone handling and time conversion

## Examples

```bash
$ python time_agent.py "Paris"
The current time in Paris is: 23:51:14 (CET)

$ python time_agent.py "Los Angeles"
The current time in Los Angeles is: 14:51:14 (PST)
```
