import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String backendUrl = 'http://127.0.0.1:5000/chat';

  static Future<String> sendMessageToBackend(String message) async {
    final response = await http.post(
      Uri.parse(backendUrl),
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonEncode({'message': message}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['reply'];
    } else {
      throw Exception("Failed to get response from backend");
    }
  }
}
