from crawl4ai import WebCrawler
from crawl4ai.extraction_strategy import CosineStrategy, LLMExtractionStrategy
from crawl4ai.chunking_strategy import NlpSentenceChunking
import base64

## crawler init
def create_crawler():
    crawler = WebCrawler(verbose=True)
    crawler.warmup()
    return crawler

## main func
crawler = create_crawler()

## llm extraction strategy
llm_extraction_strategy=LLMExtractionStrategy(
        provider="huggingface/WizardLM/WizardCoder-Python-34B-V1.0",
        api_token="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",
        instruction="Summarise this data into human readable format"
    )

## cosine extraction strategy
cosine_extraction_strategy=CosineStrategy(
        max_dist=0.2,
        top_k=3
    )

## run crawler
result = crawler.run(
    url="https://www.nbcnews.com/business",
    css_selector="h2"
)

# screenshot
# with open("screenshot.png", "wb") as f:
#     f.write(base64.b64decode(result.screenshot))
#     print("Screenshot saved to 'screenshot.png'!")

## output
output_file = 'results.txt'
with open(output_file, 'w') as f:
    f.write(f"Basic crawl result: {result}")