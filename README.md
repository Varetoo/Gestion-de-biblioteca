Objetivos del Proyecto:

Gestión de Libros y Usuarios:
Implementar una estructura que permita gestionar libros y usuarios en un sistema de biblioteca. Los usuarios deben poder realizar acciones como solicitar libros y devolverlos.

Control de Disponibilidad:
Los libros deben tener un estado que indique si están disponibles o prestados. Al realizar un préstamo, el libro debe marcarse como prestado y, al ser devuelto, debe cambiar su estado a disponible.

Diferentes Tipos de Usuarios:
Crear un tipo especial de usuario con beneficios adicionales. Un "UsuarioPremium" podrá solicitar más préstamos que un usuario estándar, reflejando una mayor capacidad de acceso a los recursos.

Seguridad en los Datos:
Los datos sensibles, como el nombre del usuario y el título del libro, deben estar protegidos y no ser accesibles directamente desde fuera de la clase correspondiente.

Métodos para Operaciones Específicas:
Los usuarios podrán solicitar un libro y devolverlo.
Los libros podrán ser marcados como prestados o disponibles mediante métodos específicos.

Consistencia en las Acciones:
Tanto los usuarios estándar como los premium deben poder solicitar libros, pero de formas ligeramente diferentes.
Un usuario premium tendrá mayor flexibilidad al solicitar varios préstamos simultáneos.