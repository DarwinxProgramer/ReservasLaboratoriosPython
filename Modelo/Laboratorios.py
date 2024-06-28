import pickle


class ModeloLaboratorio:
    def __init__(self, archivo_laboratorios='laboratorios.dat'):
        self.laboratorios = {}
        self.archivo_laboratorios = archivo_laboratorios
        self.cargar_laboratorios()

    def crear_laboratorio(self, codigo, nombre, capacidad, softwares):
        nuevo_laboratorio = {
            "codigo": codigo,
            "nombre": nombre,
            "capacidad": capacidad,
            "softwares": softwares
        }
        self.laboratorios[codigo] = nuevo_laboratorio
        self.guardar_laboratorios()

    def guardar_laboratorios(self):
        data = {'laboratorios': self.laboratorios}
        with open(self.archivo_laboratorios, 'wb') as file:
            pickle.dump(data, file)

    def cargar_laboratorios(self):
        try:
            with open(self.archivo_laboratorios, 'rb') as file:
                data = pickle.load(file)
                if 'laboratorios' in data and isinstance(data['laboratorios'], dict):
                    self.laboratorios = data['laboratorios']
        except FileNotFoundError:
            self.guardar_laboratorios()
        except (pickle.UnpicklingError, MemoryError) as e:
            print(f"Error al cargar laboratorios: {e}")

    def obtener_todos_los_laboratorios(self):
        return self.laboratorios.values()

    def buscar_laboratorio_por_codigo(self, codigo):
        try:
            with open(self.archivo_laboratorios, 'rb') as file:
                data = pickle.load(file)
                laboratorios = data.get('laboratorios', {})
        except FileNotFoundError:
            laboratorios = {}

        for id, laboratorio in laboratorios.items():
            if laboratorio.get("codigo") == codigo:
                return laboratorio

        return None

    def modificar_laboratorio(self, codigo, nuevos_datos):
        if codigo in self.laboratorios:
            self.laboratorios[codigo].update(nuevos_datos)
            self.guardar_laboratorios()
            return True
        return False

    def eliminar_laboratorio_por_codigo(self, codigo):
        for id, laboratorio in list(self.laboratorios.items()):
            if laboratorio.get("codigo") == codigo:
                del self.laboratorios[id]
                self.guardar_laboratorios()
                return True

        return False
