import 'package:flutter/material.dart';

class ChatField extends StatelessWidget {
  final TextEditingController controller;
  final Function(String) onSubmitted;
  ChatField({super.key, required this.controller, required this.onSubmitted});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: TextField(
            controller: controller,
            onSubmitted: (value) => onSubmitted(value),
            decoration: InputDecoration(
              hintText: 'Type your message...',
              hintStyle: TextStyle(color: Colors.white70),
              filled: true,
              fillColor: Colors.grey[800],
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
              ),
            ),
          ),
        ),
        const SizedBox(width: 8),
        Container(
          decoration: const BoxDecoration(
            shape: BoxShape.circle,
            color: Colors.white,
          ),
          child: IconButton(
            icon: const Icon(Icons.send),
            onPressed: () {
              if (controller.text.isNotEmpty) {
                onSubmitted(controller.text);
                controller.clear();
              }
            },
          ),
        ),
      ],
    );
  }
}
