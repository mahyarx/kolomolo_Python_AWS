
# Python Essentials – Explained Simply

These are short and clear answers to some Python basics, explained like you’d hear from a person (not a textbook or an AI model).

---

### What is `__main__.py` used for?

So basically, `__main__.py` is what Python runs when you treat a **folder (a package)** like a script.  
If you run something like `python myfolder/`, Python will look for a file called `__main__.py` inside that folder and run it.  
It's like the entry point for a Python package.

---

### How to prevent Python module code from executing when the module is imported?

Use this classic line in your code:

```python
if __name__ == "__main__":
    # your script code here
```

This makes sure the code only runs if the file is **run directly**, and not when it’s **imported somewhere else**.

---

### What's the name of the method that represents a class constructor in Python?

It’s called `__init__`.  
When you create an object with `x = MyClass()`, Python runs the `__init__` function to set things up inside the object.

---

### What are some ways to insert a variable into a string?

Here are three common ways:

1. **f-strings** (cleanest and easiest):  
   ```python
   name = "Ali"
   print(f"Hello, {name}")
   ```

2. **`.format()` method**:  
   ```python
   print("Hello, {}".format(name))
   ```

3. **Old-school `%` formatting**:  
   ```python
   print("Hello, %s" % name)
   ```

These all do the same thing — just different styles.

---

### How can you truly restrict access to a private method in Python?

You really **can’t**. Python doesn’t have real “private” methods like some other languages.  
But you can **hide** a method a bit using double underscores, like `__secret_method()`.  
This makes Python rename it behind the scenes (name mangling), so it’s harder to call it from outside.  
Still, it’s not bulletproof — it’s more like “hey, don’t touch this” rather than “you can’t”.

---

### What Python feature would you use to add functionality to an existing function without changing its code?

That’s called a **decorator**.  
You “wrap” the function with another one that adds extra behavior — like logging, checking access, etc.

Example:

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
```

When you call `say_hello()`, it runs the extra stuff too.

---

### How is `@staticmethod` different from `@classmethod`?

- `@staticmethod` doesn’t care about the class or the object. It’s just like a regular function inside the class.

- `@classmethod` gets the **class itself** (`cls`) as the first argument.  
So it can access or change class-level stuff.

Example:

```python
class MyClass:
    @staticmethod
    def do_static():
        print("No self, no cls")

    @classmethod
    def do_class(cls):
        print("Has access to class:", cls)
```

---

### What’s the benefit of using `with` when opening files?

The `with` keyword automatically **closes the file** when you're done.  
You don’t need to call `.close()` manually, and it even works if something goes wrong in the middle.

Example:

```python
with open("file.txt", "r") as f:
    content = f.read()
```

