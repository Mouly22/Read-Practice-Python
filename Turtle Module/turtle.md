<h2> Turtle Module </h2>

**Turtle Graphics**

```
import turtle
scrn = turtle.Screen()                  #creates a graphics window
sponge = turtle.Turtle()                #creates a turtle whose name is sponge
sponge.forward(200)                     #object.method(parameter)
sponge.left(90)
sponge.forward(100)
sponge.right(90)
sponge.forward(100)
sponge.left(90)
sponge.backward(30)
```
**Creating a Rectangle**

```
import turtle                   #here loads a module named turtle
                                #This module brings two new types: the Turtle type, and the Screen type.
scrn = turtle.Screen()          #creates a graphics window
                                #scrn is an instance of Screen class
ciri = turtle.Turtle()          #means the Turtle type that is defined within the turtle module
                                #ciri is an instance of Turtle class
ciri.forward(180)               #object.method(parameter)
ciri.left(90)             
ciri.forward(75)         
ciri.left(90)
ciri.forward(180)
ciri.left(90)
ciri.forward(75)
```
**Creating  a triangle**

```
import turtle                  
scrn = turtle.Screen()         
mini = turtle.Turtle()
mini.forward(180)
mini.left(150)
mini.forward(100)      #object.method(parameter)
mini.left(60)
mini.forward(100)
```
**Creating rectangle and triangle together**

```
import turtle                  
scrn = turtle.Screen()         
ciri = turtle.Turtle()         
ciri.forward(180)           #object.method(parameter)
ciri.left(90)             
ciri.forward(75)         
ciri.left(90)
ciri.forward(180)
ciri.left(90)
ciri.forward(75)

mini = turtle.Turtle()
mini.forward(180)
mini.left(150)
mini.forward(100)      #object.method(parameter)
mini.left(60)
mini.forward(100)
```

