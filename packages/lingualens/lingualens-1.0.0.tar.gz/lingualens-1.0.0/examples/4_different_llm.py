import os
import logging
from lingualens import Evaluator, LLMManager

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Example demonstrating using a different LLM vendor (Cloudverse)."""

    # --- Configuration ---
    # Ensure your Cloudverse API key is set as an environment variable
    # NOTE: Replace CLOUDVERSE_API_KEY with the actual env var name if different
    api_key = os.getenv("CLOUDVERSE_API_KEY")
    if not api_key:
        logging.error("Error: CLOUDVERSE_API_KEY environment variable not set.")
        return

    task_type = "sentiment_analysis" # Yet another task type

    content_to_evaluate = """
    The user experience on this new platform is incredibly frustrating.
    Navigation is confusing, and simple tasks take far too long.
    I appreciate the new features, but the core usability needs significant improvement.
    """

    # --- Initialization ---
    try:
        # 1. Initialize the LLM Client for Cloudverse
        llm_client = LLMManager.initialize_client(
            vendor="cloudverse",
            api_key=api_key,
            # Cloudverse client might have specific optional args, check its implementation
            # e.g., model_name="cloudverse-model-xyz" # Example if needed
        )
        logging.info(f"Initialized Cloudverse LLM client.")

        # 2. Initialize the Evaluator
        evaluator = Evaluator(
            task_type=task_type,
            num_evaluations=1,
            include_justification=True
        )

        # --- Evaluation ---
        logging.info(f"Starting evaluation with Cloudverse for task: {evaluator.task_type}...")
        result = evaluator.evaluate(
            content=content_to_evaluate,
            llm_client=llm_client # Pass the Cloudverse client
        )

        # --- Results ---
        logging.info("Evaluation Complete.")
        print("\n----- Evaluation Results (Cloudverse) -----")
        metadata = result.get("metadata", {})
        print(f"Task Type: {metadata.get('task_type', 'N/A')}")
        print(f"Total Weighted Score: {result.get('total_weighted_score', 'N/A')}")
        scores_data = result.get("Scores", {})
        for metric, data in scores_data.items():
            print(f"  Metric: {metric.upper()}")
            print(f"    Score: {data.get('score', 'N/A'):.2f}")
            if "justifications" in data and data["justifications"]:
                 print(f"    Justification(s):")
                 for i, just in enumerate(data.get('justifications', [])):
                    print(f"      Eval {i+1}: {just}")
            print("-" * 20)

    except ValueError as ve:
        logging.error(f"Configuration or Value Error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main() 