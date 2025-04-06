class UltraOptimizer:
    def __init__(self, training_data_stats, model_arch_stats, system_stats):
        self.training_data_stats = training_data_stats
        self.model_arch_stats = model_arch_stats
        self.system_stats = system_stats
    def compute_optimal_hyperparams(self):
        params = {}
        if self.system_stats["total_memory_gb"] < 8:
            params["batch_size"] = 16
        elif self.system_stats["total_memory_gb"] < 16:
            params["batch_size"] = 32
        else:
            params["batch_size"] = 64
        if self.model_arch_stats["total_parameters"] > 50_000_000:
            params["learning_rate"] = 0.001
        else:
            params["learning_rate"] = 0.01
        if self.training_data_stats["data_size"] > 1_000_000:
            params["epochs"] = 100
        else:
            params["epochs"] = 50
        params["optimizer"] = "AdamW" if self.model_arch_stats["total_parameters"] > 50_000_000 else "Adam"
        return params