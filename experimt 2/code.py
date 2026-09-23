import hashlib

text = "hello"
hash_value = hashlib.sha256(text.encode()).hexdigest()
print("Original text:", text)
print("SHA-256 hash:", hash_value)

sha256_hash=hashlib.sha256()
filename="experiment 2/sample.txt"
with open(filename, "rb") as file:
    while chunk:= file.read(4096):
        sha256_hash.update(chunk)

print("Original text:", filename)
print("SHA-256 hash:", sha256_hash.hexdigest())
