import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip(): 
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    resp = requests.post(url, headers=headers, json=input_json)

    if resp.status_code == 200:
        response_dict = json.loads(resp.text)
        emotions = response_dict.get('emotion_predictions', {})
        scores = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0)
            }

        dominant_emotion = max(scores, key=scores.get)
        scores['dominant_emotion'] = dominant_emotion

        return scores 
    else: 
        return f"Error: {resp.status_code}"  
