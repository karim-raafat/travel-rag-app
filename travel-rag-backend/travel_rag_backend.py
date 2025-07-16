import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import AzureOpenAI
from dotenv import load_dotenv
app = Flask(__name__)
CORS(app)

load_dotenv()

# Azure OpenAI Configuration
endpoint = os.get("endpoint")
open_ai_key = os.get("open_ai_key")
chat_model = "gpt-4o"
embedding_model = "text-embedding-ada-002"
search_url = os.get("search_url")
search_key = os.get("search_key")
index_name = os.get("index_name")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=open_ai_key,
    azure_endpoint=endpoint,
    api_version="2024-05-01-preview",
)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    prompt = [
        {"role": "system", "content": "You are a travel assistant that provides information on travel services available from Margie's Travel."},
        {"role": "user", "content": user_input}
    ]

    # RAG parameters
    rag_params = {
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": search_url,
                    "index_name": index_name,
                    "authentication": {
                        "type": "api_key",
                        "key": search_key,
                    },
                    "query_type": "vector",
                    "embedding_dependency": {
                        "type": "deployment_name",
                        "deployment_name": embedding_model,
                    },
                }
            }
        ]
    }

    try:
        response = client.chat.completions.create(
            model=chat_model,
            messages=prompt,
            extra_body=rag_params
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
