This is an experimental package for demonstration purposes in video courses. It depends on Numpy and Pandas. It calculates the square numbers up to n, takes the last digit of each and creates a distribution dictionary. Example usage:

```python
from fcs_package.fcs_last_digit import last_digit_of_squares

print(last_digit_of_squares(1000))
```

Result:

```
{0: 100, 1: 200, 4: 200, 5: 100, 6: 200, 9: 200}
```

Big numbers should be avoided because square should fit into 32 bit integer.
