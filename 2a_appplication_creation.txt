import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=30)
        return response.text
    except requests.exceptions.Timeout:
        return '{"error": "Request timed out. Please check your internet connection."}'
    except requests.exceptions.ConnectionError:
        return '{"error": "Cannot connect to the emotion detection service. Please check your network/firewall settings."}'
    except Exception as e:
        return f'{{"error": "{str(e)}"}}'