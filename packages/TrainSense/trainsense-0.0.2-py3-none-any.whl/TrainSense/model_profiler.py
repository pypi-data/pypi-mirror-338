import torch
import time
import torch.nn as nn

class ModelProfiler:
    def __init__(self, model, device="cpu"):
        self.model = model.to(device)
        self.device = device
    def profile_model(self, input_shape=None, iterations=50):
        if input_shape is None:
            input_shape = self._infer_input_shape()
        self.model.eval()
        dummy_input = torch.randn(*input_shape).to(self.device)
        with torch.no_grad():
            for _ in range(10):
                _ = self.model(dummy_input)
            start = time.time()
            for _ in range(iterations):
                _ = self.model(dummy_input)
            end = time.time()
        avg_time = (end - start) / iterations
        throughput = 1 / avg_time if avg_time > 0 else 0
        mem = 0
        if self.device.startswith("cuda"):
            mem = torch.cuda.max_memory_allocated(self.device) / (1024 ** 2)
        return {"avg_inference_time": avg_time, "throughput": throughput, "memory_usage_mb": mem}
    def _infer_input_shape(self):
        for layer in self.model.modules():
            if isinstance(layer, nn.Conv2d):
                return (1, 3, 32, 32)
        return (1, 10)