import os
import logging
from lingualens import Evaluator, LLMManager

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Example demonstrating multiple evaluations for score aggregation."""

    # --- Configuration ---
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("Error: OPENAI_API_KEY environment variable not set.")
        return

    task_type = "writing_quality" # Use a different task type for variety
    num_evals = 3 # Set the number of evaluations

    content_to_evaluate = """
    The article discusses the effects of climate change on polar bears.
    It presents data showing declining sea ice and correlates it with reduced hunting success.
    The author argues for stronger international climate agreements.
    However, the structure is a bit disorganized, and some paragraphs lack clear topic sentences.
    The conclusion could be stronger by summarizing the key findings more directly.
    """

    # --- Initialization ---
    try:
        # 1. Initialize LLM Client
        llm_client = LLMManager.initialize_client(
            vendor="openai",
            api_key=api_key,
            model_name="gpt-3.5-turbo"
        )

        # 2. Initialize Evaluator with num_evaluations > 1
        evaluator = Evaluator(
            task_type=task_type,
            num_evaluations=num_evals,
            include_justification=True # Justifications from all runs will be collected
        )

        # --- Evaluation ---
        logging.info(f"Starting {num_evals} evaluations for task: {evaluator.task_type}...")
        result = evaluator.evaluate(
            content=content_to_evaluate,
            llm_client=llm_client
        )

        # --- Results ---
        logging.info("Evaluation Complete.")
        print("\n----- Evaluation Results -----")
        metadata = result.get("metadata", {})
        print(f"Task Type: {metadata.get('task_type', 'N/A')}")
        print(f"Evaluations Requested: {metadata.get('num_evaluations', 'N/A')}")
        print(f"Timestamp: {metadata.get('timestamp', 'N/A')}")

        print(f"\nTotal Weighted Score (Aggregated): {result.get('total_weighted_score', 'N/A')}")

        print("\nAggregated Scores (Median after outlier removal):")
        scores_data = result.get("Scores", {})
        for metric, data in scores_data.items():
            print(f"  Metric: {metric.upper()}")
            print(f"    Median Score: {data.get('score', 'N/A'):.2f}")
            print(f"    Raw Scores (All Runs): {data.get('raw_scores', [])}")
            print(f"    Filtered Scores (Used for Median): {data.get('filtered_scores', [])}")
            print(f"    Variance (Filtered): {data.get('variance', 'N/A'):.2f}")
            print(f"    Normalized Score (Median): {data.get('normalized_score', 'N/A'):.2f}")
            print(f"    Weighted Score Contrib.: {data.get('weighted_score', 'N/A'):.2f}")
            if "justifications" in data and data["justifications"]:
                 print(f"    Justification(s):")
                 # Justifications list corresponds to the raw_scores list order
                 for i, just in enumerate(data.get('justifications', [])):
                    print(f"      Eval {i+1}: {just}")
            print("-" * 20)

    except ValueError as ve:
        logging.error(f"Configuration or Value Error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main() 