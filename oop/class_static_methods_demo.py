# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b (static utility method)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print class attribute then return the product of a and b."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
