from flask import Flask, render_template, request

import requests

from dog_breeds import prettify_dog_breed

# Initialize the Flask application
app = Flask(__name__)

def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET","POST"])
def dog_image_gallery():
  errors = []
  if request.method == "POST":
    breed = request.form.get("breed")
    number = request.form.get("number")
    if not breed:
      errors.append("Oops! Please choose a breed.")
    if not number:
      errors.append("Oops! Please choose a number.")
    if breed and number:
      response = requests.get("https://dog.ceo/api/breed/" + check_breed(breed) + "/images/random/" + number)
      data = response.json()
      dog_images = data["message"]
      return render_template("dogs.html", images=dog_images, breed=prettify_dog_breed(breed), errors=[])
  return render_template("dogs.html", images=[], breed="", errors=errors)



app.debug = True

# Run the flask server
if __name__ == "__main__":
    app.run()