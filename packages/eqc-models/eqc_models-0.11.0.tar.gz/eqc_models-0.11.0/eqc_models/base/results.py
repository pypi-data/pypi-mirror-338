import dataclasses
import warnings
import numpy as np

@dataclasses.dataclass
class SolutionResults:
    """
    The class is meant to provide a uniform interface to results, no matter
    the method of running the job.

    """

    solutions : np.ndarray
    energies : np.ndarray
    counts : np.array
    objectives : np.ndarray
    run_time : np.ndarray
    preprocessing_time : np.ndarray
    postprocessing_time : np.ndarray
    penalties : np.ndarray = None
    device : str = None
    time_units : str = "ns"

    @property
    def device_time(self):
        pre = self.preprocessing_time
        runtime = np.sum(self.run_time)
        post = np.sum(self.postprocessing_time)
        return pre + runtime + post

    @property
    def total_samples(self):
        return np.sum(self.counts)

    @property
    def best_energy(self):
        return np.min(self.energies)

    @classmethod
    def determine_device_type(cls, device_config):
        """ 
        Use the device config object from a cloud response
        to get the device info. It will have a device and job type
        identifiers in it.

        """
        devices = [k for k in device_config.keys()]
        # only one device type is supported at a time
        return devices[0]

    @classmethod
    def from_cloud_response(cls, model, response, solver):
        """ Fill in the details from the cloud """

        solutions = np.array(response["results"]["solutions"])
        energies = np.array(response["results"]["energies"])
        if hasattr(model, "evaluateObjective"):
            objectives = np.zeros((solutions.shape[0],), dtype=np.float32)
            for i in range(solutions.shape[0]):
                try:
                    objective = model.evaluateObjective(solutions[i])
                except NotImplementedError:
                    warnings.warn(f"Cannot set objective value in results for {model.__class__}")
                    objectives = None
                    break
                objectives[i] = objective
        else:
            objectives = None
        if hasattr(model, "evaluatePenalties"):
            penalties = np.zeros((solutions.shape[0],), dtype=np.float32)
            for i in range(solutions.shape[0]):
                penalties[i] = model.evaluatePenalty(solution[i]) + model.offset
        else:
            penalties = None
        counts = np.array(response["results"]["counts"])
# interrogate to determine the device type
        try:
            device_type = cls.determine_device_type(response["job_info"]["job_submission"]["device_config"])
        except KeyError:
            print(response.keys())
            raise
        job_id = response["job_info"]["job_id"]
        metrics = solver.client.get_job_metrics(job_id=job_id)
        metrics = metrics["job_metrics"]
        time_ns = metrics["time_ns"]
        device = time_ns["device"][device_type]
        runtime = device["samples"]["runtime"]
        post = device["samples"]["postprocessing_time"]
        pre = device["samples"]["preprocessing_time"]
        results = SolutionResults(solutions, energies, counts, objectives, 
                                  runtime, pre, post, penalties=penalties,
                                  device=device_type, time_units="ns")

        return results
