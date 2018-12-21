from flask_api import FlaskAPI

# Initialize the application:
app = FlaskAPI(__name__)

# Return a valid response object, list, or dict
# If you're making the API request from a regular client, this will default to a JSON response.
# If you're viewing the API in a browser it defaults to the browsable API HTML.
@app.route('/example/')
def example():
    return {'key': 'value'}
