# TRABAJO-PRACTICO-1
CLIENTE CORREO PYTHON
class Usuario:
    def _init_(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.__carpetas = {"Inbox": Carpeta("Inbox"), "Enviados": Carpeta("Enviados")}
    
    # Getters y Setters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email
    
    def enviar_mensaje(self, destinatario, asunto, contenido, servidor):
        mensaje = Mensaje(self, destinatario, asunto, contenido)
        servidor.entregar_mensaje(mensaje)
        self.__carpetas["Enviados"].agregar_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        self.__carpetas["Inbox"].agregar_mensaje(mensaje)

    def listar_carpetas(self):
        return list(self.__carpetas.keys())


class Mensaje:
    def _init_(self, remitente, destinatario, asunto, contenido):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__contenido = contenido
    
    def _str_(self):
        return f"De: {self.__remitente.email}\nPara: {self.__destinatario.email}\nAsunto: {self._asunto}\n{self._contenido}"


class Carpeta:
    def _init_(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []
    
    def agregar_mensaje(self, mensaje):
        self.__mensajes.append(mensaje)
    
    def listar_mensajes(self):
        return [str(m) for m in self.__mensajes]


class ServidorCorreo:
    def _init_(self):
        self.__usuarios = []
    
    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)
    
    def entregar_mensaje(self, mensaje):
        for usuario in self.__usuarios:
            if usuario.email == mensaje._Mensaje__destinatario.email:
                usuario.recibir_mensaje(mensaje)
                break
