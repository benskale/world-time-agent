#!/usr/bin/env python3
"""
World Time Agent - Get current time for any city in the world
"""

import sys
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


class WorldTimeAgent:
    """AI agent that provides current time for any city worldwide."""
    
    def __init__(self):
        self.geolocator = Nominatim(user_agent="world-time-agent")
        self.tf = TimezoneFinder()
    
    def get_time_for_city(self, city_name: str) -> dict:
        """
        Get the current time for a given city.
        
        Args:
            city_name: Name of the city to lookup
            
        Returns:
            Dictionary with time information or error details
        """
        try:
            # Geocode the city name to get coordinates
            location = self.geolocator.geocode(city_name, timeout=10)
            
            if not location:
                return {
                    "success": False,
                    "error": f"Could not find city: {city_name}"
                }
            
            # Get timezone from coordinates
            timezone_str = self.tf.timezone_at(
                lat=location.latitude, 
                lng=location.longitude
            )
            
            if not timezone_str:
                return {
                    "success": False,
                    "error": f"Could not determine timezone for {city_name}"
                }
            
            # Get current time in that timezone
            timezone = pytz.timezone(timezone_str)
            current_time = datetime.now(timezone)
            
            return {
                "success": True,
                "city": location.address.split(',')[0],
                "country": location.address.split(',')[-1].strip(),
                "timezone": timezone_str,
                "timezone_abbr": current_time.strftime('%Z'),
                "time": current_time.strftime('%H:%M:%S'),
                "date": current_time.strftime('%Y-%m-%d'),
                "full_datetime": current_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
                "coordinates": {
                    "latitude": location.latitude,
                    "longitude": location.longitude
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error processing request: {str(e)}"
            }
    
    def format_response(self, result: dict) -> str:
        """Format the agent's response for display."""
        if not result["success"]:
            return f"❌ {result['error']}"
        
        return f"""
🌍 {result['city']}, {result['country']}
🕐 Current time: {result['time']} ({result['timezone_abbr']})
📅 Date: {result['date']}
🌐 Timezone: {result['timezone']}
📍 Coordinates: {result['coordinates']['latitude']:.4f}, {result['coordinates']['longitude']:.4f}
        """.strip()


def main():
    """Main CLI interface for the World Time Agent."""
    agent = WorldTimeAgent()
    
    # Check if city name provided as argument
    if len(sys.argv) > 1:
        city_name = ' '.join(sys.argv[1:])
        result = agent.get_time_for_city(city_name)
        print(agent.format_response(result))
    else:
        # Interactive mode
        print("🤖 World Time Agent")
        print("=" * 50)
        print("Enter city names to get their current time.")
        print("Type 'quit' or 'exit' to stop.\n")
        
        while True:
            try:
                city_name = input("Enter city name: ").strip()
                
                if city_name.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye! 👋")
                    break
                
                if not city_name:
                    continue
                
                result = agent.get_time_for_city(city_name)
                print(agent.format_response(result))
                print()
                
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except EOFError:
                break


if __name__ == "__main__":
    main()
