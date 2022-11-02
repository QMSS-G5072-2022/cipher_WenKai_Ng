from cipher_wn2195 import cipher_wn2195

import pytest

def cipher_test():
	test = "Barcelona"
	shift = 1
	expected = "Cvsdfmpob"
	actual = cipher_wn2195.cipher(test, shift, encrypt=True)
	assert actual == expected, "Should be Cvsdfmpob"
