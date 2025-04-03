# **Mayhap**

**Mayhap**: Where your functions *may* happen... or *not*.  
Embrace the uncertainty in your code execution!

---

## **Overview**

Mayhap is a whimsical Python package that allows you to introduce controlled randomness into your function executions. By decorating your functions with `@maybe`, you can specify various probability distributions to determine whether a function should execute or not. It's perfect for simulations, testing, or just adding a bit of unpredictability to your code.

---

## **Features**

- **Multiple Distributions**: Choose from uniform, weighted, normal, exponential, Bernoulli distributions, or define your own custom logic.
- **Easy Integration**: Simply decorate your functions with `@maybe` and specify the desired distribution and parameters.
- **Flexible Probability Control**: Tailor the execution probability to fit your specific needs.
- **Optional Verbosity**: Control whether skipped executions print a message with the `verbose` flag.

---

## **Installation**

Install Mayhap using pip:

```bash
pip install mayhap
```

---

## **Usage**

Here's how you can use Mayhap in your projects:

### **Uniform Distribution**

Execute a function with a fixed probability.

```python
from mayhap import maybe

@maybe(distribution='uniform', probability=0.7)
def greet(name):
    print(f"Hello, {name}!")

greet('Alice')  # Has a 70% chance to print the greeting.
```

### **Weighted Distribution**

Assign different weights to execution outcomes.

```python
@maybe(distribution='weighted', weights=[3, 1])
def farewell(name):
    print(f"Goodbye, {name}!")

farewell('Bob')  # 'Goodbye, Bob!' is three times more likely to print than not.
```

### **Normal Distribution**

Execution probability follows a normal (Gaussian) distribution.

```python
@maybe(distribution='normal', mean=0.5, stddev=0.1)
def announce(event):
    print(f"Announcing {event}!")

announce('the event')  # Execution probability is centered around 50%.
```

### **Exponential Distribution**

Execution probability decreases exponentially over time.

```python
@maybe(distribution='exponential', lambd=1.0)
def notify(user):
    print(f"Notification sent to {user}.")

notify('Charlie')  # Execution probability decreases over time.
```

### **Bernoulli Distribution**

Execute based on a Bernoulli trial with probability `p`.

```python
@maybe(distribution='bernoulli', p=0.3)
def alert():
    print("Alert triggered!")

alert()  # Has a 30% chance to trigger the alert.
```

### **Custom Probability Function**

Define your own logic for execution probability.

```python
def custom_logic():
    # Custom conditions for execution
    return some_external_condition_check()

@maybe(distribution='custom', custom_func=custom_logic)
def process():
    print("Processing data.")

process()  # Executes based on custom logic.
```

### **Controlling Verbosity**

You can control whether skipped function calls print a message with the `verbose` flag.

```python
@maybe(distribution='uniform', probability=0.5, verbose=False)
def silent():
    print("Might run... but won't explain if not.")
```

---

## **Contributing**

Contributions are welcome! If you'd like to improve Mayhap or add new features, please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

---

## **License**

This project is licensed under the **GPL-3.0-only License**.  
See the `LICENSE` file for more details.

---

**Mayhap**: Embrace the uncertainty in your code execution!