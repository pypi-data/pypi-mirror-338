class DeepAnalyzer:
    def __init__(self, training_analyzer, arch_analyzer, model_profiler, system_diag):
        self.training_analyzer = training_analyzer
        self.arch_analyzer = arch_analyzer
        self.model_profiler = model_profiler
        self.system_diag = system_diag
    def comprehensive_report(self):
        report = {}
        report["hyperparameters"] = {"checks": self.training_analyzer.check_hyperparams(), "auto_adjust": self.training_analyzer.auto_adjust()}
        arch_info = self.arch_analyzer.analyze()
        report["architecture"] = arch_info
        profile = self.model_profiler.profile_model()
        report["profiling"] = profile
        sys_info = self.system_diag.diagnostics()
        report["system_diagnostics"] = sys_info
        report["overall_recommendation"] = self.aggregate_recommendations(report)
        return report
    def aggregate_recommendations(self, report):
        recs = []
        recs.extend(report["hyperparameters"]["checks"])
        recs.append(report["architecture"]["recommendation"])
        if report["profiling"]["memory_usage_mb"] > 2000:
            recs.append("Utilisation mémoire élevée détectée lors du profilage. Pensez à optimiser le modèle ou augmenter la VRAM.")
        if report["system_diagnostics"]["cpu_usage_percent"] > 80:
            recs.append("Utilisation CPU élevée. Vérifiez les processus concurrents ou optimisez le code.")
        recs.append(f"Temps moyen d'inférence: {report['profiling']['avg_inference_time']:.6f}s | Débit: {report['profiling']['throughput']:.2f} inf/s")
        return recs