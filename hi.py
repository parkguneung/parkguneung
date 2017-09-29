Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as a
>>> def star(n):
	a.penup()
	a.forward(100)
	a.pendown()
	for j in range(n):
		for i in range(5):
			a.pendown()
			a.forward(30)
			a.left(144)
			a.penup()
		a.backward(100)
		a.pendown()
		a.left(360/n)

>>> star(3)
>>> 
