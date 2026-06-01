import pipeline
import logging

if __name__=="__main__":
    logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    pipeline.run_pipeline()
