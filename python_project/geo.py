from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current date and time
    now = datetime.datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Get the user's IP address
    ip_address = request.remote_addr
    
    # You can use a geolocation API to get the location based on IP address
    # For example, you can use freegeoip.app
    # Replace 'your_api_key' with your actual API key
    # You can get your API key by signing up at https://freegeoip.app/signup
    # api_url = f"http://api.ipstack.com/{ip_address}?access_key=your_api_key"
    # response = requests.get(api_url)
    # data = response.json()
    # location = f"{data['city']}, {data['region_name']}, {data['country_name']}"
    # location = data['city']
    location = "London"  # Replace this with the location obtained from the API
    
    return f"Current date and time: {current_date_time}<br>Current location: {location}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
