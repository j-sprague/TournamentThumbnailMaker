# TournamentThumbnailMaker

Python Flask website that can generate thumbnails for Smash Ultimate tournament videos. 

## Deployment

Download repository and create a virtual environment. Install requirements.txt and then run "flask run" to start website. Runs on 127.0.0.1:5000 by default.

## TODO

* Add full roster images  
  * currently only 4 out of 86 characters
* Replace hard-coded character list on selection boxes
* Save with unique image filenames in a "generated_images" folder
  * currently only overwrites a single image file in the "static" folder for testing purposes
* Different theme options
* Keep previous form data filled out after generating image to make quick edits easier
* Bulk image generation