"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y): #x,y are Binarynumber
  
    xvec = x.binary_vec
    yvec = y.binary_vec
    xvec,yvec = pad(xvec,yvec)
    n = len(xvec)
    if x.decimal_val <= 1 and y.decimal_val <=1:
      return     BinaryNumber(x.decimal_val*y.decimal_val)
    else:
      l_xvec,r_xvec = split_number(xvec)
      l_yvec,r_yvec = split_number(yvec)
    #a = xl*yl
    a = _quadratic_multiply(l_xvec,l_yvec)
  #b = xr *y l 
    b = _quadratic_multiply(BinaryNumber(l_xvec.decimal_val + r_xvec.decimal_val),BinaryNumber(l_yvec.decimal_val+r_yvec.decimal_val))
   #d = xl*yr
  #c = xr*yr
    c = _quadratic_multiply(r_xvec,r_yvec)
  # result = 2^(n/2) *a + 2^(n/2)(b-a-c) + c

    result = bit_shift(a,n).decimal_val + bit_shift(BinaryNumber(b.decimal_val -a.decimal_val - c.decimal_val),n//2).decimal_val + c.decimal_val
  
      
    
    
    return BinaryNumber(result)
    ### TODO
    pass
    ###


    
    
def time_quadratic_multiply(x, y, f):
    start = time.time()
    print(f(BinaryNumber(x),BinaryNumber(y)));
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000

print(time_quadratic_multiply(3,6,quadratic_multiply))

    

