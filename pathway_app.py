import pathway as pw
from pathway.xpacks.llm.vector_store import VectorStoreServer
from pathway.xpacks.llm.embedders import OpenAIEmbedder

# Folder where PDFs are added/edited
DATA_DIR = "medical_docs"

# Read documents as a live stream
docs = pw.io.fs.read(
    DATA_DIR,
    format="binary",
    with_metadata=True
)

# Convert binary → text
docs = docs.select(
    text=pw.utils.parse_pdf(docs.data),
    path=docs.path
)

# Create live vector store
vector_store = VectorStoreServer(
    docs,
    embedder=OpenAIEmbedder(
        model="text-embedding-3-small",
        api_key="YOUR_OPENAI_API_KEY"
    )
)

# Run Pathway app
pw.run()
