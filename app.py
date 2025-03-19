# Import Flask
from flask import Flask, jsonify

# Import character functions from our functions file
from rick_morty_characters import get_all_characters, filter_characters

# Create Flask app
app = Flask(__name__)

# Storage cache to keep the characters
_characters_cache = None

# Helper function to get characters from cache or API
def get_cached_characters():
    """
    Checks if characters are cached, and if not, fetches them from the API.
    """
    # Use the cache created above
    global _characters_cache
    
    # If our cache is empty...
    if _characters_cache is None:
        # Get all characters
        print("Getting new characters from the API...")
        all_characters = get_all_characters()
        # Filter the cahracters
        _characters_cache = filter_characters(all_characters)
    
    # Return the cache
    return _characters_cache

# HealthCheck route
@app.route('/healthcheck')
def healthcheck():
    """
    Checks if the service is healthy.
    """
    return jsonify({"status": "healthy", "message": "The service is running!"})

# Present the characters route
@app.route('/characters')
def get_characters():
    """
    Returns all live human characters from Earth.
    """
    try:
        # Try to get the characters
        characters = get_cached_characters()
        
        # Return in JSON format
        return jsonify({
            "status": "successful",
            "message": "All the live human characters from Earth!",
            "count": len(characters),
            "characters": characters
        })
    except Exception as e:
        # Present the error
        return jsonify({
            "status": "Oh no!",
            "message": f"Error: {str(e)}"
        }), 500

# Start the server if this file is run directly
if __name__ == '__main__':
    # Start the server
    print("Starting the server...")
    print("URLs for details:")
    print("- http://localhost:5000/healthcheck")
    print("- http://localhost:5000/characters")
    app.run(host='0.0.0.0', port=5000)