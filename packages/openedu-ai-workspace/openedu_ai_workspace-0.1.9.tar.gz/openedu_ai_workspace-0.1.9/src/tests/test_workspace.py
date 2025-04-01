from ai_workspace import Workspace
import os
from dotenv import load_dotenv
from ai_workspace.schemas import WorkspaceSchema
# Tải các biến từ file .env
load_dotenv()
def test_workspace():
    qdrant_uri = os.getenv("QDRANT_URI")
    qdrant_api_key = os.getenv("API_KEY_QDRANT")
    qdrant_port = os.getenv("QDRANT_URL")
    azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_deployment = os.getenv("DEPLOYMENT_NAME_GPT4")    
    azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    workspace = Workspace(
        mongodb_url="mongodb+srv://lochoang611:K8ZvBbaPL8jvyLEa@cluster0.nnwioc9.mongodb.net/example",
        qdrant_uri=qdrant_uri,
        qdrant_api_key=qdrant_api_key,
        qdrant_port=qdrant_port,
        azure_api_key=azure_api_key,
        azure_endpoint=azure_endpoint,
        azure_deployment=azure_deployment,
        azure_api_version=azure_api_version,
        
    )
    workspace_data = WorkspaceSchema(
        description="test",
        instructions="test",
        title="test",
        user_id="test",
        chat_session=["213","213q21"]
    )
    id=workspace.add_workspace(workspace_data)
    print(workspace.get_instructions(id))
test_workspace()