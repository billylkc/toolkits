import yake
from protos import text_pb2
from protos import text_pb2_grpc
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class Text(text_pb2_grpc.TextServicer):
    def ExtractKeywords(self, request, context):
        text = request.text
        language = "en"
        max_ngram_size = 2
        deduplication_thresold = 0.6
        deduplication_algo = "seqm"
        windowSize = 1
        numOfKeywords = 20

        custom_kw_extractor = yake.KeywordExtractor(
            lan=language,
            n=max_ngram_size,
            dedupLim=deduplication_thresold,
            dedupFunc=deduplication_algo,
            windowsSize=windowSize,
            top=numOfKeywords,
            features=None,
        )
        kws = custom_kw_extractor.extract_keywords(text)
        keywords = [x[0] for x in kws]
        resp = text_pb2.KeywordResponse(text=keywords)

        return resp

    def ExtractSummary(self, request, context):
        text = request.text
        count = request.count  # sentence count
        stemmer = Stemmer("english")
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words("english")

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        ss = summarizer(parser.document, count)
        result = []
        for s in ss:
            result.append(str(s))
        resp = text_pb2.SummaryResponse(text="\n\n".join(result))
        return resp

    def ExtractTfIdf(self, request, context):
        docs = request.text
        tfIdfVectorizer = TfidfVectorizer(use_idf=True)
        tfIdf = tfIdfVectorizer.fit_transform(docs)

        df = pd.DataFrame(
            tfIdf[0].T.todense(),
            index=tfIdfVectorizer.get_feature_names(),
            columns=["score"],
        )
        df = df.sort_values("score", ascending=False)
        df.reset_index(drop=False, inplace=True)  # keywords

        resp = text_pb2.TFResponse()
        for _, row in df.iterrows():
            rec = text_pb2.TFRecord(text=row["index"], score=row["score"])
            resp.records.append(rec)

        return resp
