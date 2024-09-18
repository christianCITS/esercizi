from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
"In questo modo e' possibile generare una chiave pubblica e una privata  (da linea 5  a linea 9) (key_pair:chiave privata,public key chiave pubblica)"
# Generating RSA Key Pair
# key_pair = RSA.generate(2048)
# public_key = key_pair.publickey()
# print(public_key.export_key())
# print(key_pair.export_key())
sPriv='-----BEGIN RSA PRIVATE KEY-----\nMIIEoAIBAAKCAQEAoTppgZzFy3uo6ZMQitbga0A1u/pX4zAfoGkZVK4oJx13ECwM\nGR4UC0HGt4f+Yna1BNUMJuPu3JaRnqSZE7v1CEjLlF3xmugIMlsOJlaqmZS/cA5P\n+dGkcXjHWyQGyhxD61j5KkwQZ3/GXefykoRZImLKpzakMOHDSwGtpjZnp8yuFRUo\nSTWCmeXL0DARHHMYsZN/smtoo7qCB4j+O4i8QjUxDXcUhDf/P5DqJzYQfEED3aWs\nvC14Dc8MX3yJmq+T3VkZhdvQHC/Bkbf+thXDdN59hvWSKGGK7Z1zl3uCFInJLJig\n48he4/sU3IxiM+NDEnolC7wBCtSi5+fZAq33uQIDAQABAoH/DP1Hwsl+pgYwdaED\nlCv7qKhjq+Ffc05NPf85qzjcw0n8bbEeyGdD9iQ2flLWi9hEfT8s23VBqUP4N2/L\nZWufMiurOyjWbkSDZIsxeKVC2VzCj6SXjOj29q1kYlNkuKPOVQe2C1JVgAErWiV1\nxZgkFkEfUpl0YPvPYBuigeGgOESEcF0Qe4eTZyLNvpR+vb/ZldGzDOQvHAQ9Hi1j\nqroLueQYJjYTqIC03pDgiYBlSvGFzB9WUWWv75uyhm0WxOI9KO/+KWgYyPtWywMH\nj1BaDHuvCGg8sTi/4epMZKyeRg+D+23bcIr9RPv3hZJGj+25W/P3o6f7+nFWHHbG\n+/lhAoGBAL05JBjMcSJilxHg98jikXM6OINLXQAA+S9oV+3t/EbV6KHSj9/qRCUc\n+FWjW2zd4GbsHuVlLoux0Qcq9xAl76LqHmSgStpp6cEU6iAkGvhJL28VUCl5y6yR\nON3lL/lgtPjB+5BZfGmIe3DsQKm20M5S6jZ7Qn2FFsKFcefDrtwZAoGBANogIqr/\nersKydXLbSnc29xFKOhNGwPHDa4LScxrI2sltr1GoCINVCxmlYVFv4vL0Q/eqMsu\n2Z9Ndu9hiLalL40ce4ar21OCwJUgA0Wh4xEkbI8Fdp3AKfwZLyO1vKbTvpsiYP+N\nFomHRNoqx0DqPv/qW8guv1mDi2znRCBvE2yhAoGAA7LXOsjcOUDWFRphnYKYNzlf\nG2ngsnxSYpPWjCcHtFbAClG0UDsjA9qyG/JqehFILprU68TziPV70XkMhTtImNWc\nrHjZnbVORWDkRqaOBGZhz/kJrRXdXk0kYGn3axdx0h7wjNzC6skpKIblqKuTH0VN\noKz+Grf8Puce19niVBkCgYAInsh/9YTGK5D6cAWqZ94QgHMzawisR4uU20FZYMqP\ni3gDVu0xK1GuR4eVMsJ1JeLnO6d0EC/ticQvha0/epu8eemv0s7iKAKwYgl/EPzG\nSqg3psGfTl7aZaxlPuNrvGaF/v/SWaMQYFYqQRKK0DcZKgvih2ZshTRXY3Rfy8P6\nwQKBgGz0VgcUrJy5cVco1XZDfCAvWCizwwig5mD5cGxDHAV1bUueq7mE2S5D+Nww\nJARgooQXIQo32ROP7I7FuJbhk8iUN5d4CfdEWpjrSgf17NiTu9aWVMR0Id05eYvO\nvBl2lef/aYi3KeF+mC3uaoCNbBq+3lwQ0Z8ZRkr23vueRv1t\n-----END RSA PRIVATE KEY-----'
sPub='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoTppgZzFy3uo6ZMQitbg\na0A1u/pX4zAfoGkZVK4oJx13ECwMGR4UC0HGt4f+Yna1BNUMJuPu3JaRnqSZE7v1\nCEjLlF3xmugIMlsOJlaqmZS/cA5P+dGkcXjHWyQGyhxD61j5KkwQZ3/GXefykoRZ\nImLKpzakMOHDSwGtpjZnp8yuFRUoSTWCmeXL0DARHHMYsZN/smtoo7qCB4j+O4i8\nQjUxDXcUhDf/P5DqJzYQfEED3aWsvC14Dc8MX3yJmq+T3VkZhdvQHC/Bkbf+thXD\ndN59hvWSKGGK7Z1zl3uCFInJLJig48he4/sU3IxiM+NDEnolC7wBCtSi5+fZAq33\nuQIDAQAB\n-----END PUBLIC KEY-----'
pubFra='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAodRTArmVwLiEj9KGI0In\nHWTUM4N7jru3qfClugLG3RbueugS/xTup4FzbUUIT7AQFwU4Y+6riBjhImKiVqtr\n7f4msIyuufyT3u3/Tta3Y8EwEh7jRMDWgIKu1OZE5kQBIig7LAW9sKpazOeyLCgQ\nAEg6yWQSPR3TF6Y5/9Yhy8YP+oNsAk2SiVFJNadgfVX49QRJhn2/IEtppeRZDyMX\npWNkVCGRDGBaLM/jU4od8hmmXCXYpKKNUUY6U0rk8emK3b6J/xad5UoKcPzGpSg6\nGpam0NeMLe5FmtGahCGBw/6GVX/UWtt7Rtr1YxaNzABMD5QWFle5tuc9ogKTBHcg\nEwIDAQAB\n-----END PUBLIC KEY-----'
PubMattia='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlMZQj1Z2ABv8yNur17Ba\nzUnuWOFX2/6k4FhSbSZ/uuk/gwM99zM03CSxatZt8K8PU9K5ipuIoboS0zbIj+tz\nuWb9wP+w+qbvwuctcgDZAObK6TBKt12X2KGsKpQkFXjzk/anomx6o9v1IWcmh0Ox\noWfX+mt50orJ7gpWwa8Xu96o0Fxvv0Ccp+G1VltkN+T9YaJK+r5tm7naDDQzheJN\n+HteJnNUVOA/0JEqaRoQ9QA3gwT2GwUC6QgNBIpBoo0Du+ybx55xfCquJaezmyr5\nSpgCkXcWU7yz974QMm1wp4j8umrGdXikegwDwivB3ej/UAR1xQCll4CrLUi3NVI/\nzQIDAQAB\n-----END PUBLIC KEY-----'
pubFil='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAt0uxmw92L7B4hcvhBO6t\nOHomNGouo269U5Z7n6BznUEcq0soR6h3wtr0+a/qXp9pLZcDfuTt7gcACiD11hn+\nkpnp5fNghQjmXqkXn7U085bQM9NPnGcDbbwpAcElBbbEs6TxOIrA3ZPuNeZnwqz6\nICvr4j/Y4YKwIfTVr7urDcaq+tzOCM7lfAV3mEzaHNudNwHBaz1/C+WEWqsHtNza\n4yLMl96U4hHw+CAG8LyGk1ySM6q7kUMpExpgkAH2fRqn0Bn8f3dkPNBMkupTp8qv\nTfLL2IkkERtZ8oOWw5Lfq54HwPPstrG//GFxqj/u2zh7Hh3FphkJW20zQuXAN06c\n6QIDAQAB\n-----END PUBLIC KEY-----'
messaggiodaFra="hwawxdK6kE4P6mPjeRbffq1WzObzJlAhDBsGNVtQ6yGIm56T+SPnLcMZK9oKpnp6zR3j9xgbYsvKJlDch6viBGI+0bSDOuxEuQW46l6XlwwBjd0A9B5/ID2bPAz56eG7aJK2uxYURrkAzSLAdpIuQ7x8zWP4lOqGK9FbB/bvvFNkG33XVfkKmlrNXUFF/oa039lh4fV0OpEB5PCOwI0jPyel4Pl+2jG8uo9Xye4OGJAkRauW19jm9cKWnEeR49KIiJxuGw1LmCI+0NsmhovSna4CGAPXye8FVleY5IlkjqKEzjDo8kC93D191I4da5A9XWHF18ESIG+PMR8XAk27uA=="
messaggeMattia="Z5HP9tsQcjsaox74gZeKaulGnevbv97UTjwJ4C31UetwX31WstO8aPTiBd3/aFlZrowVqfUINv76twQeLVmtj/jzrVblqzIXXpH0fFISyvfaIc3NDFeHeJ9QejU79HHnY61Dh+v1RroLLSv2KVZm+KRoaMmEs7+VS2097LBCJXJXGe35IbwD6HK1swOS9yenC7zlNyU//ELGlb7ghADKOWkILy1pQnthD0wv3UkeVELqE+/xIR5wxojytZZ1+xfXKJt/62AE7OblcJtmuKR2hZsJYIpN9KPE9sfcu4IQN9EoJSsyRAQvkfRCBf3CLz6S0PwC0iAW5Nop1SDbjHwSNQ=="
messFil="EROIUB4XMD6nIgyXyTBVCxmtRMqzW8rDQ/a8SvKl8Gp4EAME1lpkUAayPBRQ2HzwnSl/FoPVYjmMkOP07Xa22zBGPpn6HOWCra5z+5D/hnN3mWR0ruc7qTqQcJZiDoFdNbF78SXIqVmdun2ag6/hsIQCJa4+Xzkbe4YnxyfTUKC1iVS94+YL8h8/qppeu9onKevHzq1u95209jNYCxy32CEpD6x2DE3y819+icNKLASWYXCfg8Xn3/wZHU4EWfZwAwIsgxnwPxFKHVaMBB5AYMxOQ29MszY67VQPs/67Dx1UWayu9w/Qx/AosrtKlNoY5mZUBwzKTj59obKd5bgbjA=="
messaggioFil2="jjlT2QdC4jNms+XSzEBwB6L/rPocMMo6pMa9NDpZt+4Z6hpXHNduR0I6n6t1Iw0j/jIRGsaFp3314u/vsELHmaN6oCuhM4kTx4v1fFdVASro/GTI892+kS107etY8MER0kMWj777bNYAj6S1FOJaqfMByzzLnoj17GSpTsxBxDIvyPgdgHUpFgnjt8DMK8FOODYhdqJ+plufdyIEcSObh8HsR6UZdX4EnBHF7e9Bt38/qNIUHUNL8OxbCmnIuxetJh3Ajzukmp40mAVZT8ahzqXhzGyaX4DWFBB/RgsWR93lEu+LWe0Y5LR6JmrQeUiq2HrO1fkLwI2UehYQE3Yasg=="
messaggioMio="non sei bono manco a fa un cazzo de body che cresce al serpente pippa"

key_pair=RSA.import_key(sPriv)
public_key= key_pair.public_key()
chiaveFra=RSA.import_key(pubFra)
chiaveMat=RSA.import_key(PubMattia)
chiaveFil=RSA.import_key(pubFil)




# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# # Example usage
# message = "This is a secret message"
# encrypted_message = encrypt_message(message, public_key)
# decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)

print(encrypt_message(messaggioMio,chiaveFil))





