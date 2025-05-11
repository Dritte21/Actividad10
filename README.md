# Sistema de Citas Médicas con Patrones de Diseño

Este proyecto es una aplicación sencilla de consola que permite gestionar citas médicas usando tres patrones de diseño: **Factory Method**, **Decorator** y **Observer**.

## 🎯 Objetivo

Demostrar el uso de patrones de diseño en un caso de uso realista (agendamiento de citas) de forma clara y funcional.

## 🧱 Patrones Usados

- **Creacional (Factory Method):** se encarga de crear instancias de citas médicas.
- **Estructural (Decorator):** agrega funcionalidad adicional (recordatorios SMS) sin modificar la clase original.
- **Comportamiento (Observer):** permite notificar a varios usuarios al mismo tiempo cuando una cita es confirmada.

## 🖥️ Cómo ejecutar el programa

1. Asegúrate de tener **Python 3** instalado.
2. Descarga o clona el repositorio.
3. Abre una terminal en el directorio del proyecto.
4. Ejecuta el programa con:

```bash
python citas_medicas.py
