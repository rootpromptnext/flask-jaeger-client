from flask import Flask
import time
import random
import opentracing
from jaeger_client import Config

app = Flask(__name__)

# Configure Jaeger tracer
def init_tracer(service):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
        },
        service_name=service,
    )
    return config.initialize_tracer()

tracer = init_tracer("flask-jaeger-demo")
opentracing.tracer = tracer

@app.route("/")
def home():
    with tracer.start_span("home-span") as span:
        time.sleep(random.uniform(0.2, 1.0))
        return "Welcome to Jaeger Client Demo\n"

@app.route("/hello")
def hello():
    with tracer.start_span("hello-span") as span:
        time.sleep(random.uniform(0.1, 0.8))
        return "Hello Jaeger\n"

@app.route("/error")
def error():
    with tracer.start_span("error-span") as span:
        time.sleep(0.5)
        raise Exception("Something went wrong")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
