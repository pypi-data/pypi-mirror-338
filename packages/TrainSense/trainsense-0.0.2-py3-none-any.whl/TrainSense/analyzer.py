class TrainingAnalyzer:
    def __init__(self, batch_size: int, learning_rate: float, epochs: int, system_config=None, arch_info=None):
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.system_config = system_config
        self.arch_info = arch_info
    def check_hyperparams(self):
        rec = []
        if self.system_config and self.system_config.gpu_info:
            for gpu in self.system_config.gpu_info:
                if gpu["memory_total"] < 6000:
                    if self.batch_size > 16:
                        rec.append("GPU à mémoire limitée détecté. Batch size recommandé ≤ 16.")
                    else:
                        rec.append("Batch size compatible avec GPU à mémoire limitée.")
                else:
                    if self.batch_size > 128:
                        rec.append("Batch size excessif pour GPU performant. Recommandation ≤ 128.")
                    else:
                        rec.append("Batch size bien optimisé pour votre GPU.")
        else:
            rec.append("Aucune info GPU détectée. Vérifiez votre configuration CPU.")
        if self.learning_rate > 0.1:
            rec.append("Learning rate trop élevé, risque de divergence.")
        elif self.learning_rate < 0.0001:
            rec.append("Learning rate trop bas, convergence très lente.")
        else:
            rec.append("Learning rate dans une plage standard. Ajustez pour améliorer la convergence.")
        if self.epochs < 10:
            rec.append("Nombre d'epochs insuffisant pour un apprentissage complet.")
        elif self.epochs > 300:
            rec.append("Nombre d'epochs trop élevé, risque de surapprentissage.")
        else:
            rec.append("Nombre d'epochs bien équilibré pour la plupart des entraînements.")
        if self.arch_info:
            if self.arch_info.get("total_parameters", 0) > 100_000_000:
                rec.append("Modèle volumineux détecté. Pensez à réduire le batch size ou optimiser le modèle.")
            elif self.arch_info.get("total_parameters", 0) < 100_000:
                rec.append("Modèle léger détecté. Possibilité d'augmenter le batch size pour exploiter pleinement le GPU.")
            else:
                rec.append("Taille du modèle modérée. Hyperparamètres semblent adéquats, mais vérifiez la complexité des couches.")
        else:
            rec.append("Informations d'architecture manquantes pour affiner les recommandations.")
        return rec
    def auto_adjust(self):
        adj = {}
        if self.system_config and self.system_config.gpu_info:
            avg_mem = sum(gpu["memory_total"] for gpu in self.system_config.gpu_info) / len(self.system_config.gpu_info)
            if avg_mem < 6000 and self.batch_size > 16:
                adj["batch_size"] = 16
            elif avg_mem >= 6000 and self.batch_size > 128:
                adj["batch_size"] = 128
            else:
                adj["batch_size"] = self.batch_size
        else:
            adj["batch_size"] = self.batch_size
        if self.learning_rate > 0.1:
            adj["learning_rate"] = 0.05
        elif self.learning_rate < 0.0001:
            adj["learning_rate"] = 0.001
        else:
            adj["learning_rate"] = self.learning_rate
        if self.epochs < 10:
            adj["epochs"] = 50
        elif self.epochs > 300:
            adj["epochs"] = 150
        else:
            adj["epochs"] = self.epochs
        return adj
    def summary(self):
        s = {"batch_size": self.batch_size, "learning_rate": self.learning_rate, "epochs": self.epochs}
        if self.system_config:
            s["system"] = {"cpu_count": self.system_config.cpu_count, "total_memory_gb": self.system_config.total_memory, "gpu_info": self.system_config.gpu_info, "cuda_version": self.system_config.cuda_version, "cudnn_version": self.system_config.cudnn_version}
        if self.arch_info:
            s["architecture"] = self.arch_info
        return s