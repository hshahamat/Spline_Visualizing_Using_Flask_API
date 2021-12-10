# Spline Visualizing Using Flask API
A spline visualization replaces the straight line of a line visualization with a curve.

### requirements
Flask==1.1.2
numpy==1.18.5
opencv_python==4.5.4.58
Pillow==8.4.0
requests==2.24.0
scipy==1.5.0

### First of all we need to run the following command in a separate terminal to start flask API:
python flask_app.py


### Then in another terminal, we can run this command to send an image and its corresponding spline to the API, and then receive and show the final image:
python test_flask_app.py


### You can also show spline on images directly by this file (without using flask API):
python test_show_spline.py


### Spline visualization on Image 1 and the results can be seen in Image 2.
### Image 1
<div align="center">
    <img src="/dog.jpg">
</div>


### Image 2
<div align="center">
    <img src="/result.jpg">
</div>
