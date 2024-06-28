import pickle


class ModeloUsuario:
    def __init__(self, archivo_usuarios='usuarios.dat'):
        self.usuarios = {
            "admin": {"id": "admin", "nombre": "admin", "apellido": "admin", "rol": "admin", "email": "admin", "contrasena": "admin"}
        }
        self.archivo_usuarios = archivo_usuarios
        self.cargar_usuarios()

    def crear_usuario(self, id, nombre, apellido, rol, email, contrasena):
        nuevo_usuario = {
            "id": id,
            "nombre": nombre,
            "apellido": apellido,
            "rol": rol,
            "email": email,
            "contrasena": contrasena
        }
        self.usuarios[id] = nuevo_usuario
        # Guardar usuarios en el archivo después de crear uno nuevo
        self.guardar_usuarios()

    def cargar_usuarios(self):
        try:
            with open(self.archivo_usuarios, 'rb') as file:
                data = pickle.load(file)
                if 'usuarios' in data and isinstance(data['usuarios'], dict):
                    self.usuarios = data['usuarios']
        except FileNotFoundError:
            pass
        except (pickle.UnpicklingError, MemoryError) as e:
            print(f"Error al cargar usuarios: {e}")

    def guardar_usuarios(self):
        data = {'usuarios': self.usuarios}
        with open(self.archivo_usuarios, 'wb') as file:
            pickle.dump(data, file)

    def obtener_usuario_por_credenciales(self, email, contrasena):
        for usuario in self.usuarios.values():
            if usuario.get("email") == email and usuario.get("contrasena") == contrasena:
                return usuario
        return None

    def obtener_todos_los_usuarios(self):
        return self.usuarios.values()

    def modificar_usuario(self, id, nuevos_datos):
        if id in self.usuarios:
            self.usuarios[id].update(nuevos_datos)
            self.guardar_usuarios()
            return True
        return False

    def buscar_usuario_por_id(self, id):
        try:
            with open(self.archivo_usuarios, 'rb') as file:
                data = pickle.load(file)
                usuarios = data.get('usuarios', {})
        except FileNotFoundError:
            usuarios = {}
        return usuarios.get(id, None)

    def eliminar_usuario_por_credenciales(self, email, contrasena):
        for id, usuario in list(self.usuarios.items()):
            if usuario.get("email") == email and usuario.get("contrasena") == contrasena:
                del self.usuarios[id]
                self.guardar_usuarios()
                return True
        return False

    def eliminar_usuario_por_id(self, id):
        usuario = self.buscar_usuario_por_id(id)
        if usuario:
            return self.eliminar_usuario_por_credenciales(usuario["email"], usuario["contrasena"])
        return False
