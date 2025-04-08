# Instance Method in Python
# This code defines a class called Student which has a class attribute name and age and a class method printall(). The printall() method takes one parameter self and gender.

# When creating an object of the class, o=Student(), you can call the printall() method using the object and providing the additional parameter gender as an argument. For example, o.printall("Male") or by using the class name and passing the object and the argument as Student.printall(o,"Male").

# When you try to call o.printall() or Student.printall(o) without providing the required parameter gender you get TypeError as "Missing 1 required positional argument: 'gender'"

# This is because, in method definition, we have defined two parameters self and gender and if we call the method without providing both the parameters, it will raise an error.


# instance Methods
class student:
    name = "Shanmugavel"
    age = 20

    def printall(self,gender):
        print("Name : ",student.name)
        print("Age : ",student.age)
        print("Gender : ",gender)

o = student()
# o.printall()
# student.printall(o)
o.printall("Male")
student.printall(o,"Male")