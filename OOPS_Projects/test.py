# Define the classes
class A:
    def greet(self):
        return "Hello from A"

class X:
    def greet(self):
        return "Hello from X"

class B(X):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(C, B):
    pass

# Create an instance of D
d = D()

# Check the MRO of class D
print(D.mro())  # Output: [, , , , ]

# Call the greet method
print(d.greet())  # Output: Hello from B
     