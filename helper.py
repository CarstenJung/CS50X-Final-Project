# Helper Functions for Login
from functools import wraps
from flask import g, request, redirect, url_for
from flask import session
from PIL import Image


# Decorate routes to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Image Color
def scan_image(image):
    """Scan image for colors"""
    # Create a list of colors
    colors = []
    # Open image
    img = Image.open(image)
    # Get image colors
    img_colors = img.getcolors(img.size[0]*img.size[1])

    # Get top 5 colors
    for i in range(5):
        colors.append(img_colors[i][1])
    # Return colors
    return colors


# Color API
def load_more(result):
     # ENDPOINT:
    url = "http://colormind.io/api/"
    # Request Format
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"model":"default"}'

    # Request:
    resp = requests.post(url, headers=headers, data=data)

    colors = resp.json().get("result")
    result = [(colors[0][0], colors[0][1], colors[0][2]), (colors[1][0], colors[1][1], colors[1][2]), (colors[2][0], colors[2][1], colors[2][2]), (colors[3][0], colors[3][1], colors[3][2]), (colors[4][0], colors[4][1], colors[4][2])]

    return result