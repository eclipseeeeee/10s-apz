class Blackboard:
    def __init__(self):
        self.data = {}

    def get_data(self, key):
        return self.data.get(key)

    def set_data(self, key, value):
        self.data[key] = value

class TextExtractor:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def extract_text(self, social_media_data):
        text = social_media_data  # Extract text from social media data
        self.blackboard.set_data('text', text)


class SentimentAnalyzer:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def analyze_sentiment(self):
        text = self.blackboard.get_data('text')
        if text:
            sentiment = self.perform_sentiment_analysis(text)
            self.blackboard.set_data('sentiment', sentiment)

    def perform_sentiment_analysis(self, text):
        # Perform sentiment analysis on the given text
        # Assume a fictional sentiment analyzer that assigns positive sentiment
        sentiment_score = 0.8  # Assume a sentiment score between 0 and 1
        return sentiment_score



class ResultViewer:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def display_result(self):
        text = self.blackboard.get_data('text')
        sentiment = self.blackboard.get_data('sentiment')
        if text and sentiment:
            print("Text:", text)
            print("Sentiment:", sentiment)

class Controller:
    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.knowledge_sources = []

    def add_knowledge_source(self, knowledge_source):
        self.knowledge_sources.append(knowledge_source)

    def process_social_media_data(self, social_media_data):
        for knowledge_source in self.knowledge_sources:
            if isinstance(knowledge_source, TextExtractor):
                knowledge_source.extract_text(social_media_data)
            elif isinstance(knowledge_source, SentimentAnalyzer):
                knowledge_source.analyze_sentiment()

        result_viewer = ResultViewer(self.blackboard)
        result_viewer.display_result()

if __name__ == "__main__":
    # Usage example
    blackboard = Blackboard()
    controller = Controller(blackboard)

    text_extractor = TextExtractor(blackboard)
    sentiment_analyzer = SentimentAnalyzer(blackboard)

    controller.add_knowledge_source(text_extractor)
    controller.add_knowledge_source(sentiment_analyzer)

    social_media_data = "I'm feeling great today! It's a beautiful sunny day."

    controller.process_social_media_data(social_media_data)
