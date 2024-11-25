from flask import Flask, request, jsonify
from flask_cors import CORS  # 导入 CORS
from openai import OpenAI
import os
import time

deepseek_api = os.environ.get("DEEPSEEK_API")
deepseek_url = "https://api.deepseek.com"

openai_api_key = os.environ.get("OPENAI_API_KEY")
charanywhere_api_url = "https://api.chatanywhere.tech"

def send_request(user_input, need_print=False):
    client = OpenAI(api_key=deepseek_api, base_url=deepseek_url)
    # client = OpenAI(api_key=openai_api_key, base_url=charanywhere_api_url)
    message = [{"role": "system", "content": "You are a helpful assistant"}]
    message.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",
        # model="gpt-3.5-turbo-0125",
        messages=message,
        stream=True  # 启用流式输出
    )

    response_text = ""
    for chunk in response:
        if hasattr(chunk.choices[0].delta, 'content'):
            chunk_text = chunk.choices[0].delta.content
            if chunk_text == None:
                break
            response_text += chunk_text
            yield f'{{"response": "{chunk_text}"}}headinclouds'  # 修改为逐步返回



app = Flask(__name__)
CORS(app)  # 启用跨域支持

from flask import Response

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')

    def generate():
        for part in send_request(user_message):
            yield part

    return Response(generate(), content_type='application/json;charset=utf-8')

if __name__ == '__main__':
    app.run(port=5000)

