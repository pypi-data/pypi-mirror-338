import torch.nn as nn

class ArchitectureAnalyzer:
    def __init__(self, model):
        self.model = model
    def count_parameters(self):
        total = sum(p.numel() for p in self.model.parameters())
        return total
    def count_layers(self):
        layers = [module for module in self.model.modules() if len(list(module.children())) == 0]
        return len(layers)
    def detect_layer_types(self):
        types = {}
        for name, module in self.model.named_modules():
            cls_name = module.__class__.__name__
            types[cls_name] = types.get(cls_name, 0) + 1
        return types
    def analyze(self):
        info = {}
        total = self.count_parameters()
        layers = self.count_layers()
        types = self.detect_layer_types()
        info["total_parameters"] = total
        info["layer_count"] = layers
        info["layer_types"] = types
        info["architecture_type"] = self.infer_architecture_type(types)
        info["recommendation"] = self.get_architecture_recommendation(total, layers, types)
        return info
    def infer_architecture_type(self, types):
        if types.get("LSTM", 0) > 0:
            return "LSTM"
        if types.get("GRU", 0) > 0:
            return "GRU"
        if types.get("RNN", 0) > 0:
            return "RNN"
        if types.get("Conv2d", 0) > 0 or types.get("Conv1d", 0) > 0:
            return "CNN"
        if types.get("Transformer", 0) > 0 or types.get("MultiheadAttention", 0) > 0:
            return "Transformer"
        if types.get("GPT2Model", 0) > 0 or types.get("GPT2LMHeadModel", 0) > 0:
            return "GPT"
        return "Inconnu"
    def get_architecture_recommendation(self, total_params, layer_count, types):
        if total_params < 1_000_000 and layer_count < 10:
            return "Modèle très simple et léger. Possibilité d'augmenter le batch size pour tirer parti du GPU."
        elif total_params < 50_000_000 and layer_count < 50:
            return "Modèle de complexité moyenne. Les hyperparamètres actuels semblent appropriés, mais un réglage fin peut être envisagé."
        elif total_params < 100_000_000 and layer_count < 100:
            return "Modèle avancé. Attention aux ressources, optimiser la gestion de la mémoire et ajuster les paramètres d'entraînement."
        else:
            return "Modèle très complexe. Nécessite un hardware performant et une optimisation hyperparamétrique poussée."