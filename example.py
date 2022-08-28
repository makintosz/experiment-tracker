import numpy as np

from experiment_tracker.tracker import ExperimentTracker


tracker = ExperimentTracker("Exemplary story name", "training_example")
tracker.add_parameter("learning_rate", 0.005)
tracker.add_parameter("network_model", "fully_connected")

tracker.add_result("rmse", 0.03423)
tracker.add_result("validation_results", np.zeros((12, 32)))
tracker.save()