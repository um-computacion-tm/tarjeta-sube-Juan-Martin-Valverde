class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"
PRECIO_TICKET = 70
DESACTIVADO = "desactivado"
ACTIVADO = "activado"

DESCUENTOS = {
    PRIMARIO: 50,       
    SECUNDARIO: 60,     
    UNIVERSITARIO: 70,  
    JUBILADO: 75,       
}

class Sube:
    def __init__(self):
        self.saldo = 1000
        self.grupo_beneficiario = None
        self.estado = ACTIVADO

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario in DESCUENTOS:
            descuento_porcentaje = DESCUENTOS[self.grupo_beneficiario]
            descuento_decimal = descuento_porcentaje / 100
            precio_con_descuento = PRECIO_TICKET * (1 - descuento_decimal)
            return precio_con_descuento
        return PRECIO_TICKET

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("El usuario está desactivado.")
        precio_ticket = self.obtener_precio_ticket()
        if self.saldo < precio_ticket:
            raise NoHaySaldoException("No hay saldo suficiente.")
        self.saldo -= precio_ticket

    def cambiar_estado(self, estado):
        if estado not in (ACTIVADO, DESACTIVADO):
            raise EstadoNoExistenteException("El estado no existe.")
        self.estado = estado