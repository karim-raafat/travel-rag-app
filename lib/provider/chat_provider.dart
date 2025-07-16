import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:travel_rag_app/backend_services/api_service.dart';
import 'package:travel_rag_app/class_models/chat_message.dart';
import 'package:travel_rag_app/provider/chat_provider.dart';

class ChatNotifier extends StateNotifier<ChatState> {
  ChatNotifier() : super(ChatState(messages: []));

  Future<void> sendMessage(String userInput) async {
    // Add user message
    state = ChatState(messages: [
      ...state.messages,
      ChatMessage(role: ChatMessageRole.user, content: userInput),
    ], isLoading: true);

    try {
      final reply = await ApiService.sendMessageToBackend(userInput);
      state = ChatState(messages: [
        ...state.messages,
        ChatMessage(role: ChatMessageRole.assistant, content: reply),
      ], isLoading: false);
    } catch (e) {
      state = ChatState(messages: [
        ...state.messages,
        ChatMessage(
          role: ChatMessageRole.assistant,
          content: 'Error: ${e.toString()}',
        ),
      ], isLoading: false);
    }
  }

  void clearChat() {
    state = ChatState(messages: []);
  }
}

final chatProvider =
    StateNotifierProvider<ChatNotifier, ChatState>((ref) => ChatNotifier());

class ChatState {
  final List<ChatMessage> messages;
  final bool isLoading;

  ChatState({required this.messages, this.isLoading = false});
}
