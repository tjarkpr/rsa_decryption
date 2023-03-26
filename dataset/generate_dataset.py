import pandas as pd

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from tqdm.auto import tqdm


if __name__ == "__main__":
    data = []
    for _ in tqdm(range(100)):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        der_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        der_public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        data.append((der_private_key, der_public_key))
    data = pd.DataFrame(data, columns=['private', 'public'])
    data.to_csv('./rsa_key_dataset.csv', index=False)