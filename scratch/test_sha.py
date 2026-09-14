# Test SHA256 in Python and verify JS equivalence
import hashlib

def sha256_py(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

test_val = "admin1234"
print("Hash of admin1234:", sha256_py(test_val))
assert sha256_py(test_val) == "ac9689e2272427085e35b9d3e3e8bed88cb3434828b43b86fc0596cad4c6e270"
print("Hash verified successfully!")
