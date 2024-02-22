import requests

# APIのURL
url = 'https://2804-123-226-12-83.ngrok-free.app/shortest-path/'

# スタートとゴールの情報を辞書で定義
data = {
    'start': 'G',
    'goal': 'S'
}

# POSTリクエストを送る
response = requests.post(url, json=data)

# レスポンスの確認
if response.status_code == 200:
    # JSON形式で結果を表示
    print(response.json())
else:
    print("Error:", response.status_code)
