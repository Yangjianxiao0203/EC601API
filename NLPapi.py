from google.cloud import language
import os
path="/Users/jianxiaoyang/Downloads/jianxiao602nlp-d001e4497302.json"
path2="/Users/jianxiaoyang/Documents/EC601 software/google nlp api/jianxiao602nlp-d001e4497302.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path2

def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}") #空10格后输入：

def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")

def analyze_text_syntax(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_syntax(document=document)

    fmts = "{:10}: {}"
    print(fmts.format("sentences", len(response.sentences)))
    print(fmts.format("tokens", len(response.tokens)))
    for token in response.tokens:
        print(fmts.format(token.part_of_speech.tag.name, token.text.content))
        
def classify_text(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)

    for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")

texts = ["I won't be back today","l will be home"]
for text in texts:
    analyze_text_sentiment(text)
# classify_text(text)
# analyze_text_entities(text)