# Evaluator Submission Guide

This version incorporates the feedback from the previous evaluator submission.

## Q1
Create the public GitHub repository with the exact required name:
`oaqjp-final-project-emb-ai`

README must explicitly contain:
`Final Project`

Submit the public README URL.

## Q2
Paste the complete `EmotionDetection/emotion_detection.py` into `2a_emotion_detection`.
It explicitly shows the EmotionPredict endpoint, required model-ID header, raw_document payload, POST request, and response.text processing.

## Q3
Use a real terminal transcript, not only a custom success sentence. Example:
```text
PS D:\VU\Sem5\...\oaqjp-final-project-emb-ai> python
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> print(emotion_detector("I am very happy today"))
{'anger': ..., 'disgust': ..., 'fear': ..., 'joy': ..., 'sadness': ..., 'dominant_emotion': 'joy'}
```
The final dictionary requires the Watson service to be reachable.

## Q4
Paste the complete `emotion_detection.py` with the required output dictionary and dominant emotion calculation.

## Q5
Paste the actual successful Watson output showing all five scores and `dominant_emotion`.

Do not fabricate values if the Watson endpoint is unreachable.

## Q6
Submit the public GitHub URL for:
`EmotionDetection/__init__.py`
The repository name must be `oaqjp-final-project-emb-ai`.

## Q7
Submit a real terminal transcript including:
```text
from EmotionDetection.emotion_detection import emotion_detector
print(emotion_detector("I am very happy today"))
{... emotion scores ..., 'dominant_emotion': 'joy'}
```

## Q8
Paste `test_emotion_detection.py`.

## Q9
Run:
```powershell
python -m unittest test_emotion_detection.py -v
```
Expected successful ending:
```text
Ran 5 tests in ...s

OK
```

## Q10
Paste the complete `server.py`. It now returns the evaluator-required formatted response string containing all five emotions and dominant emotion.

## Q11
Run `python server.py`, open `http://127.0.0.1:5000`, enter a sentence, and capture the screenshot only after the result is visibly displayed. Save as `6b_deployment_test.png`.

## Q12
Paste the complete `emotion_detector` function including the explicit 400 handling, endpoint, header, payload, response processing, and None dictionary.

## Q13
Paste the complete `server.py`, not only the blank-input lines. It includes Flask imports/routes, blank input handling, and formatted response.

## Q14
Clear the text area and submit empty input. The interface must visibly show exactly:
`Invalid input! Try again.`
Capture as `7c_error_handling_interface.png`.

## Q15
Paste complete `server.py`.

## Q16
Run:
```powershell
pylint server.py
```
Submit terminal output showing the Pylint score. Aim for 10.00/10.

## Important
The previous evaluator feedback showed that partial snippets and generic success messages were not enough. For code questions, paste the complete relevant file/function. For terminal questions, paste the real terminal transcript. For screenshots, capture the completed state, not the loading state.
