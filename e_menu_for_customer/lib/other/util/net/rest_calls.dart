import 'package:dio/dio.dart';

import '../api_keys.dart';

class RESTCalls{
  static Future get(String extension) async {
    Dio dio = new Dio();
    Response response;

    response = await dio.get('https://www.emenu.services/api/$extension',
        options: Options(headers: {"Authorization": "Api-Key ${getkey()}"}));
    if (response.statusCode == 200) {
      return response.data;
    } else {
      return false;
    }
  }

  static Future post(String extension,
      {Map<String, String> headers, FormData data}) async {
    Response response;
    Dio dio = new Dio();

    response = await dio.post('https://www.emenu.services/api/$extension/',
        options: Options(headers: {"Authorization": "Api-Key ${getkey()}"}),
        data: data);
    if (response.statusCode == 200) {
      return true;
    } else {
      return false;
    }
  }

  static Future update(String extension, {FormData data}) async {
    Dio dio = new Dio();
    Response response;
    response = await dio.patch('https://www.emenu.services/api/$extension',
        options: Options(headers: {"Authorization": "Api-Key ${getkey()}"}),
        data: data);
    print(response);
    if (response.statusCode == 200) {
      return true;
    } else {
      return false;
    }
  }
}