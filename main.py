import pipeline
import logging
import traceback

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
if __name__ == "__main__":
    print("ENTERING MAIN BLOCK")
    try:
        pipeline.run_pipeline()
        print("PIPELINE COMPLETED")
    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()