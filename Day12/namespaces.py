# Namespaces: Local vs Global

################### Scope ####################

enemies = 1  # global scope


def increase_enemies():
    enemies = 5  # local scope
    # Local Scope - within functions

    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants - name of variable - capital letters
PI = 3.14159
