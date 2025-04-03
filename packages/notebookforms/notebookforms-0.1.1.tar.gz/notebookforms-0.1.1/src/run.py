from forms.formHandler import form, Form
import time

@form(token="4IVV@nSdDKQk1uDo0WgdJdgfT&r5BCfU)2v#zILxM^w3NiJkR!!07yKxpsRR0L@f")
def my_form(form:Form):
    print(form.select("Which is your favorite color?", False, options=[["Red", "red"], ["Blue", "blue"], ["Green", "green"]]))
    r = form.ab_buttons("Are you already a member?", [["Yes", "yes"], ["No", "no"]])
    print("Answer 1: ", r)
    name = form.input("What is your name?")
    
    age = form.input(f"Hi {name}, what's your age?")
    
    form.se
    
    time.sleep(5)
    
    print("done... for now")

a = my_form.serve()
print(a)