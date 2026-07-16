# Flask Jaeger Client

A simple Python Flask application instrumented with the **Jaeger Python Client** for learning distributed tracing.

## Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
└── README.md
```

---

# Prerequisites

- Python 3.12+
- Docker
- Kubernetes (MicroK8s)
- Jaeger installed in Kubernetes

---

# Install Python Dependencies

```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

# Run the Application

```bash
python3 app.py
```

Application URL

```
http://localhost:5000
```

Test

```bash
curl http://localhost:5000

curl http://localhost:5000/hello

curl http://localhost:5000/error
```

---

# Run Using Docker

Build the image

```bash
docker build -t flask-jaeger-client:v1 .
```

Run the container

```bash
docker run -d \
--name flask-jaeger-client \
-p 5000:5000 \
-e JAEGER_AGENT_HOST=<JAEGER_HOST> \
-e JAEGER_AGENT_PORT=6831 \
flask-jaeger-client:v1
```

Example

```bash
docker run -d \
--name flask-jaeger-client \
-p 5000:5000 \
-e JAEGER_AGENT_HOST=192.168.1.10 \
-e JAEGER_AGENT_PORT=31616 \
flask-jaeger-client:v1
```

Verify

```bash
curl http://localhost:5000

curl http://localhost:5000/hello
```

---

# Push Image to Docker Hub

Tag the image

```bash
docker tag flask-jaeger-client:v1 rootpromptnext/flask-jaeger-client:v1
```

Push

```bash
docker push rootpromptnext/flask-jaeger-client:v1
```

---

# Deploy on Kubernetes

Deploy the application

```bash
kubectl apply -f deployment.yaml
```

Verify

```bash
kubectl get pods -n observability

kubectl get svc -n observability
```

Application URL

```
http://<NODE-IP>:30500
```

Example

```bash
curl http://<NODE-IP>:30500

curl http://<NODE-IP>:30500/hello

curl http://<NODE-IP>:30500/error
```

---

# View Traces

Open the Jaeger UI

```
http://<NODE-IP>:30686
```

Select the service

```
flask-jaeger-demo
```

Click

```
Find Traces
```

Open any trace to view the generated spans.

---

# Cleanup

Docker

```bash
docker stop flask-jaeger-client

docker rm flask-jaeger-client
```

Kubernetes

```bash
kubectl delete -f deployment.yaml
```
