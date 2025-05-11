#  Understanding Dependency Injection in FastAPI (with Annotated)

This README is your **all-in-one** guide to understanding **Dependency Injection (DI)** in **FastAPI**, including concepts like **coupling**, why DI is used, and how to use `Annotated` with `Depends`.

---

##  What is Dependency Injection?

**Dependency Injection** means:  
> “Don't create what you need inside your function — ask for it and let something else provide it.”

###  Real-life analogy:
Imagine you're building a toy house.  
Instead of making your own bricks every time, you just say:  
> “Please give me some bricks.”

---

##  Why Use Dependency Injection?

| Without DI                        | With DI                               |
|----------------------------------|----------------------------------------|
| You build/setup everything       | You get already-built stuff injected   |
| Code is tightly coupled          | Code is modular and testable           |
| Hard to change or test           | Easy to swap/mock components           |


###  Benefits:
- Cleaner, modular code
- Easier testing (you can mock dependencies)
- Reusability of components
- Separation of concerns

---

##  What is Coupling?

**Coupling** means how tightly connected your components are.

- **Tightly Coupled:** Functions/classes know too much about each other. Changing one breaks the other.
- **Loosely Coupled (Good):** They depend only on interfaces or external inputs (like DI), so they are flexible and independent.

**Dependency Injection helps reduce coupling.**

---

##  How FastAPI Handles Dependency Injection

FastAPI lets you declare dependencies in your path operation functions using `Depends()`.

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_message():
    return {"msg": "Hello from dependency"}

@app.get("/")
def read_root(message: dict = Depends(get_message)):
    return message
```
- FastAPI sees `Depends(get_message)`
- It runs get_message() and injects the result into the route



## Cleaner with Annotated
Python 3.9+ supports Annotated, which combines type hinting and dependencies.

```python
from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

def get_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/goal")
def goal(response: Annotated[dict, Depends(get_goal)]):
    return response
```

### Benefits of Annotated:
- Clearer syntax
- Avoids confusion with default values
- Recommended in FastAPI 0.95+


##  Dependency Caching

FastAPI runs each dependency **once per request**, even if multiple routes or sub-dependencies use it.  
This improves performance and avoids repeated work.


## Use Cases of Dependency Injection
- Inject database session
- Inject configuration or settings
- Authenticate users
- Inject third-party APIs (e.g. Stripe, ShipEngine)
- Common shared logic like pagination or logging