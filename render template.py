from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  resume_data = None
  if request.method == "POST":
    resume_data = {
        "name": request.form.get("name"),
        "title": request.form.get("title"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "location": request.form.get("location"),
        "summary": request.form.get("summary"),
        "experience": request.form.get("experience"),
        "education": request.form.get("education"),
        "skills": [
            s.strip()
            for s in request.form.get("skills", "").split(",")
            if s.strip()
        ],
    }
  return render_template("index.html", resume=resume_data)


if __name__ == "__main__":
  app.run(debug=True)