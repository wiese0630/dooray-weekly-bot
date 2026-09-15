import requests

WEBHOOK_URL = "여기에_Dooray_Incoming_URL"

message = "📢 점심 메뉴 11시까지 추천 받습니다."

response = requests.post(
    WEBHOOK_URL,
    json={"text": message}
)

print(response.status_code)
print(response.text)

response.raise_for_status()
