import psutil
import platform
import socket

class SystemDiagnostics:
    def diagnostics(self):
        diag = {}
        diag["cpu_usage_percent"] = psutil.cpu_percent(interval=1)
        diag["memory_usage_percent"] = psutil.virtual_memory().percent
        diag["disk_usage_percent"] = psutil.disk_usage('/').percent
        diag["os"] = platform.system() + " " + platform.release()
        diag["hostname"] = socket.gethostname()
        diag["uptime_seconds"] = psutil.boot_time()
        return diag