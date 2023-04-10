# Simple bit repacker for binary files
Simple binary repacker for binary files.

![1](/1.png)

### Example 1
Repacking a file with 8 bit bytes into a file with 10 bit bytes:
```
0b1111111111111111 -> 0b11111111001111111100
```

### Example 2
Repacking a file with 10 bit bytes into a file with 6 bit bytes:
```
0b11100110111110011011 -> 0b111001111001
```

### Example 3
Repacking a file with 9 bit bytes into a file with 2 bit bytes:
```
0b111000110001000110 -> 0b1100
```

### Example 4
Repacking a file with 8-bit bytes into a file with 10-bit bytes and inverting the output bits:
```
0b1111111111111111 -> 0b00000000110000000011
```

## Usage
To improve the performance of this utility, I recommend using the pypy3 interpreter.
Before using, you need to install the bitstring and tkinter modules:
```
pypy -m pip install bitstring, tk
```
After installation you can run it!
```
pypy main.py
```

## Note
While the program is running, the GUI window may freeze. This is the normal mode of operation.
