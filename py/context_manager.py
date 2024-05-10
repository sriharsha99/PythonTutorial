class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # Optionally, return an object to be used within the 'with' block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # Cleanup code can be added here

# Using the context manager
with MyContextManager() as cm:
    print("Inside the 'with' block")