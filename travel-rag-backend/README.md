# Travel RAG App - Chat History Implementation

## Overview
This update adds chat history context to the travel RAG chatbot, allowing the backend to maintain conversation context and provide more relevant, personalized responses.

## Changes Made

### Backend (Python)
- **Updated endpoint**: `/chat` now accepts both single messages (legacy) and full chat history (new)
- **Added system message**: Provides travel assistant context for better responses
- **Improved error handling**: Better logging and error messages
- **CORS support**: Added for potential web deployment
- **Backward compatibility**: Maintains support for single message requests

### Frontend (Flutter)
- **Enhanced ChatMessage model**: Added JSON serialization/deserialization
- **New API method**: `sendChatHistoryToBackend()` sends full conversation context
- **Updated ChatProvider**: Now sends entire chat history instead of just the latest message
- **Maintained UI compatibility**: No changes to the user interface

## New Features

### Context-Aware Responses
The backend now receives the full conversation history, enabling:
- Follow-up questions that reference previous messages
- Consistent recommendations across the conversation
- Better understanding of user preferences mentioned earlier
- More natural conversation flow

### Backward Compatibility
The backend supports both:
- **Legacy format**: `{"message": "single message"}`
- **New format**: `{"messages": [{"role": "user", "content": "..."}]}`

## Installation

### Backend Dependencies
```bash
cd travel-rag-backend
pip install -r requirements.txt
```

### Running the Backend
```bash
cd travel-rag-backend
python travel_rag_backend.py
```

### Testing
Run the test script to verify both message formats work:
```bash
cd travel-rag-backend
python test_chat_history.py
```

## Usage Examples

### Single Message (Legacy)
```json
{
  "message": "What are the best places to visit in Paris?"
}
```

### Chat History (New)
```json
{
  "messages": [
    {"role": "user", "content": "I'm planning a trip to France"},
    {"role": "assistant", "content": "Great! What type of experience are you looking for?"},
    {"role": "user", "content": "I love history and museums"}
  ]
}
```

## Technical Details

### Message Flow
1. User types message in Flutter app
2. ChatProvider adds user message to conversation history
3. Full conversation history sent to backend via `ApiService.sendChatHistoryToBackend()`
4. Backend adds system message for travel context
5. Azure OpenAI processes conversation with RAG context
6. Response returned and added to conversation history

### System Message
A system message is automatically added to provide context:
```
"You are a helpful travel assistant powered by a comprehensive travel knowledge base. 
Use the retrieved context to provide accurate, helpful, and personalized travel advice. 
Consider the conversation history to maintain context and provide consistent recommendations."
```

## Benefits
- **Better Context**: Responses consider previous conversation
- **Personalization**: Remembers user preferences mentioned earlier
- **Natural Flow**: Allows for follow-up questions and clarifications
- **Consistency**: Recommendations align with previous suggestions
- **Enhanced UX**: More natural, human-like conversation experience
