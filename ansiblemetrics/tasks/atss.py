import yaml
from io import StringIO

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.general.loc import LOC

class ATSS(AnsibleMetric):

    def count(self, relative=False):
        return 0