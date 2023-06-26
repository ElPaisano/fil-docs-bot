from superpowered import create_knowledge_base, create_document_via_url
import os

os.environ["SUPERPOWERED_API_KEY_ID"] = ""
os.environ["SUPERPOWERED_API_KEY_SECRET"] = ""

knowledge_base_title = "What is Filecoin"
kb = create_knowledge_base(title=knowledge_base_title)
kb_id = kb["id"]

print(f"Created knowledge base with id: {kb_id}")

urls = [
    "https://docs.filecoin.io/basics/what-is-filecoin/overview/",
    "https://docs.filecoin.io/basics/what-is-filecoin/crypto-economics/",
    "https://docs.filecoin.io/basics/what-is-filecoin/blockchain/",
    "https://docs.filecoin.io/basics/what-is-filecoin/storage-model/",
    "https://docs.filecoin.io/basics/what-is-filecoin/storage-market/",
    "https://docs.filecoin.io/basics/what-is-filecoin/retrieval-market/",
    "https://docs.filecoin.io/basics/what-is-filecoin/programming-on-filecoin/",
    "https://docs.filecoin.io/basics/what-is-filecoin/networks/",
    "https://docs.filecoin.io/basics/the-blockchain/actors/",
    "https://docs.filecoin.io/basics/the-blockchain/addresses/",
    "https://docs.filecoin.io/basics/the-blockchain/tipsets/",
    "https://docs.filecoin.io/basics/the-blockchain/consensus/",
    "https://docs.filecoin.io/basics/the-blockchain/drand/",
    "https://docs.filecoin.io/basics/the-blockchain/proofs/"
]

for url in urls:
    create_document_via_url(knowledge_base_id=kb_id, url=url)
