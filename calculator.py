"""
Calculator Module with Basic Operations
"""

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    
    return a + b


def filter_positive_numbers(numbers: list) -> list:
    """
    Filter and return only positive numbers from a list.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        list: List containing only positive numbers
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    return [num for num in numbers if num > 0]


def calculate_average(numbers: list) -> float:
    """
    Calculate the average of numbers in a list.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        float: Average value
    
    Raises:
        ValueError: If list is empty
        TypeError: If input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    return sum(numbers) / len(numbers)


# Example usage
if __name__ == "__main__":
    # Test add_numbers
    print(f"Sum: {add_numbers(10, 5)}")
    
    # Test filter_positive_numbers
    sample_data = [-5, 2, -1, 8, 0, 3]
    positives = filter_positive_numbers(sample_data)
    print(f"Positive numbers: {positives}")
    
    # Test calculate_average
    average = calculate_average([1, 2, 3, 4, 5])
    print(f"Average: {average}")
