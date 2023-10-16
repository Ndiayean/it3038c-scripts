#Lab 7 

Below are the following instructions to run the python script that I have created. This python script uses the plugin called Turtle.

First make sure that you have virtualenv installed 

```powershell
pip install virtualenv
```



Create a folder to store the virtual env
```powershell
New-Item -Path "C:\" -Name "Testscript" -ItemType Directory
```


Now create a virtual environment called testDrawing

```powershell
python -m venv c:\testscript\testDrawing
```

Go to the testscript folder and activate the virtualenv 

``` cd c:\testscript
    .\testDrawing\Scripts\Activate.ps1
```

Now install the turtle plugin

```
    pip install turtle==0.0.1
```

Create a new script called Lab7turtledrawing.py in the same directory as the testDrawing virtual environment

Within a text editor type the following to use the turtle plugin

```python
import turtle
```

This code will customize the color of the window

```python
window.bgcolor("white")
```

This will draw the custom turtle image on the screen

```python
simpleturtle = turtle.Turtle()
simpleturtle.shape("turtle")
simpleturtle.color("blue", "yellow")
```



This will move the turtle

```python
simpleturtle.begin_fill()
simpleturtle.forward(200)
simpleturtle.left(90)
simpleturtle.forward(200)
simpleturtle.left(90)
simpleturtle.forward(200)
simpleturtle.left(90)
simpleturtle.forward(200)
simpleturtle.end_fill()
```


Clickin the screen will close the window

```python
window.exitonclick()
```


After trying out the code make sure to deactivate the virtual environment

```powershell
deactivate
```





