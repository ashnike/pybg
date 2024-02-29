import os  # Import the os module

from flask import Flask, render_template, request
from jinja2.exceptions import TemplateNotFound
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Set the template directory explicitly
app.config['TEMPLATES'] = os.path.join(os.path.dirname(__file__), 'templates')

metrics = PrometheusMetrics(app)


# Define Prometheus metrics
request_count = metrics.counter(
    'flask_app_requests_total', 'Total number of requests served by the app'
)
app_health = metrics.gauge(
    'flask_app_health', 'Health status of the Flask application (1: healthy, 0: unhealthy)'
)

@app.route('/', methods=['GET', 'POST'])
def index():
    heading = "My Flask App"  # Initial heading
    inputs = {}  # Initialize empty dictionary for inputs

    if request.method == 'POST':
        # Process form data here
        for key, value in request.form.items():
            inputs[key] = value
        heading = "Heading with Inputs Added"  # Dynamically update heading

    try:
        return render_template('index.html', heading=heading, inputs=inputs)
    except TemplateNotFound:
        return render_template('error.html', message='Template not found!')

@app.route('/health')
def health_check():
    # Your health check logic goes here
    app_health.set(1)  # Set metric to 1 (healthy)
    return 'App is healthy'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

