import bcrypt

def hash_password(password, rounds=10):
	return bcrypt.encrypt(password, rounds=rounds)

def verify_password(to_check, password_hash):
	return bcrypt.verify(to_check, password_hash)