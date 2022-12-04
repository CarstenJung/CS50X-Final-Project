# Helper Functions for Login
from functools import wraps
from flask import g, request, redirect, url_for
from PIL import Image


# Decorate routes to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Image Color API
def scan_image(image):
    """Scan image for colors"""
"""     # Create a list of colors
    colors = []
    # Open image
    img = Image.open(image)
    # Get image colors
    img_colors = img.getcolors()
    # Sort colors by count
    img_colors.sort(reverse=True)
    # Get top 5 colors
    for i in range(5):
        colors.append(img_colors[i][1])
    # Return colors
    return colors """

