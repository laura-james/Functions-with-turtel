import turtle
turtle.speed(0)
turtle.width(2)
colorlist=["red","pink","magenta","purple","black","blue"]
# function start
def hexagon(size,color,x,y):  #2 parameters size & color
  turtle.goto(x,y)
  turtle.pendown()  
  for i in range(6):
    turtle.color(colorlist[i])
    turtle.forward(size)
    turtle.left(60)
  turtle.penup()
#function end
    
#call the function
for i in range(10):
  hexagon(20*i,"blue",i*10,i*10) #draw a hexagon

