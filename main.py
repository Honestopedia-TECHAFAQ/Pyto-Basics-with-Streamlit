import streamlit as st

def welcome_message():
    st.write("Welcome to Pyto!")

def display_variables():
    name = "Pyto User"
    age = 25
    is_learning = True
    st.write(f"Name: {name}, Age: {age}, Learning: {is_learning}")

def arithmetic_operations(num1, num2):
    st.write(f"{num1} + {num2} = {num1 + num2}")
    st.write(f"{num1} - {num2} = {num1 - num2}")
    st.write(f"{num1} * {num2} = {num1 * num2}")
    st.write(f"{num1} / {num2} = {num1 / num2}")

def conditional_statement(age):
    if age < 18:
        st.write("You are a minor.")
    else:
        st.write("You are an adult.")

def looping_example():
    st.write("Counting from 1 to 5:")
    for i in range(1, 6):
        st.write(i)

def greet_user(username):
    return f"Hello, {username}! Welcome to learning Pyto."

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def buggy_function(x):
    return x - 1

st.title("Pyto Basics with Streamlit")

st.header("Welcome Message")
welcome_message()

st.header("Variables and Data Types")
if st.button("Display Variables"):
    display_variables()

st.header("Basic Arithmetic Operations")
num1 = st.number_input("Enter first number", value=10)
num2 = st.number_input("Enter second number", value=5)
if st.button("Perform Arithmetic Operations"):
    arithmetic_operations(num1, num2)

st.header("Conditional Statements")
age = st.number_input("Enter your age", value=25)
if st.button("Check Age Group"):
    conditional_statement(age)

st.header("Looping Example")
if st.button("Run Loop"):
    looping_example()

st.header("Function Definition")
username = st.text_input("Enter your name", value="Pyto User")
if st.button("Greet User"):
    st.write(greet_user(username))

st.header("Simple Algorithm - Factorial")
factorial_input = st.number_input("Enter a number to calculate factorial", value=5)
if st.button("Calculate Factorial"):
    result = factorial(factorial_input)
    st.write(f"Factorial of {factorial_input} is {result}")

st.header("Debugging Example")
if st.button("Run Buggy Function"):
    for i in range(3):
        st.write(f"buggy_function({i}) = {buggy_function(i)}")
