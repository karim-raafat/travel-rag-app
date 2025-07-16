# 🌍 TravelRAG — Intelligent Travel Planning Assistant

TravelRAG is a smart and intuitive mobile application that helps users plan their travel experiences more efficiently. The app leverages powerful AI models deployed on Azure to provide brochure-grounded, conversational recommendations through a clean and responsive Flutter frontend.

## ✨ Key Features

- 🧳 **Conversational Travel Planning**: Chat with an AI assistant that recommends travel destinations and information based on real brochures.
- 📄 **Contextual Answers from Real Data**: Retrieves and uses content from actual PDF brochures.
- 🔐 **Simple, Private Interaction**: No login or account creation required — just ask and plan.
- 📱 **Cross-Platform**: Built using Flutter, the app runs smoothly on both Android and iOS devices.

## 🧠 Use of Azure AI

This application integrates Microsoft’s **Azure AI Studio** to power an intelligent, retrieval-augmented chat experience. It uses:

- **`text-embedding-ada-002`**: Converts PDF travel brochure content into vector embeddings for semantic search.
- **`gpt-4o`**: Generates context-aware responses to user queries based on retrieved content.

The Flask backend performs:

1. PDF preprocessing and indexing into a vector store using Azure Embeddings  
2. Retrieval of relevant chunks based on user input  
3. Contextual response generation with `gpt-4o`  

This allows the app to deliver accurate, real-time answers grounded in brochure-based travel data.

> 📚 Brochure Dataset:  
> The indexed travel data comes from Microsoft's sample brochure set, available [here](https://github.com/MicrosoftLearning/mslearn-ai-studio/raw/main/data/brochures.zip).

## 🧱 Tech Stack

| Layer     | Technology                |
|-----------|---------------------------|
| Frontend  | Flutter, Dart             |
| Backend   | Python, Flask             |
| AI Models | Azure AI Studio (text-embedding-ada-002, gpt-4o) |
| Data      | PDF Brochures             |
| Tools     | Android Studio, Postman   |

## 📁 Project Structure
travel_rag_app/
├── travel-rag-backend/ # Python Flask backend
│ ├── app.py
│ ├── vector_indexing.py
│ ├── .env # Environment file (excluded from Git)
│ └── ...
├── travel_rag_flutter/ # Flutter mobile app
│ ├── lib/
│ ├── android/
│ ├── ios/
│ └── ...
└── README.md


## 🚫 Notes

- Sensitive keys and endpoints have been removed from the `.env` file and are **not** tracked by Git.
- This project is complete and currently has **no planned updates**.

---


