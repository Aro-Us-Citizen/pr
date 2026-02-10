# Simple Calculator - Needs Review

def calc(a, b):
    # Add two numbers
    c = a + b
    return c

def process_list(nums):
    out = []
    for n in nums:
        if n > 0:
            out.append(n)
    return out

# No error handling, poor naming, missing docs
