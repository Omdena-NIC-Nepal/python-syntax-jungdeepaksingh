def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    
    elif number < 10:
       return "Lesser"
    
    else:
        return "Equal"
 



def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum=0
    for i in range(1, n+1):
        sum += i
    return sum    


   
def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total_sum= sum(numbers)
    maximum= max(numbers)
    minimum= min(numbers)
    return (total_sum,maximum, minimum)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    pass
    high_score=[]
    for name, score in students_dict.items():
        if score>80:
            high_score.append(name)
    return high_score        


def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    set1=set(list1)
    set2=set(list2)
    return set1.intersection(set2)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    results={
        "sum": a+b ,
        "difference": a-b,
        "product": a*b,
        "quotient": a/b
    }
    return results
    

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    results={
        "and": x and y,
        "or": x or y ,
        "not_x":not x
    }
    return results

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    results={
        "and": a & b,
        "or": a | b,
        "xor": a ^ b
    }
    return results
 
