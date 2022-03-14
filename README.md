
# FastApiDI

[![Tests](https://github.com/EmilK322/FastApiDI/actions/workflows/tests.yml/badge.svg)](https://github.com/EmilK322/FastApiDI/actions/workflows/tests.yml)

Dependency injection utility for FastApi

## Dependency Injection In FastApi
FastApi's dependency injection system is good, but it could be better.  
It helps us passing dependencies to our route by importing and calling the dependency.  

### Pros And Cons
✅ It is simple as it can be, import and call it.   
✅ Can cache the dependency.  
❌ Violates Dependency Inversion principle, depends on implementation instead of abstractions.  
❌ Not truly injection, we cannot replace dependency without modifying the route module.  
❌ Lacks dependency lifetime management.  

### The Good News
FastApi has dependency injection, and use it in tests.
```python
app = FastApi()
app.dependency_overrides = {}
```
FastApiDI uses that mechanism to enrich FastApi with additional features.

## Dependency Injection With FastApiDI
FastApiDI implements all the 3 cons from above and more.  
✅ Can work with abstractions and encourage you to do it.  
✅ Injects dependencies from outside, replace implementations without changing route module.  
✅ Implements dependency lifetime management.  
✅ Exposes its interfaces, implement it your way if you want.  

### How To Use
Setup true dependency injection with 4 simple steps:
1. Write your abstractions and implementations
    ```python
    # asbtract.py
    import abc
    
    class Abstract(abc.ABC):
        @abc.abstractmethod
        def foo(self, a: int) -> str:
            pass
    ```
    
    ```python
    # implementation.py
    from asbtract import Abstract
    
    class Implementation(Abstract):
        def foo(self, a: int) -> str:
            return str(a)
    ```
   
2. Make your route depends on the abstraction
    ```python
    @app.get("/")
    def root(my_dep: Abstract = Depends(Abstract)):
        result: str = my_dep.foo(6)
        return {"message": result}
    ```

3. Wrap FastApi app with FastApiDI
    ```python
    from fastapi import FastAPI
    from fastapidi.facades import FastApiDI
    
    app = FastAPI()
    app_di = FastApiDI(app)   
    ```

4. Register your dependencies with specific lifetime
   ```python
   app_di.register_scoped(Abstract, Implementation)
   ```

Congratulations 🎉  
Now you can implement different implementations, The only place you need to change is the module that registers the dependencies instead of the route module

### Registration Options
FastApiDI allows many options for registering dependencies
- Inject implementation as abstraction (Recommended).  
  ```python
  FastApiDI.register_scoped(Abstract, Implementation)
  ```
  
- Inject implementation as the same implementation.  
  ```python
  FastApiDI.register_scoped(Abstract, Implementation)
  ```

- Inject implementation as the options above with parameters.
  ```python
  FastApiDI.register_scoped(Abstract, Implementation, *args, **kwargs)
  ```
Resigtration using abstractions is recommended!

### Life-Time Management
Dependency life-time is the scope of which it is getting created and destroyed.   
There are 3 types of life-time's in FastApiDI
- Singleton
- Scoped
- Custom

#### Singleton Life-Time
Singleton life-time will create the dependency only once for the entire application life-time.  
Singleton Life-time can be set with `FastApiDI.register_singleton()` method.

#### Scoped Life-Time
Scoped life-time will create the dependency every time the dependency is requested.  
Scoped Life-time can be set with `FastApiDI.register_scoped()` method.  
**Note**: FastApi's `Depends` function can cache the dependency, this behaviour creates 2 different time-lifes, you can read about it in [Life-Time And FastApi's Depends](README.md#life-time-and-fastapis-depends)

#### Custom Life-Time
FastApiDI gives you the option to customize the life-time of your dependencies.  
To implement your own life-time you simply need to register `factory` instead of the dependency itself.  
`Factory` is a function which takes 0 arguments and return the dependency.  
The `factory` is responsible for managing the creation and deletion of the dependency upon its different calls.  
Custom Life-time can be set with `FastApiDI.register_factory()` method.  

Singleton Life-time can be set with `FastApiDI.register_singleton()` method.


#### Life-Time And FastApi's Depends
FastApi's `Depends` can cache the dependancy using `use_cache` parameter which defaults to `True`.  
If `use_cache=True`, then the dependency will be cached independently of FastApiDI.  
The dependency will have life-time at least of the called request scope.  
This behaviour can impact registrations with shorter life-time then the called request scope and have no impact on longer life-times like `Singleton`.  
To disable `Depends` caching pass `use_cache=False` to it
