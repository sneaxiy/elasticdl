"""Callback for unittests."""
from abc import ABC, abstractmethod

ON_REPORT_GRADIENT_BEGIN = "on_report_gradient_begin"
ON_REPORT_EVALUATION_METRICS_BEGIN = "on_report_evaluation_metrics_begin"


class BaseCallback(ABC):
    """Base class of callbacks used for testing."""

    def __init__(self, master, worker, call_times):
        self._master = master
        self._worker = worker
        self.call_times = call_times

    @abstractmethod
    def __call__(self):
        pass
