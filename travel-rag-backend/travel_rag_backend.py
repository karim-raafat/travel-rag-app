import json
from flask import Flask, request, jsonify
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

chat_client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("endpoint"),
    api_key=os.getenv("open_ai_key")
)

chat_model = "gpt-4o"
embedding_model = "text-embedding-ada-002"
search_url = os.getenv("search_url")
search_key = os.getenv("search_key")
index_name = os.getenv("index_name")

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        data = request.get_json(force=True)
        messages = data.get("messages")
        
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        elif messages and isinstance(messages, list):
            pass
        else:
            single_message = data.get("message")
            if single_message:
                messages = [{"role": "user", "content": single_message}]
            else:
                return jsonify({"error": "Invalid or missing 'messages' array or 'message' field"}), 400

        if not messages or messages[0].get("role") != "system":
            system_message = {
                "role": "system",
                "content": "You are a helpful travel assistant powered by a comprehensive travel knowledge base. "
            }
            messages = [system_message] + messages

        rag_params = {
            "data_sources": [
                {
                    "type": "azure_search",
                    "parameters": {
                        "endpoint": search_url,
                        "index_name": index_name,
                        "authentication": {
                            "type": "api_key",
                            "key": search_key
                        },
                        "query_type": "vector",
                        "embedding_dependency": {
                            "type": "deployment_name",
                            "deployment_name": embedding_model
                        }
                    }
                }
            ]
        }

        response = chat_client.chat.completions.create(
            model=chat_model,
            messages=messages,
            extra_body=rag_params
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
