# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

World Time Agent is a Python CLI application that provides current time information for any city worldwide using geocoding and timezone lookup services.

## Development Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Or with a virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

### Running the Application
```bash
# Run with city name as argument
python time_agent.py "New York"
python time_agent.py "Tokyo"

# Run in interactive mode
python time_agent.py
```

### Testing
```bash
# Run the application with various cities to test functionality
python time_agent.py "Paris"
python time_agent.py "Los Angeles"
python time_agent.py "Sydney"
```

## Architecture

### Core Components

**WorldTimeAgent Class** (`time_agent.py`)
- Single-class architecture implementing the time lookup functionality
- Uses composition pattern with external services (geopy, timezonefinder, pytz)
- Returns structured dictionaries for both success and error cases

**Service Dependencies**
1. **geopy.Nominatim**: Geocodes city names to latitude/longitude coordinates
2. **timezonefinder.TimezoneFinder**: Maps coordinates to IANA timezone identifiers
3. **pytz**: Handles timezone-aware datetime conversion

**Data Flow**
```
City Name → Geocoding (geopy) → Coordinates → Timezone Lookup (timezonefinder) 
→ Timezone Object (pytz) → Current Time → Formatted Response
```

### Key Methods

- `get_time_for_city(city_name)`: Main business logic method that orchestrates the lookup pipeline and returns structured results
- `format_response(result)`: Presentation layer that converts result dictionaries to user-friendly output with emoji indicators

### Error Handling

The application uses a consistent error response pattern where all methods return dictionaries with a `success` boolean flag. Failed operations include descriptive error messages in the `error` field rather than raising exceptions to the user.

## Code Style

- Uses type hints for function parameters and return values
- Docstrings follow Google/NumPy style with Args and Returns sections
- Emoji indicators in user-facing output (🌍 for city, 🕐 for time, etc.)
- Command-line interface supports both argument-based and interactive modes
