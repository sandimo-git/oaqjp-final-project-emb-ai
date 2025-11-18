import json
from urllib import request, error

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {"raw_document": {"text": text_to_analyse}}
    data = json.dumps(payload).encode('utf-8')

    req = request.Request(url, data=data, headers=headers, method='POST')
    try:
        with request.urlopen(req) as resp:
            if resp.status == 200:
                result = resp.read()
                response_data = json.loads(result)
                emotion_data = response_data['emotionPredictions'][0]['emotion']
                scores = {
                    'anger': emotion_data.get('anger', 0),
                    'disgust': emotion_data.get('disgust', 0),
                    'fear': emotion_data.get('fear', 0),
                    'joy': emotion_data.get('joy', 0),
                    'sadness': emotion_data.get('sadness', 0)
                }
                dominant_emotion = max(scores, key=scores.get)
                return {'label': dominant_emotion.capitalize()}

            elif status_code == 400:
                return{
                    'anger': scores['None'],
                    'disgust': scores['None'],
                    'fear': scores['None'],
                    'joy': scores['None'],
                    'sadness': scores['None'],
                    'The dominant emotion is': ['None']
                }  
            else:
                return None
    except error.URLError as e:
        print(f"Request error: {e}")
        return None