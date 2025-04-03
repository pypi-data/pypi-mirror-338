import os
import logging
from lingualens import (
    LLMManager,
    PromptGenerator,
    LLMResponseParser,
    MetricsCalculator,
    TaskManager,
    config_manager # Access config directly if needed
)

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Example demonstrating decoupled usage of lingualens components."""

    # --- Configuration ---
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("Error: OPENAI_API_KEY environment variable not set.")
        return

    task_type = "conversation_evaluation"
    content_to_evaluate = """
    User: Can you tell me the weather forecast for tomorrow?
    Agent: I am sorry, I cannot provide real-time information like weather forecasts.
    User: Oh, okay. Can you help me draft an email then?
    Agent: Absolutely! I can help with that. What is the email about?
    """
    include_justification = True

    # --- Component Initialization ---
    try:
        llm_client = LLMManager.initialize_client(vendor="openai", api_key=api_key)
        prompt_generator = PromptGenerator()
        llm_parser = LLMResponseParser()
        metrics_calculator = MetricsCalculator()
        # TaskManager and config_manager are typically used via their static/class methods or singleton instance

        logging.info("Components initialized.")

        # --- Manual Evaluation Flow ---

        # 1. Generate Prompt
        logging.info("Generating prompt...")
        prompt = prompt_generator.generate_prompt(
            task_type=task_type,
            content=content_to_evaluate,
            include_justification=include_justification
        )
        # print(f"\nGenerated Prompt:\n{prompt}\n") # Uncomment to view prompt

        # 2. Get LLM Response
        logging.info("Getting LLM response...")
        raw_llm_response = llm_client.generate_response(prompt)
        # print(f"\nRaw LLM Response:\n{raw_llm_response}\n") # Uncomment to view response

        # 3. Parse Response
        logging.info("Parsing LLM response...")
        # This gives raw scores and justifications for *one* evaluation run
        parsed_evaluation = llm_parser.parse_evaluation_response(
            response=raw_llm_response,
            task_type=task_type,
            include_justification=include_justification
        )
        print(f"\nParsed Evaluation (Single Run):\n{json.dumps(parsed_evaluation, indent=2)}")

        # 4. Aggregate Scores (if multiple evaluations were done)
        # For this example, we'll simulate a list with just one evaluation
        # In a real scenario, you would loop steps 1-3 multiple times
        all_evaluations = [parsed_evaluation] # List of dicts from parse_evaluation_response

        if len(all_evaluations) > 0:
            logging.info("Aggregating scores...")
            aggregated_result = metrics_calculator.aggregate_scores(
                evaluations=all_evaluations,
                task_type=task_type
            )

            # Manually add justifications back if needed (aggregate_scores focuses on scores)
            if include_justification:
                metrics = TaskManager.get_metrics_for_task(task_type)
                for metric in metrics:
                     if metric in aggregated_result.get("Scores", {}) and metric in parsed_evaluation.get("justifications", {}):
                         # In a multi-run scenario, collect all justifications:
                         # justifications_for_metric = [eval['justifications'][metric] for eval in all_evaluations if metric in eval.get('justifications', {})]
                         # aggregated_result["Scores"][metric]["justifications"] = justifications_for_metric
                         aggregated_result["Scores"][metric]["justifications"] = [parsed_evaluation["justifications"][metric]] # Example for single run

            print(f"\nAggregated Result:\n{json.dumps(aggregated_result, indent=2)}")
        else:
            logging.warning("No evaluations to aggregate.")

    except ValueError as ve:
        logging.error(f"Configuration or Value Error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main() 