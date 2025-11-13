def milan_function(a, b):
    if not isinstance(a, (int,float)) or not isinstance(b, (int,float)):
        return "Error, both inputs must be numbers"
    
    return a + b

print (milan_function("3", 7))

