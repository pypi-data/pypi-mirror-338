import logging
import json
from lingualens import TaskManager, config_manager

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Example demonstrating how to list supported tasks and metrics."""

    try:
        # --- List Supported Tasks ---
        print("\n----- Supported Task Types -----")
        supported_tasks = TaskManager.get_supported_tasks_with_descriptions()
        if not supported_tasks:
            print("No task types found in configuration.")
        else:
            for task_type, description in supported_tasks.items():
                print(f"Task Type: {task_type}")
                print(f"  Description: {description}")
                # Get metrics and weights for this task
                try:
                    metrics = TaskManager.get_metrics_for_task(task_type)
                    weights = TaskManager.get_weightages_for_task(task_type)
                    print("  Metrics & Weights:")
                    for metric in metrics:
                        print(f"    - {metric}: {weights.get(metric, 'N/A'):.2f}")
                except ValueError as e:
                    print(f"  Error getting details for task {task_type}: {e}")
                print("-" * 20)

        # --- List All Metrics Details from ConfigManager ---
        # Note: ConfigManager is a singleton instance, accessed directly.
        print("\n----- All Defined Metrics (from metrics_pool.json) -----")
        all_metrics = config_manager.metrics_pool
        if not all_metrics:
            print("No metrics found in metrics_pool configuration.")
        else:
            for metric_name, metric_config in all_metrics.items():
                print(f"Metric: {metric_name}")
                print(f"  Description: {metric_config.get('description', 'N/A')}")
                if 'scoring_criteria' in metric_config:
                    print("  Scoring Criteria:")
                    for score, criteria in metric_config['scoring_criteria'].items():
                        print(f"    {score}: {criteria}")
                print("-" * 20)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main() 