
import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Check the status code of the response
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the actual emotion scores dictionary
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion (the key with the maximum value)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Add the dominant emotion back into the dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion

    # Return the complete dictionary containing scores AND the dominant emotion
    return emotion_scores