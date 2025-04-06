import psutil
import torch
import platform
try:
    import GPUtil
except ImportError:
    GPUtil = None

class SystemConfig:
    def __init__(self):
        self.cpu_count = psutil.cpu_count(logical=False)
        self.total_memory = psutil.virtual_memory().total / (1024 ** 3)
        self.cpu_freq = psutil.cpu_freq().max if psutil.cpu_freq() else None
        self.gpu_info = self._get_gpu_info() if GPUtil else []
        self.cuda_version = self._get_cuda_version()
        self.cudnn_version = self._get_cudnn_version()
        self.os_info = platform.platform()
    def _get_gpu_info(self):
        gpus = GPUtil.getGPUs()
        info = []
        for gpu in gpus:
            info.append({
                "id": gpu.id,
                "name": gpu.name,
                "memory_total": gpu.memoryTotal,
                "memory_used": gpu.memoryUsed,
                "load": gpu.load
            })
        return info
    def _get_cuda_version(self):
        try:
            return torch.version.cuda
        except Exception:
            return "Non disponible"
    def _get_cudnn_version(self):
        try:
            return torch.backends.cudnn.version()
        except Exception:
            return "Non disponible"