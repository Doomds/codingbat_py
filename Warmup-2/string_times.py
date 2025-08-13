def string_times(str, n):
  if n <= 0:
    return ""
    
  for i in range(n):
    new_str = str * n
        
  return new_str


# Tests
print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 3))
print(string_times('Hi', 0))
