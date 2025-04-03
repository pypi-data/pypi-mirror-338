import os
import logging
from lingualens import Evaluator, LLMManager, TaskManager

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Example demonstrating automatic task identification."""

    # --- Configuration ---
    # API key is needed for both task identification and evaluation
    api_key = os.getenv("OPENAI_API_KEY") # Or CLOUDVERSE_API_KEY if using cloudverse for identification
    if not api_key:
        logging.error("Error: API key environment variable not set (e.g., OPENAI_API_KEY).")
        return

    # Content to evaluate - the system will try to infer the task from this
    content_to_evaluate = """
    Subject: Problem with recent order #12345

    Hi Support Team,

    I received my order #12345 today, but the main item is damaged.
    The box was intact, but the product inside has a large crack.
    Could you please arrange for a replacement or refund?

    Thanks,
    A. Customer
    """

    # --- Initialization ---
    try:
        # 1. Initialize an LLM Client (needed for task identification)
        # Using OpenAI here, but could be Cloudverse depending on TaskManager setup
        # Note: The LLM used for identification can be different from the one used for evaluation
        identification_client = LLMManager.initialize_client(
            vendor="openai", # TaskManager might default differently, explicitly use openai here
            api_key=api_key,
            model_name="gpt-3.5-turbo"
        )

        # --- Task Identification (Manual Step Shown for Clarity) ---
        # Although Evaluator can do this implicitly if task_type=None,
        # we show the step explicitly here.
        # This requires the content and an LLM client.
        identified_task = TaskManager.identify_task_type(content_to_evaluate, identification_client)
        logging.info(f"Automatically identified task type: {identified_task}")

        # 2. Initialize the LLM Client for Evaluation (can be the same or different)
        evaluation_client = LLMManager.initialize_client(
            vendor="openai",
            api_key=api_key,
            model_name="gpt-3.5-turbo"
        )

        # 3. Initialize the Evaluator WITHOUT specifying task_type
        # It will use the TaskManager internally to identify the task if not provided.
        # Providing the identified_task here just confirms the previous step.
        evaluator = Evaluator(
            task_type=identified_task, # Or pass task_type=None to let Evaluator call identify_task_type
            num_evaluations=1,
            include_justification=True
        )
        logging.info(f"Evaluator initialized for task: {evaluator.task_type}")

        # --- Evaluation ---
        logging.info(f"Starting evaluation...")
        result = evaluator.evaluate(
            content=content_to_evaluate,
            llm_client=evaluation_client # Pass the client to be used for evaluation
        )

        # --- Results ---
        logging.info("Evaluation Complete.")
        print("\n----- Evaluation Results -----")
        metadata = result.get("metadata", {})
        print(f"Task Type Used: {metadata.get('task_type', 'N/A')}")
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