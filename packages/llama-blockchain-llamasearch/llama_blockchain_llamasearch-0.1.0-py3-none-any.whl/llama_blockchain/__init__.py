"""
llama_blockchain: A comprehensive blockchain integration package for LLM applications.

This package provides tools for verifying blockchain data, tracking data provenance,
generating zero-knowledge proofs, and interacting with various blockchain features
like tokens, NFTs, DAOs, and decentralized ranking systems.
"""

__version__ = "0.1.0"

try:
    import web3
except ImportError:
    print("Warning: web3.py is not installed. Ethereum connectivity features will not work.")
    print("To enable full functionality, install with: pip install llama_blockchain[ethereum]")

from .blockchain_verifier import BlockchainVerifier
from .contract_validator import ContractValidator  # Corrected: using renamed file
from .blockchain_exceptions import (  # Corrected: removed .exceptions
    BlockchainError,
    ContractValidationError,
    ProvenanceError,
    TransactionError,
    ZKProofError,
)
from .dao_manager import DAOManager  # Corrected: removed .managers
from .nft_manager import NFTManager  # Corrected: removed .managers
from .ranking_manager import RankingManager  # Corrected: removed .managers
from .token_manager import TokenManager  # Corrected: removed .managers
from .provenance_tracker import ProvenanceTracker
from .zk_prover import ZKProver

__all__ = [
    "BlockchainVerifier",
    "ContractValidator",
    "ProvenanceTracker",
    "ZKProver",
    "DAOManager",
    "NFTManager",
    "RankingManager",
    "TokenManager",
    "BlockchainError",
    "ContractValidationError",
    "ProvenanceError",
    "ZKProofError",
    "TransactionError",
]
