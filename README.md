
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
FastApiDI implements all the 3 cons from above.  
✅ Can work with abstractions and encourage you to do it.  
✅ Inject dependencies from outside, replace implementations without changing route module.  
✅ Implements dependency lifetime management.  
