from app.core.security import get_password_hash, verify_password

pwd = "123456" * 50

hashed = get_password_hash(pwd)
print("HASH:", hashed)

print("VERIFY:", verify_password(pwd, hashed))
