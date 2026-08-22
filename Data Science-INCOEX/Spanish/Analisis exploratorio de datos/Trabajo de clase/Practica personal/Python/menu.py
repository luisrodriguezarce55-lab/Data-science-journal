# ==========================================
# MENÚ CON IMPORTS INDIVIDUALES
# ==========================================

while True:
    print("=" * 60)
    print("   MENÚ DE CONTROL Y GENERACIÓN DE GRÁFICOS E INFORMES   ")
    print("=" * 60)
    print("1. Ejercicio 1 -> Canales de Pedido de una cafeteria")
    print("2. Ejercicio 2 -> Técnico de soporte")
    print("3. Ejercicio 3 -> Registro de tiempos de espera en caja")
    print("4. Ejercicio 4 -> Intervalo de confianza y prueba de hipótesis")
    print("5. Ejercicio 5 -> Comparación de dos campañas de marketing")
    print("6. Salir del programa")
    print("=" * 60)

    opcion = input("Ingresa la opción a ejecutar (1-6): ").strip()

    if opcion == "1":
        print("\n Ejecutando Ejercicio 1...\n")
        import ejercicio_1

    elif opcion == "2":
        print("\n Ejecutando Ejercicio 2...\n")
        import ejercicio_2

    elif opcion == "3":
        print("\n Ejecutando Ejercicio 3...\n")
        import ejercicio_3

    elif opcion == "4":
        print("\n Ejecutando Ejercicio 4...\n")
        import ejercicio_4

    elif opcion == "5":
        print("\n Ejecutando Ejercicio 5...\n")
        import ejercicio_5

    elif opcion == "6":
        print("\n ¡Programa finalizado con éxito!")
        break

    else:
        print("\n Opción no válida. Ingresa un número del 1 al 6.\n")

    input("\nPresiona ENTER para regresar al menú principal...")