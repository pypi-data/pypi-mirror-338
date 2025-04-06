from typing import Final, Tuple

from alkindi import core
from alkindi.core import OQS_SUCCESS

STANDARDIZED_SIGNATURES_ALGORITHMS: Final[tuple[str, ...]] = (
    "ML-DSA-44",
    "ML-DSA-65",
    "ML-DSA-87",
)


class Signature:
    """
    A Python wrapper for the C liboqs OQS_SIG struct, providing a signature scheme interface.

    This class encapsulates keypair generation, signing, and verification operations,
    mirroring key fields of the underlying OQS_SIG struct for clarity. It manages resources
    via the context manager protocol and supports various signature algorithms.

    Method mappings to C liboqs:
        Python            |  C liboqs
        ------------------|------------
        generate_keypair  |  OQS_SIG_keypair
        sign              |  OQS_SIG_sign
        verify            |  OQS_SIG_verify
    """


    def __init__(self, alg_name: str) -> None:
        """
        Initialize the signature scheme with a given algorithm.

        Constructs an OQS_SIG object and checks for NULL returns, indicating an invalid
        or disabled algorithm at compile-time.

        Args:
            alg_name (str): A supported signature algorithm name from STANDARDIZED_SIGNATURES_ALGORITHMS.

        Raises:
            ValueError: If alg_name is not in STANDARDIZED_SIGNATURES_ALGORITHMS or not supported by liboqs.
        """
        if alg_name not in STANDARDIZED_SIGNATURES_ALGORITHMS:
            raise ValueError(
                f"Algorithm must be one of {STANDARDIZED_SIGNATURES_ALGORITHMS}, got {alg_name}"
            )

        self._sig = core.liboqs.OQS_SIG_new(alg_name.encode("utf-8"))
        if self._sig == core.ffi.NULL:
            raise ValueError(f"Algorithm {alg_name} is not supported by liboqs")

        self.method_name = core.ffi.string(self._sig.method_name).decode("utf-8")
        self.alg_version = core.ffi.string(self._sig.alg_version).decode("utf-8")
        self.claimed_nist_level = self._sig.claimed_nist_level
        self.length_public_key = self._sig.length_public_key
        self.length_secret_key = self._sig.length_secret_key
        self.length_signature = self._sig.length_signature


    def __enter__(self) -> "Signature":
        """
        Enter the context manager, providing the Signature instance for use in a `with` block.

        Runs at the start of a `with` statement (e.g., `with Signature("algorithm") as sig:`).
        No additional setup is performed beyond `__init__`.

        Returns:
            Signature: The current instance, ready for signing operations.
        """
        return self


    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Exit the context manager, freeing the OQS_SIG object to prevent memory leaks.

        Called when the `with` block ends, ensuring proper cleanup of C resources.

        Args:
            exc_type: Type of exception (if any), else None.
            exc_value: Exception instance (if any), else None.
            traceback: Traceback object (if any), else None.
        """
        if hasattr(self, "_secret_key"):
            secret_key_ptr = core.ffi.from_buffer(self._secret_key)
            core.liboqs.OQS_MEM_cleanse(secret_key_ptr, len(self._secret_key))
            self._secret_key = None

        if self._sig is not None:
            core.liboqs.OQS_SIG_free(self._sig)
            self._sig = None


    def generate_keypair(self) -> Tuple[bytes, bytes]:
        """
        Generate a keypair (public/secret) for the signature scheme.

        Allocates memory for public_key and secret_key based on self.length_public_key
        and self.length_secret_key, then invokes the C keypair generation function.

        Returns:
            Tuple[bytes, bytes]: A tuple of (public_key, secret_key) as Python bytes objects.

        Raises:
            RuntimeError: If keypair generation fails (e.g., due to internal liboqs error).
            MemoryError: If memory allocation fails for public or secret key.
        """
        public_key = core.ffi.new("uint8_t[]", self.length_public_key)
        if public_key == core.ffi.NULL:
            raise MemoryError("Failed to allocate memory for public key")

        secret_key = core.ffi.new("uint8_t[]", self.length_secret_key)
        if secret_key == core.ffi.NULL:
            raise MemoryError("Failed to allocate memory for secret key")

        result = core.liboqs.OQS_SIG_keypair(self._sig, public_key, secret_key)
        if result != OQS_SUCCESS:
            raise RuntimeError(f"Failed to generate keypair for {self.method_name}")

        self._secret_key = bytes(secret_key)

        return bytes(public_key), bytes(secret_key)


    def sign(self, message: bytes, secret_key: bytes) -> bytes:
        """
        Signature generation algorithm.

        Allocates a signature buffer based on self.length_signature and generates a signature.
        The actual signature length may be less than the maximum, as returned via signature_len.

        Args:
            message (bytes): The message to sign.
            secret_key (bytes): The secret key from generate_keypair, must match self.length_secret_key.

        Returns:
            bytes: The signature as a Python bytes object.

        Raises:
            RuntimeError: If signing fails (e.g., invalid secret key or internal error).
            ValueError: If secret_key length does not match self.length_secret_key.
            MemoryError: If memory allocation fails for signature or signature length.
        """
        if len(secret_key) != self.length_secret_key:
            raise ValueError(
                f"Secret key length {len(secret_key)} does not match expected {self.length_secret_key}"
            )

        signature = core.ffi.new("uint8_t[]", self.length_signature)
        if signature == core.ffi.NULL:
            raise MemoryError("Failed to allocate memory for signature")

        signature_len = core.ffi.new("size_t *", self.length_signature)
        if signature_len == core.ffi.NULL:
            raise MemoryError("Failed to allocate memory for signature length")

        result = core.liboqs.OQS_SIG_sign(
            self._sig, signature, signature_len, message, len(message), secret_key
        )
        if result != OQS_SUCCESS:
            raise RuntimeError(f"Failed to sign message with {self.method_name}")

        return bytes(signature[0 : signature_len[0]])


    def verify(self, message: bytes, signature: bytes, public_key: bytes) -> bool:
        """
        Signature verification algorithm.

        Checks the validity of a signature against a message and public key.

        Args:
            message (bytes): The signed message.
            signature (bytes): The signature to verify.
            public_key (bytes): The public key from generate_keypair, must match self.length_public_key.

        Returns:
            bool: True if the signature is valid, False otherwise.

        Raises:
            ValueError: If public_key length does not match self.length_public_key.
        """
        if len(public_key) != self.length_public_key:
            raise ValueError(
                f"Public key length {len(public_key)} does not match expected {self.length_public_key}"
            )

        result = core.liboqs.OQS_SIG_verify(
            self._sig, message, len(message), signature, len(signature), public_key
        )
        return result == OQS_SUCCESS


__all__ = ["Signature"]
