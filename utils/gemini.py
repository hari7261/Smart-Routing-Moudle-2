import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def get_ai_suggestions(context):
    if not GEMINI_API_KEY:
        return {
            "recommended_speed_kmh": 80,
            "throttle_advice": "Maintain steady throttle for fuel efficiency",
            "terrain_advice": "Adjust speed based on road conditions"
        }
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"""
        Analyze this driving scenario and provide concise, friendly recommendations:
        - Route: {context['route']['distance_km']} km, about {context['route']['duration_min']:.1f} minutes
        - Weather: {context['weather']['conditions']} and {context['weather']['temp_c']}°C
        - Vehicle: {context['vehicle']['fuel_type']} ({context['vehicle']['weight_kg']} kg)

        Give me brief, friendly driving tips (1-2 sentences each):
        - recommended_speed_kmh: Just the number (e.g., 85)
        - throttle_advice: Brief advice about acceleration and fuel efficiency
        - terrain_advice: Short tips about road conditions and safety
        - safety_message: One encouraging safety reminder
        - extra_tips: Quick comfort or entertainment suggestion

        Output as JSON only. Keep all text values concise and friendly.
        """
        
        response = model.generate_content(prompt)
        # Try to extract the actual JSON from Gemini's response
        raw = None
        if hasattr(response, 'candidates') and response.candidates and hasattr(response.candidates[0], 'content'):
            parts = getattr(response.candidates[0].content, 'parts', None)
            if parts and isinstance(parts, list) and len(parts) > 0:
                raw = parts[0]
        if not raw:
            raw = getattr(response, 'text', None) or str(response)
        try:
            # Remove markdown code block markers if present
            if isinstance(raw, str):
                raw = raw.strip()
                if raw.startswith('```json'):
                    raw = raw[7:]
                if raw.startswith('```'):
                    raw = raw[3:]
                if raw.endswith('```'):
                    raw = raw[:-3]
                raw = raw.strip()
            result = json.loads(raw)
            # If result is a string (Gemini double-encodes), parse again
            if isinstance(result, str):
                result = json.loads(result)
            return result
        except Exception as json_err:
            print(f"Gemini API did not return valid JSON. Raw response: {raw}")
            return {
                "recommended_speed_kmh": 80,
                "throttle_advice": "Maintain steady throttle for fuel efficiency",
                "terrain_advice": "Adjust speed based on road conditions",
                "safety_message": "Drive safe and enjoy your journey!",
                "extra_tips": "Bring your favorite playlist and some snacks for the road!"
            }
    except Exception as e:
        print(f"Gemini API error: {e}")
        return {
            "recommended_speed_kmh": 80,
            "throttle_advice": "Maintain steady throttle for fuel efficiency",
            "terrain_advice": "Adjust speed based on road conditions"
        }