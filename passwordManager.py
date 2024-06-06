import hashlib
class passwordManager:
    @staticmethod
    def generatePassword(password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8')) # will convert the string to bytes
        return sha256.hexdigest()



    

