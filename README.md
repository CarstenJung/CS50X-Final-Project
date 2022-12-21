# Colors - find the best colors for your next project
#### Video Demo:  <URL HERE>
#### Description:

## The main task of colors is to quickly find colors and schemes for a new design. The following functionalities are available for this:


### 1. Load, reload and save a Scheme of 5 Colors
#### @app.route(/console)

The colormind API is used to query the colors via requests. The corresponding function is in helper.py

The function is then loaded on the first render or when the page is reloaded and return a variable "result" with the processed JSON data from the API call

The data is saved as a global variable to be able to use it in different routes and prevent reloading when the save button is used

New color schemes can be loaded as often as you like using the "New Palette" button and reload the load_more() function.

The color scheme can be saved under the "My Colors" tab using the "Save Palette" button.



### 2. Load an image and search for the 5 dominant colors and save it if desired to "My Colors"
#### @app.route(/scan and /scanned)

Under "Scan Image" you can upload your own image via a file input and determine the 5 dominant colors.

When the image is loaded, it will be displayed as a preview. An onchange function was created in main.js, which displays the loaded image via an html element.

If an image is loaded, the image is saved in a variable and then saved in the previously defined upload folder with the image name. This is then forwarded to /scanned where the 5 most common colors are displayed.

With the help of the PIL (Python Imaging Library), the image is then split and the 5 most common colors are evaluated. Unfortunately, in the case of images with a high proportion of white, these are also named as the dominant colors. So not quite ideal.

With the with open function the scan_image function is then used to store the 5 most common colors in a global variable so that I can also use them outside of the if statement.

With the "Save Color" button, the colors from the image can be saved under "My Colors".



### 3. Manage your color schemes and image colors. Copy the RGB data and delete if necessary
#### @app.route(/mycolors)

All saved colors from the console (schemes) and scan (images) are displayed separately in the "My Colors" tab.

If several colors are available, you can switch from one section to the other using the navigation at the top right with two buttons which are always displayed thanks to position fixed.

Each category has its own delete button, which can be used to delete the saved data.

The color tabs shown all have a "Copy" button that can be used to load RBG color value into the clipboard using Java Script.


### 4. Copy Color(RGB) from "My Colors" and get HEX, HSL and color name from "Analyze"

With the copied RGB color values, you can start a search via form in the "Analyze" tab and display further data like:

1. Color Name
2. HEX
3. HSL

The thecolorapi API is used for the search.


### 5. Login, Register with redirect should be missing data
#### @app.route(/login /register)

Of course there is an area to register and log in. The stored data is always assigned to the registered person.



### 6. Sorry
#### @app.route(/sorry)

Under (/sorry) there is an error page that displays a message with the corresponding error next to an image



### 7. Design

The CSS was created just like Java Script without the help of a library

For the animated background, a simple keyframe animation and an oversized gradient background were used. This creates an animation that is not too obtrusive and that fits the topic well.

A shadow was added to set the color tabs and the buttons apart from the background.

GSAP and SplitText were used to animate the Colors lettering on the route(/).

The buttons have hover and active animations to give the user feedback.

The design is responsive.

