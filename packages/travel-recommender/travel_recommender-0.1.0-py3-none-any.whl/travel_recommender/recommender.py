# recommender.py
import os
import google.generativeai as genai
import json

class TravelRecommender:
    def __init__(self, api_key=None):
        """
        Initialize the TravelRecommender with a Google API key.
        
        Args:
            api_key (str, optional): Google API key. If not provided, will try to get from environment variable.
        """
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API key must be provided or set as GOOGLE_API_KEY environment variable")
        
        # Configure the Gemini API
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    def get_recommendations(self, location, recommendation_type="both", num_results=3):
        """
        Get travel recommendations based on location.
        
        Args:
            location (str): City name or coordinates (lat,long)
            recommendation_type (str): Type of recommendations - "hotels", "attractions", or "both"
            num_results (int): Number of recommendations to return
            
        Returns:
            dict: Dictionary containing recommendations
        """
        # Determine if location is coordinates or city name
        if isinstance(location, tuple) or ("," in location and any(c.isdigit() for c in location)):
            prompt = f"Give me recommendations for a traveler at coordinates {location}."
        else:
            prompt = f"Give me recommendations for a traveler visiting {location}."
            
        # Add specific request based on recommendation type
        if recommendation_type.lower() == "hotels":
            prompt += f" List {num_results} hotel recommendations with brief descriptions."
        elif recommendation_type.lower() == "attractions":
            prompt += f" List {num_results} attraction recommendations with brief descriptions."
        else:
            prompt += f" List {num_results} hotel recommendations and {num_results} attraction recommendations with brief descriptions."
        
        # Add formatting instructions
        prompt += " Format the response as a JSON object with 'hotels' and/or 'attractions' as keys, each containing an array of objects with 'name', 'description', and 'rating' fields. the resultant string should be valid json"
        
        # System prompt
        system_prompt = "You are a helpful travel assistant that provides hotel and attraction recommendations in JSON format."
        
        # Call Gemini API
        response = self.model.generate_content(
            [system_prompt, prompt]
        )
        
        # Process and return the response
        try:
            # Extract JSON from the response
            content = response.text
            
            
            # Sometimes Gemini might wrap the JSON in markdown code blocks
            # if "```" in content:
            content = content.split("```json")[1].split("```")[0]
            # elif "```" in content:
            #     content = content.split("``````")[0].strip()
            # print((str(content)))
            json_str = content.strip()
            print(json_str)
            # Convert string to JSON
            parsed_json = json.loads(json_str)

            result = parsed_json
            return result
        except Exception as e:
            return {"error": f"Failed to parse recommendations: {str(e)}"}
