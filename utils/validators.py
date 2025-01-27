class Validators:
    @staticmethod
    def validate_text(text):
        if not isinstance(text, str) or len(text) == 0:
            raise ValueError("Text must be a non-empty string.")
        
        if len(text) > 1000:  # Пример ограничения на длину текста
            raise ValueError("Text is too long.")

    @staticmethod
    def validate_vector(vector, dimension):
        if not isinstance(vector, (list, np.ndarray)):
            raise ValueError("Vector must be a list or numpy array.")
        
        if len(vector) != dimension:
            raise ValueError(f"Vector must have dimension {dimension}.")