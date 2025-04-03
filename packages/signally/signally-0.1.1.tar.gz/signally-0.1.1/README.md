# PyEvent: A simple event handling library for python

## Getting Started

- Simply Run this Command:
  
``` bash
pip install signally
```

- Here are the examples on how to run events and add a listeners:

```python
from signally.event import Event

test_event = Event()

def greet(name, **kwargs):
    print(f"Hello, {name}!")

def greet_with_exclamation(name, **kwargs):
    print(f"Hello, {name}!!!")

def greet_with_age(name, age, **kwargs):
    print(f"Hello, {name}! You are {age} years old.")

@test_event.emittable
def greet_with_decorator(name, **kwargs):
    print(f"Hello, {name} from decorator!")

def main():
    # Add listeners to the event
    test_event.add_listener(greet) # Greet the user
    test_event.add_listener(greet_with_exclamation) # Greet with exclamation 
    test_event.add_listener(greet_with_age)  # Greet with age
    test_event.add_listener(lambda name, **kwargs: print(f"Hello, {name} from lambda!")) # Greet from lambda
    # test_event.emittable(greet_with_decorator) # This should be a decorator and throws error
    
    # Emit the event
    test_event.emit(name="John", age=20)


if __name__ == "__main__":
    main()

```

<b> Just Copy to try and get started...</b>