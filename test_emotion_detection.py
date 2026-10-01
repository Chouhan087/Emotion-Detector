"""Unit tests for the EmotionDetection application."""

import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


def mock_response(emotions):
    """Create a mocked Watson response."""
    response = Mock()
    response.status_code = 200
    response.text = json.dumps({
        "emotionPredictions": [{"emotion": emotions}]
    })
    return response


class TestEmotionDetector(unittest.TestCase):
    """Test dominant-emotion detection for all five emotions."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value = mock_response({
            "anger": 0.01, "disgust": 0.01, "fear": 0.01,
            "joy": 0.95, "sadness": 0.02
        })
        result = emotion_detector("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value = mock_response({
            "anger": 0.95, "disgust": 0.01, "fear": 0.01,
            "joy": 0.01, "sadness": 0.02
        })
        result = emotion_detector("I am angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        mock_post.return_value = mock_response({
            "anger": 0.01, "disgust": 0.95, "fear": 0.01,
            "joy": 0.01, "sadness": 0.02
        })
        result = emotion_detector("This is disgusting")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        mock_post.return_value = mock_response({
            "anger": 0.01, "disgust": 0.01, "fear": 0.95,
            "joy": 0.01, "sadness": 0.02
        })
        result = emotion_detector("I am afraid")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        mock_post.return_value = mock_response({
            "anger": 0.01, "disgust": 0.01, "fear": 0.01,
            "joy": 0.02, "sadness": 0.95
        })
        result = emotion_detector("I am sad")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
