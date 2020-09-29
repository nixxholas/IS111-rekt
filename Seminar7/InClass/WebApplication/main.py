from flask import Flask, render_template, request, redirect, url_for

import model

app = Flask(__name__)

# directories which store image files
image_dir = "./static/images/"

# ###############################################
# The root page. 
# This page displays all the images inside image_dir.
@app.route("/")
def root():
    return render_template("root.html", 
        image_details = model.get_all_image_details_in_dir(image_dir))
# ###############################################


# ###############################################    
# The page that displays the images based on orientation.
@app.route("/grouped-by-orientation")
def by_orientation():
    return render_template("grouped-by-orientation.html",
        square_details = model.get_square_image_details_in_dir(image_dir),
        portrait_details = model.get_portrait_image_details_in_dir(image_dir),
        landscape_details = model.get_landscape_image_details_in_dir(image_dir))
# ###############################################


# ###############################################
# The page that allows the user to search for images whose names
# contain certain keywords.
@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        keyword = request.form["keyword"]
        return render_template("root.html", image_details = model.get_matching_image_details(image_dir, keyword))
    else:
        return render_template("search.html")
        
if __name__ == "__main__":
    app.run(port=5004, debug = True)