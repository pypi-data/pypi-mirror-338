# SGX Storage Client

A secure Python client for Intel SGX enclave communication implementing DCAP remote attestation and AES-GCM encrypted sessions. Designed for managing sensitive configurations in trusted execution environments.

## Features

- **Secure Session Protocol** - Ephemeral ECDH key exchange + AES-128-GCM encryption
- **DCAP Remote Attestation** - Verify enclave identity through Intel's Quote Verification Service
- **Complete Management API**:
  - Exchange account credentials storage
  - Blockchain address whitelisting
  - Multi-role user access control
  - Network/currency configuration management
- **Production-Ready Security**:
  - MRSIGNER-based enclave verification
  - Anti-replay protection with session nonce
  - CMAC-based key derivation (NIST SP 800-108)
  - Hardware-rooted trust chain

## Installation

```bash
pip install sgx-storage-client
```

## Components

- **SGX Client** (client.py)

  Main interface for enclave communication:

```python
from sgx.client import SgxClient
from sgx.attestaion import SGXAttestationVerifier

client = SgxClient(
    host="enclave.example.com",
    port=2241,
    spid="11223344556677889900AABBCCDDEEFF",  # 16-byte hex Service Provider ID
    private_value=680592519268687832738673940181144757182820103, # Private key for enclave authentication
    attestation_verifier=SGXAttestationVerifier(
        mr_signer="a1b2c3d4e5f6...", # Trusted enclave fingerprint
        dcap_url="https://qvs.example.com/qvs/attestation/sgx/dcap/v1/report"
    )  # Optional, use None to skip dcap verification
)
```
- **Attestation Module** (attestation.py)

  Interface for enclave attestation:
```python
from sgx.attestaion import SGXAttestationVerifier

verifier = SGXAttestationVerifier(
    mr_signer="trusted_enclave_hash",
    dcap_url="https://qvs.example.com/qvs/attestation/sgx/dcap/v1/report"
)
```
- **Session Handler (session.py)**

  Manages secure channel:

  - Automatic attestation protocol (MSG0-MSG4)
  - Session key derivation
  - Encrypted payload handling

### Example usage
#### Exchange Account Management
```python
client.get_accounts()

client.add_account(
   name='main-account', 
   exchange='binance', 
   public_key='public-key',
   key='sercret-key', 
   sorting_key=1, 
   additional_data={}
)

client.update_account(
   account_id='1binance', 
   name='secondary-account', 
   public_key='public-key', 
   key='secret-key', 
   sorting_key=1, 
   additional_data={}
)

client.del_account('1binance')
```
#### Address Management
```python
client.get_standalone_addresses()

client.add_standalone(
    address='0xC8CD2BE653759aed7B0996315821AAe71e1FEAdF',
    network='ETHEREUM',
    alias='eth-address',
    whitelist=True,
    multisig=False,
    currencies=['ETH', 'USDT'],
    sorting_key=1
)

client.update_standalone(
    address='0xC8CD2BE653759aed7B0996315821AAe71e1FEAdF',
    network='ETHEREUM',
    alias='eth-address-2',
    whitelist=True,
    multisig=False,
    currencies=[],
    sorting_key=1
)

client.del_standalone(address='0xC8CD2BE653759aed7B0996315821AAe71e1FEAdF', network='ETHEREUM')
```

#### Whitelist Management

```python
client.get_whitelist()

client.add_whitelist(
    address='0xC8CD2BE653759aed7B0996315821AAe71e1FEAdF',
    network='ETHEREUM',
    alias='trusted-address',
    currencies=[],
    sorting_key=1
)

client.update_whitelist(
   address='0xC8CD2BE653759aed7B0996315821AAe71e1FEAdF',
   network='ETHEREUM',
   alias='trusted-address-2'
)

client.del_whitelist(
    address='0xC8CD2BE653759aed7B0996315821AAe71e1FEAdF',
    network='ETHEREUM',
)
```

#### User Management

```python
client.get_users()

client.add_user(
    user='test@gamil.com', 
    role='FULL_ACCESS', 
    sorting_key=2
)

client.update_user(user='test@gamil.com', role='READ_ONLY', sorting_key=2)

client.del_user('test@gamil.com')

client.reset_user_hotp('test@gamil.com')
```

#### configurations

```python
client.get_network_coins()

client.get_status()
```
