import os
from flask import Flask, request, jsonify
from backend.generate_blog import generate_blog

app = Flask(__name__)

@app.route("/generate_blog", methods=["POST"])
def generate_blog_endpoint():
    data = request.json
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "Please provide a topic."}), 400
    blog = generate_blog(topic)
    blog_filename = f"blogs/{topic.replace(' ', '_').lower()}.md"
    with open(blog_filename, "w", encoding="utf-8") as f:
        f.write(blog)

    return jsonify({"message": "Blog generated successfully!", "blog": blog})

if __name__ == "__main__":
    os.makedirs("blogs", exist_ok=True)
    app.run(host="0.0.0.0", port=5007, debug=True)