"""A small package for friendly greetings."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
