"""
Main entry point for the application.
This is a simple starter code for practicing Python.
"""


def greet(name="World"):
    """
    Returns a greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """Main function."""
    message = greet()
    print(message)
    
    # Example with custom name
    custom_message = greet("Python Developer")
    print(custom_message)


if __name__ == "__main__":
    main()
