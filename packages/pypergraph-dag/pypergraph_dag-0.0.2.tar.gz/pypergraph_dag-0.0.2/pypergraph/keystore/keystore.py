import base64
import hashlib
import json
import random
from decimal import Decimal
from typing import Tuple, Callable, Optional, Union, Literal, Dict, Any

import base58
import eth_keyfile
from bip32utils import BIP32Key
from ecdsa import SigningKey, SECP256k1, VerifyingKey
from ecdsa.util import sigencode_der, sigdecode_der
import eth_utils
from pyasn1.codec.der.decoder import decode as der_decode
from pyasn1.codec.der.encoder import encode as der_encode
from pyasn1.type.univ import Sequence, Integer

from pypergraph.core.constants import PKCS_PREFIX
from pypergraph.network.models.transaction import Transaction, TransactionReference
from .kryo import Kryo
from .bip_helpers.bip32_helper import Bip32Helper
from .bip_helpers.bip39_helper import Bip39Helper
from .v3_keystore import V3KeystoreCrypto, V3Keystore
from ..core import BIP_44_PATHS

MIN_SALT = int(Decimal("1e8"))


class KeyStore:
    """
    Methods dealing with keys.
    """

    PERSONAL_SIGN_PREFIX = "\u0019Constellation Signed Message:\n"
    DATA_SIGN_PREFIX = "\u0019Constellation Signed Data:\n"

    @staticmethod
    def prepare_tx(
        amount: int,
        to_address: str,
        from_address: str,
        last_ref: TransactionReference,
        fee: int = 0,
    ) -> Tuple[Transaction, str]:
        """
        Prepare a new transaction.

        :param amount: Amount to send.
        :param to_address: Destination DAG address.
        :param from_address: Source DAG address.
        :param last_ref: Dictionary with keys: ordinal, hash.
        :param fee: Transaction fee.
        :return: TransactionV2 object, sha512hash, rle.
        """
        if to_address == from_address:
            raise ValueError(
                "KeyStore :: An address cannot send a transaction to itself"
            )

        if int(amount) < 1e-8:
            raise ValueError("KeyStore :: Send amount must be greater than 1e-8")

        if fee < 0:
            raise ValueError("KeyStore :: Send fee must be greater or equal to zero")

        # Create transaction
        tx = Transaction(
            source=from_address,
            destination=to_address,
            amount=amount,
            fee=fee,
            parent=last_ref,
            salt=MIN_SALT + int(random.getrandbits(48)),
        )

        # Get encoded transaction
        encoded_tx = tx.encoded

        kryo = Kryo()
        serialized_tx = kryo.serialize(msg=encoded_tx, set_references=False)
        hash_value = hashlib.sha256(bytes.fromhex(serialized_tx)).hexdigest()

        return tx, hash_value

    def encode_data(
        self,
        msg: dict,
        prefix: bool = True,
        encoding: Optional[
            Union[Literal["base64"], Callable[[dict], str], None]
        ] = None,
    ) -> str:
        """
        Encode custom data transaction for signing or signature verification.

        :param msg: Dictionary (the content of 'value' in a SignedTransaction).
        :param prefix: Enable or disable the default prefix '\u0019Constellation Signed Data:\n' to the encoded msg.
        :param encoding: Can be None (default), 'base64' or a custom encoding function.
        :return: Encoded data transaction.
        """
        if encoding:
            if callable(encoding):
                # Use custom encoding function
                msg = encoding(msg)
            elif encoding == "base64":
                # Used in the VOTING and NFT metagraph example
                encoded = json.dumps(msg, separators=(",", ":"))
                msg = base64.b64encode(encoded.encode()).decode()
            else:
                raise ValueError("KeyStore :: Not a valid encoding method.")
        else:
            # Default: used in the TO-DO, SOCIAL and WATER AND ENERGY metagraph examples
            msg = json.dumps(msg, separators=(",", ":"))

        if prefix:
            msg = f"{self.DATA_SIGN_PREFIX}{len(msg)}\n{msg}"
        return msg

    def data_sign(
        self,
        private_key,
        msg: dict,
        prefix: bool = True,
        encoding: Optional[
            Union[Literal["base64"], Callable[[dict], str], None]
        ] = None,
    ) -> Tuple[str, str]:
        """
        Encode message according to serializeUpdate on your template module l1.

        :param private_key:
        :param msg: Dictionary (the content of 'value' in a SignedTransaction).
        :param prefix: Enable or disable the default prefix '\u0019Constellation Signed Data:\n' to the encoded msg.
        :param encoding: Can be None (default), 'base64' or a custom encoding function.
        :return: signature, transaction hash.
        """

        # 1. The TO-DO, SOCIAL and WATER AND ENERGY template doesn't add the signing prefix, it only needs the transaction to be formatted as string without spaces and None values:
        #     # encoded = json.dumps(tx_value, separators=(',', ':'))
        #     signature, hash_ = keystore.data_sign(pk, encoded, prefix=False) # Default encoding = "hex"
        # 2. The VOTING and NFT template does use the dag4JS dataSign (prefix=True), the encoding (before data_sign) is done first by stringifying, then converting to base64:
        #     # encoded = json.dumps(tx_value, separators=(',', ':'))
        #     # encoded = base64.b64encode(encoded.encode()).decode()
        #     signature, hash_ = keystore.data_sign(pk, tx_value, prefix=True, encoding="base64") # Default prefix is True
        # 3. The TO-DO, SOCIAL and WATER AND ENERGY template doesn't add the signing prefix, it only needs the transaction to be formatted as string without spaces and None values:
        #     # encoded = json.dumps(tx_value, separators=(',', ':'))
        #     signature, hash_ = keystore.data_sign(pk, encoded, prefix=False) # Default encoding = "hex"
        # X. Inject a custom encoding function:
        #     def encode(msg: dict):
        #         return json.dumps(tx_value, separators=(',', ':'))
        #
        #     signature, hash_ = keystore.data_sign(pk, tx_value, prefix=False, encoding=encode)
        """ Encode """
        msg = self.encode_data(encoding=encoding, prefix=prefix, msg=msg)

        """ Serialize """
        serialized = msg.encode("utf-8")

        hash_ = hashlib.sha256(serialized).hexdigest()
        """ Sign """
        signature = self.sign(private_key, hash_)
        return signature, hash_

    def verify_data(
        self, public_key, encoded_msg: str, signature: str,
    ):
        # Encode the message the same way as in data_sign
        serialized = encoded_msg.encode("utf-8")

        # Compute SHA256 hash of the serialized message as hex
        sha256_hash_hex = hashlib.sha256(serialized).hexdigest()
        # Compute SHA512 digest of the hex string's UTF-8 bytes
        sha512_digest = hashlib.sha512(sha256_hash_hex.encode("utf-8")).digest()

        try:
            vk = VerifyingKey.from_string(
                bytes.fromhex(public_key), curve=SECP256k1
            )
            return vk.verify_digest(
                bytes.fromhex(signature),
                sha512_digest[:32],
                sigdecode=sigdecode_der,
            )
        except Exception:
            return False

    # def serialize(self, msg: str):
    #    return msg.encode("utf-8").hex()

    def personal_sign(self, msg, private_key) -> str:
        # TODO: How is this used?
        message = f"{self.PERSONAL_SIGN_PREFIX}{len(msg)}\n{msg}"
        return self.sign(private_key, message)

    @staticmethod
    def sign(private_key: str, tx_hash: str) -> str:
        """
        Create transaction signature.

        :param private_key: Private key in hex format.
        :param tx_hash: Transaction hash from prepare_tx.
        :return: Signature supported by the transaction API (@noble/secp256k1).
        """

        # secp256k1 curve order
        SECP256K1_ORDER = SECP256k1.order

        def _enforce_canonical_signature(signature: bytes) -> bytes:
            """
            Adjust the signature to ensure canonical form (s < curve_order / 2).
            """
            r, s = _decode_der(signature)
            if s > SECP256K1_ORDER // 2:
                s = SECP256K1_ORDER - s
            return _encode_der(r, s)

        def _decode_der(signature: bytes):
            """
            Decode a DER-encoded signature to (r, s).
            """
            seq, _ = der_decode(signature, asn1Spec=Sequence())
            r = int(seq[0])
            s = int(seq[1])
            return r, s

        def _encode_der(r: int, s: int) -> bytes:
            """
            Encode (r, s) back into DER format.
            """
            seq = Sequence()
            seq.setComponentByPosition(0, Integer(r))
            seq.setComponentByPosition(1, Integer(s))
            return der_encode(seq)

        def _sign_deterministic_canonical(
            private_key: str, tx_hash: bytes
        ) -> str:
            """
            Create a deterministic and canonical secp256k1 signature.
            """
            # Create SigningKey object from private key hex
            sk = SigningKey.from_string(
                bytes.fromhex(private_key), curve=SECP256k1
            )
            # Sign the prehashed message deterministically
            signature_der = sk.sign_digest_deterministic(
                tx_hash[:32],  # Truncate to 32 bytes if needed
                hashfunc=hashlib.sha256,
                sigencode=sigencode_der,
            )
            canonical_signature_der = _enforce_canonical_signature(signature_der)
            return canonical_signature_der.hex()

        tx_hash = hashlib.sha512(tx_hash.encode("utf-8")).digest()
        return _sign_deterministic_canonical(private_key=private_key, tx_hash=tx_hash)

    @staticmethod
    def verify(public_key_hex, tx_hash, signature_hex) -> bool:
        """
        Verify is the signature is valid.

        :param public_key_hex:
        :param tx_hash: Hex format
        :param signature_hex:
        :return: True or False
        """
        tx_hash = hashlib.sha512(tx_hash.encode("utf-8")).digest()
        vk = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=SECP256k1)
        try:
            # Use verify_digest for prehashed input
            valid = vk.verify_digest(
                bytes.fromhex(signature_hex),
                tx_hash[:32],  # Prehashed hash
                sigdecode=sigdecode_der,
            )
            return valid
        except Exception:
            return False

    @staticmethod
    def validate_address(address: str) -> bool:
        """
        Returns True if DAG address is valid, False if invalid.

        :param address: DAG address.
        :return: Boolean value.
        """
        if not address:
            return False

        valid_len = len(address) == 40
        valid_prefix = address.startswith("DAG")
        valid_parity = address[3].isdigit() and 0 <= int(address[3]) < 10
        base58_part = address[4:]
        valid_base58 = (
            len(base58_part) == 36
            and base58_part == base58.b58encode(base58.b58decode(base58_part)).decode()
        )

        return valid_len and valid_prefix and valid_parity and valid_base58

    @staticmethod
    def validate_mnemonic(mnemonic_phrase: str) -> bool:
        """
        Returns True is phrase is valid, False if invalid.

        :param mnemonic_phrase: String of words (default: 12).
        :return: Boolean value.
        """
        return Bip39Helper.validate_mnemonic(mnemonic_phrase=mnemonic_phrase)

    @staticmethod
    def generate_mnemonic() -> str:
        """
        :return: Mnemonic values in a dictionary with keys: mnemo, words, seed, entropy
        """
        bip39 = Bip39Helper()
        return bip39.mnemonic()

    def generate_private_key(self) -> str:
        """
        Generates private key.

        :return: Private key hex.
        """
        return SigningKey.generate(SECP256k1).to_string().hex()

    @staticmethod
    def is_valid_json_private_key(data: dict) -> bool:
        if not data:
            return False

        crypto = data.get("crypto", {})
        kdfparams = crypto.get("kdfparams", {})

        return all(
            key in kdfparams and kdfparams[key] is not None
            for key in ("salt", "n", "r", "p", "dklen")
        )

    @staticmethod
    async def encrypt_phrase(phrase: str, password: str) -> V3Keystore:
        """
        Can be used to encrypt the phrase using password.

        :param phrase:
        :param password:
        :return:
        """
        return await V3KeystoreCrypto.encrypt_phrase(phrase=phrase, password=password)

    @staticmethod
    async def decrypt_phrase(keystore: V3Keystore, password: str) -> str:
        """
        Can be used to decrypt the phrase using password.

        :param keystore:
        :param password:
        :return:
        """
        return await V3KeystoreCrypto.decrypt_phrase(keystore=keystore, password=password)

    def generate_encrypted_private_key(
        self, password: str, private_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Can be stored (written to disk) and transferred.

        :param private_key:
        :param password:
        :return: Dictionary, use json.dumps()
        """
        private_key = private_key or self.generate_private_key()
        return eth_keyfile.create_keyfile_json(
            private_key=bytes.fromhex(private_key),
            password=password.encode("utf-8"),
            kdf="scrypt",
        )

    def decrypt_private_key(self, data: dict, password: str):
        if self.is_valid_json_private_key(data):
            wallet = eth_keyfile.decode_keyfile_json(
                raw_keyfile_json=data, password=password.encode("utf-8")
            )
            return wallet.hex()

    @staticmethod
    def get_master_key_from_mnemonic(
        phrase: str, derivation_path: str = BIP_44_PATHS.CONSTELLATION_PATH.value
    ):
        """
        Master key can be used to derive HD keys.

        :param phrase:
        :param derivation_path:
        :return:
        """
        bip32 = Bip32Helper()
        return bip32.get_master_key_from_mnemonic(phrase, path=derivation_path)

    @staticmethod
    def derive_account_from_master_key(master_key: BIP32Key, index: int) -> str:
        """
        Derive HD private key from master key.

        :param master_key:
        :param index:
        :return:
        """
        account_key = master_key.ChildKey(index)
        return account_key.PrivateKey().hex()

    @staticmethod
    def get_extended_private_key_from_mnemonic(mnemonic: str):
        # Extended keys can be used to derive child keys
        bip39 = Bip39Helper()
        bip32 = Bip32Helper()
        if bip39.validate_mnemonic(mnemonic):
            seed_bytes = bip39.get_seed_from_mnemonic(mnemonic)
            root_key = bip32.get_root_key_from_seed(seed_bytes)
            return root_key.ExtendedKey()

    @staticmethod
    def get_private_key_from_mnemonic(
        phrase: str, derivation_path = BIP_44_PATHS.CONSTELLATION_PATH.value
    ) -> str:
        """
        Get private key from phrase. Returns the first account.

        :param phrase:
        :param derivation_path:
        :return: Private key as hexadecimal string
        """
        bip32 = Bip32Helper()
        bip39 = Bip39Helper()
        seed = bip39.get_seed_from_mnemonic(phrase)
        private_key = bip32.get_private_key_from_seed(seed=seed, path=derivation_path)
        return private_key.hex()

    @staticmethod
    def get_public_key_from_private(private_key: str) -> str:
        """
        :param private_key:
        :return: Public key (Node ID)
        """
        bip32 = Bip32Helper()
        return bip32.get_public_key_from_private_hex(
            private_key=bytes.fromhex(private_key)
        )

    @staticmethod
    def get_dag_address_from_public_key(public_key: str) -> str:
        """
        :param public_key: The private key as a hexadecimal string.
        :return: The DAG address corresponding to the public key (node ID).
        """
        if len(public_key) == 128:
            public_key = PKCS_PREFIX + "04" + public_key
        elif len(public_key) == 130 and public_key[:2] == "04":
            public_key = PKCS_PREFIX + public_key
        else:
            raise ValueError("KeyStore :: Not a valid public key.")

        public_key = hashlib.sha256(bytes.fromhex(public_key)).hexdigest()
        public_key = base58.b58encode(bytes.fromhex(public_key)).decode()
        public_key = public_key[len(public_key) - 36 :]

        check_digits = "".join([char for char in public_key if char.isdigit()])
        check_digit = 0
        for n in check_digits:
            check_digit += int(n)
            if check_digit >= 9:
                check_digit = check_digit % 9

        address = f"DAG{check_digit}{public_key}"
        return address

    def get_dag_address_from_private_key(self, private_key: str):
        public_key = self.get_public_key_from_private(private_key=private_key)
        return self.get_dag_address_from_public_key(public_key=public_key)

    @staticmethod
    def get_eth_address_from_public_key(public_key: str) -> str:
        eth_address = eth_utils.keccak(bytes.fromhex(public_key))[-20:]
        return "0x" + eth_address.hex()

    def get_eth_address_from_private_key(self, private_key: str) -> str:
        public_key = self.get_public_key_from_private(private_key=private_key)[2:]  # Removes the 04 prefix from public key
        return self.get_eth_address_from_public_key(public_key=public_key)
