'''
ARITHMETIC OPERATORS ---------------------------------------------------------------
Binary Operators ---------------------------------------------------------------------
Operator	            Description	                                            Syntax
+	Addition:           adds two operands	                                    x + y
–	Subtraction:        subtracts two operands	                                x – y
*	Multiplication:     multiplies two operands	                                x * y
/	Division (float):   divides the first operand by the second	                x / y
//	Division (floor):   divides the first operand by the second	                x // y
%	Modulus:            returns the remainder when first operand
                        is divided by the second	                            x % y
**	Power :             Returns first raised to power second	                x ** y

Float vs Floor Division -------------------------------------------------------------
In Python 3.x, 5 / 2 will return 2.5 and 5 // 2 will return 2.
The former is floating point division, and the latter is floor division,
floor division sometimes also called integer division (because floor division returns integer value).

In Python 2.2 or later in the 2.x line, there is no difference for integers unless you perform
a from __future__ import division, which causes Python 2.x to adopt the 3.x behavior.

Regardless of the future import, 5.0 // 2 will return 2.0 since that's the floor division result of the operation.

Modulus / Remainder -----------------------------------------------------------------
How to get Remainder?
14 % 4
Method:
01. divide opt1 with opt2
    14 / 4 = 3.5
02. convert answer from float to int. and multiply it with opt2
    3 * 4 = 12
03. subtract the answer with opt1
    14 - 12 = 2
04. the remainder 14/4 is 2

Classic Example:
If you want to determine what time it would be nine hours after 8:00 a.m. On a twelve-hour clock,
you can’t simply add 9 to 8 because you would get 17. You need to take the result, 17, and use % to get
its equivalent value in a twelve-hour.

context:
8 o'clock + 9 = 17 o'clock
17 % 12 = 5

Power Operator -----------------------------------------------------------------------
2 power of 5
2**5 translates to 2*2*2*2*2

ASSIGNMENTS OPERATORS --------------------------------------------------------

Operator        Description
y += 1			# add then assign value

y -= 1			# subtract then assign value

y *= 2			# multiply then assign value

y /= 3			# divide then assign value

y // = 5		# floor divide then assign value

y **= 2			# increase to the power of then assign value

y %= 3			# return remainder then assign value

x &= 3	        x = x & 3 #x and 3
x |= 3	        x = x | 3 #x or 3
x ^= 3	        x = x ^ 3
x >>= 3	        x = x >> 3
x <<= 3	        x = x << 3

COMPARISON OPERATORS ---------------------------------------------------------------
Operator	    Name	                    Example
==	            Equal	                    x ==
!=	            Not equal	                x != y
>	            Greater than	            x > y
<	            Less than	                x < y
>=	            Greater than or equal to	x >= y
<=	            Less than or equal to	    x <= y


LOGICAL OPERATORS ---------------------------------------------------------------------
Operator    Description	                                                    Example
and 	    Returns True if both statements are true	                    x < 5 and  x < 10
or	        Returns True if one of the statements is true	                x < 5 or x < 4
not	        Reverse the result, returns False if the result is true	not     (x < 5 and x < 10)

MEMBERSHIP OPERATORS --------------------------------------------------------------------
Operator	Description	                                                                        Example
in 	        Returns True if a sequence with the specified value is present in the object	    x in y
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y

BITWISE OPERATORS ------------------------------------------------------------------------
Bitwise operators are used to compare (binary) numbers
Operator    Name	                Description
& 	        AND	                    Sets each bit to 1 if both bits are 1
|	        OR	                    Sets each bit to 1 if one of two bits is 1
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
~	        NOT	                    Inverts all the bits
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
'''