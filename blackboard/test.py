import unittest
from unittest.mock import patch
from main import Blackboard, TextExtractor, SentimentAnalyzer, ResultViewer, Controller

class TestBlackboardPattern(unittest.TestCase):
    def test_process_social_media_data(self):
        blackboard = Blackboard()
        controller = Controller(blackboard)

        text_extractor = TextExtractor(blackboard)
        sentiment_analyzer = SentimentAnalyzer(blackboard)

        controller.add_knowledge_source(text_extractor)
        controller.add_knowledge_source(sentiment_analyzer)

        social_media_data = "I'm feeling great today! It's a beautiful sunny day."

        with patch.object(ResultViewer, 'display_result') as mock_display_result:
            controller.process_social_media_data(social_media_data)

            mock_display_result.assert_called_once()

    def test_text_extractor(self):
        blackboard = Blackboard()
        text_extractor = TextExtractor(blackboard)

        social_media_data = "I'm feeling great today! It's a beautiful sunny day."

        text_extractor.extract_text(social_media_data)

        self.assertEqual(blackboard.get_data('text'), social_media_data)

    def test_sentiment_analyzer(self):
        blackboard = Blackboard()
        sentiment_analyzer = SentimentAnalyzer(blackboard)

        blackboard.set_data('text', "I'm feeling great today!")

        sentiment_analyzer.analyze_sentiment()

        self.assertIsNotNone(blackboard.get_data('sentiment'))

    def test_result_viewer(self):
        blackboard = Blackboard()
        result_viewer = ResultViewer(blackboard)

        blackboard.set_data('text', "I'm feeling great today!")
        blackboard.set_data('sentiment', 0.8)

        with patch('builtins.print') as mock_print:
            result_viewer.display_result()

            mock_print.assert_called_with("Sentiment:", 0.8)

if __name__ == "__main__":
    unittest.main()
