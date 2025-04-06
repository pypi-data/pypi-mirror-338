try:
    import GPUtil
except ImportError:
    GPUtil = None

class GPUMonitor:
    def __init__(self):
        if GPUtil is None:
            raise ImportError("GPUtil non installé, installez-le avec 'pip install GPUtil'")
    def get_gpu_status(self):
        gpus = GPUtil.getGPUs()
        status = []
        for gpu in gpus:
            status.append({
                "id": gpu.id,
                "name": gpu.name,
                "load": f"{gpu.load * 100:.1f}%",
                "memory_used": f"{gpu.memoryUsed} MB",
                "memory_total": f"{gpu.memoryTotal} MB",
                "temperature": f"{gpu.temperature} °C"
            })
        return status