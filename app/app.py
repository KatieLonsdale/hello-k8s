from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def root():
  msg = os.environ.get("APP_MESSAGE", "Hello Kubernetes World!")
  pod = os.environ.get("POD_NAME", "unknown-pod")
  node = os.environ.get("NODE_NAME", "unknown-node")
  return f"<h1>{msg}<h1><p>Pod: {pod}</p><p>Node: {node}</p>"

@app.route("/healthz")
def health():
  return "ok", 200

@app.route("/readyz")
def ready():
  return "ready", 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

  