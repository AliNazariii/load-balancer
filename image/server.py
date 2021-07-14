from flask import Flask, request
import json
import subprocess

app = Flask(__name__)


@app.route("/", methods=["GET"])
def req():
  try:
    body = json.loads(request.data)
    process = subprocess.Popen(["python", f"/home/ali{body['code']}", f"/home/ali{body['input']}"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stdout:
      file = open(f"/home/ali{body['output']}", "w")
      file.write(stdout.decode("utf-8"))
      file.close()
      return {"status": "200"}
    else:
      return {"status": "500"}

  except Exception as e:
    print("error", e)
    return json.dumps({"error": str(e)})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=50051)
