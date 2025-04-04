# utils.py
import re

def is_valid_coordinates(coords):
    """
    Check if the provided string represents valid coordinates.
    
    Args:
        coords (str): String representation of coordinates
        
    Returns:
        bool: True if valid coordinates, False otherwise
    """
    # Simple regex for lat,long format
    pattern = r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$'
    return bool(re.match(pattern, coords))

def format_recommendations(recommendations):
    """
    Format recommendations for pretty printing.
    
    Args:
        recommendations (dict): Recommendations dictionary
        
    Returns:
        str: Formatted string of recommendations
    """
    result = []
    
    if "hotels" in recommendations:
        result.append("=== HOTEL RECOMMENDATIONS ===")
        for i, hotel in enumerate(recommendations["hotels"], 1):
            result.append(f"{i}. {hotel['name']}")
            if "rating" in hotel:
                result.append(f"   Rating: {hotel['rating']}")
            result.append(f"   {hotel['description']}")
            result.append("")
    
    if "attractions" in recommendations:
        result.append("=== ATTRACTION RECOMMENDATIONS ===")
        for i, attraction in enumerate(recommendations["attractions"], 1):
            result.append(f"{i}. {attraction['name']}")
            if "rating" in attraction:
                result.append(f"   Rating: {attraction['rating']}")
            result.append(f"   {attraction['description']}")
            result.append("")
    
    return "\n".join(result)
