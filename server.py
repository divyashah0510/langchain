from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

# 1. Create a prompt template
system_template = "Suggest me some good recipe that are {recipe_type}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# 2. Creating a model
model = ChatGroq()

# 3. Create a parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser

# 5. App Definition
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple suggestion API server using Langchain's Runnable interfaces",
)

# 6. Adding chain routes
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
    
# Run the port on http://localhost:8000/chain/playground/
