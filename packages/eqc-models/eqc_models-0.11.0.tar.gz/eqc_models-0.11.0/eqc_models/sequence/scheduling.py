import numpy as np
from eqc_models.base.quadratic import ConstrainedQuadraticModel
from eqc_models.base.constraints import InequalitiesMixin

class CrewSchedulingModel(ConstrainedQuadraticModel):
    """
    Crew scheduling model

    Parameters
    ------------

    crews : List
    tasks : List

    >>> crews = [{"name": "Maintenance Crew 1", "skills": ["A", "F"]}, 
    ...          {"name": "Baggage Crew 1", "skills": ["B"]},
    ...          {"name": "Maintenance Crew 2", "skills": ["A", "F"]}]
    >>> tasks = [{"name": "Refuel", "skill_need": "F"},
    ...          {"name": "Baggage", "skill_need": "B"}]

    """

    def __init__(self, crews, tasks):
        self.crews = crews
        self.tasks = tasks

    def decode(self, solution) -> np.ndarray:
        """ Translate the solution into a list of tasks for each crew """

