class Configuracion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuracion, cls).__new__(cls)
            cls._instance.usuario_actual = None
        return cls._instance
