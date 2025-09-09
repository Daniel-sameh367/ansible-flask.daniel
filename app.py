from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# الصفحة HTML كلها هنا
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Welcome to My Project!</h1>

    <input type="text" id="inputText" placeholder="Type something">
    <button id="btn">Send to Backend</button>

    <p id="response"></p>

    <script>
        document.getElementById('btn').onclick = async () => {
            const text = document.getElementById('inputText').value;
            const res = await fetch('/process', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text})
            });
            const data = await res.json();
            document.getElementById('response').innerText = data.reply;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_text = data.get('text', '')
    # هنا ممكن تحط أي عملية Backend على النص
    reply = f"You sent: {user_text}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50003)

