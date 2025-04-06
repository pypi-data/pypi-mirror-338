class OptimizerHelper:
    @staticmethod
    def suggest_optimizer(model_size: int, architecture_complexity=0):
        if model_size < 10_000_000:
            return "SGD ou Adam"
        elif model_size < 50_000_000:
            if architecture_complexity < 50:
                return "Adam"
            else:
                return "AdamW"
        else:
            return "AdamW avec réglages avancés et scheduler"
    @staticmethod
    def adjust_learning_rate(current_lr: float, performance_metric: float):
        if performance_metric > 1.0:
            new_lr = current_lr * 0.7
            return new_lr, "Réduction significative du learning rate en raison d'un débit faible"
        elif performance_metric < 0.1:
            new_lr = current_lr * 1.2
            return new_lr, "Augmentation du learning rate pour accélérer l'entraînement"
        else:
            return current_lr, "Learning rate optimal"