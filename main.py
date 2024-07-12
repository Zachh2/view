from flask import Flask, request, jsonify
import requests, random
from getuseragent import UserAgent

app = Flask(__name__)

@app.route('/boost', methods=['GET'])
def boost():
    user = request.args.get('username')
    link = request.args.get('link')
    
    if not user or not link:
        return jsonify({"error": "Missing username or link"}), 400

    ua = UserAgent("ios").Random()
    
    response = requests.post(
        'https://api.likesjet.com/freeboost/3',
        json={
            "link": link,
            "tiktok_username": user,
            "email": f"shiki{random.randint(100000,999999)}@gmail.com"
        },
        headers={
            "Host": "api.likesjet.com",
            "content-length": "137",
            "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": ua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://likesjet.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://likesjet.com/",
            "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"
        }
    )

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=8080)
