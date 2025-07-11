def greet(language):
    match language:
        case "English":
            print("Hello!")
        case "Spanish":
            print("¡Hola!")
        case "French":
            print("Bonjour!")
        case _:
            print("Language not supported.")

# Example usage
greet("Spanish")   # Output: ¡Hola!
greet("German")    # Output: Language not supported.
