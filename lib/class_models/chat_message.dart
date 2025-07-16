class ChatMessage {
  final ChatMessageRole role;
  final String content;

  ChatMessage({required this.role, required this.content});
}

enum ChatMessageRole {
  user,
  assistant,
}
