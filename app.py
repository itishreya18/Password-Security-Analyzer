from rich.console import Console
from rich.panel import Panel

from modules.hashing import generate_hash, save_hash
from modules.password_strength import check_password_strength
from modules.search_space import (
    calculate_search_space,
    estimate_time,
    convert_seconds
)
from modules.benchmark import benchmark_hashes
from modules.salt import generate_salted_hash
from modules.entropy import calculate_entropy

console = Console()


# =====================================================
# Generate Password Hash
# =====================================================
def generate_password_hash():

    password = console.input("\n[bold yellow]Enter Password:[/] ")

    console.print("\nChoose Hash Algorithm")
    console.print("1. MD5")
    console.print("2. SHA1")
    console.print("3. SHA256")
    console.print("4. SHA512")

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha512"
    }

    choice = console.input("\nChoice: ")

    if choice not in algorithms:
        console.print("[bold red]Invalid Choice![/bold red]")
        return

    algorithm = algorithms[choice]

    hashed = generate_hash(password, algorithm)

    save_hash(password, algorithm, hashed)

    console.print("\n[bold green]Hash Generated Successfully[/bold green]")

    console.print(f"Algorithm : {algorithm.upper()}")
    console.print(f"Hash      : {hashed}")


# =====================================================
# Password Strength
# =====================================================
def password_strength_menu():

    password = console.input("\nEnter Password: ")

    strength, feedback = check_password_strength(password)

    colors = {
        "Weak": "red",
        "Medium": "yellow",
        "Strong": "green"
    }

    console.print(
        f"\nStrength : [{colors.get(strength,'white')}]{strength}[/{colors.get(strength,'white')}]"
    )

    if feedback:
        console.print("\nSuggestions")

        for item in feedback:
            console.print(f"• {item}")


# =====================================================
# Search Space Calculator
# =====================================================
def search_space_menu():

    console.print("\n[bold cyan]Brute Force Search Space Calculator[/bold cyan]")

    try:
        length = int(console.input("\nPassword Length: "))
    except ValueError:
        console.print("[red]Please enter a valid number.[/red]")
        return

    console.print("\nCharacter Set")

    console.print("1. Numbers (10)")
    console.print("2. Lowercase (26)")
    console.print("3. Lowercase + Uppercase (52)")
    console.print("4. Lowercase + Uppercase + Numbers (62)")
    console.print("5. All Printable Characters (95)")

    charset = {
        "1": 10,
        "2": 26,
        "3": 52,
        "4": 62,
        "5": 95
    }

    choice = console.input("\nChoice: ")

    if choice not in charset:
        console.print("[red]Invalid Choice[/red]")
        return

    size = charset[choice]

    total = calculate_search_space(length, size)

    console.print("\n[bold green]Results[/bold green]")

    console.print(f"Character Set Size : {size}")
    console.print(f"Password Length    : {length}")
    console.print(f"Search Space       : {total:,}")

    console.print("\nEstimated Time")

    speeds = {
        "1 Thousand/sec": 1000,
        "1 Million/sec": 1000000,
        "1 Billion/sec": 1000000000
    }

    for label, speed in speeds.items():

        seconds = estimate_time(total, speed)

        console.print(
            f"{label:<20}: {convert_seconds(seconds)}"
        )


# =====================================================
# Hash Benchmark
# =====================================================
def benchmark_menu():

    console.print("\n[bold cyan]Hash Benchmark[/bold cyan]")

    password = console.input("\nEnter Password: ")

    results = benchmark_hashes(password)

    console.print("\n[bold green]Results[/bold green]\n")

    for algorithm, time_taken in results.items():

        console.print(
            f"{algorithm:<8}: {time_taken:.10f} seconds"
        )


# =====================================================
# Salt Demonstration
# =====================================================
def salt_demo():

    console.print("\n[bold cyan]Salted Hash Demonstration[/bold cyan]")

    password = console.input("\nEnter Password: ")

    salt, salted_hash = generate_salted_hash(password)

    console.print("\nGenerated Salt")
    console.print(salt)

    console.print("\nSalted SHA256 Hash")
    console.print(salted_hash)

    console.print(
        "\n[green]Run this again using the same password."
        "\nYou'll get a different salt and therefore a different hash.[/green]"
    )


# =====================================================
# Password Entropy
# =====================================================
def entropy_menu():

    console.print("\n[bold cyan]Password Entropy Calculator[/bold cyan]")

    password = console.input("\nEnter Password: ")

    entropy, rating = calculate_entropy(password)

    colors = {
        "Very Weak": "red",
        "Weak": "red",
        "Reasonable": "yellow",
        "Strong": "green",
        "Very Strong": "bright_green"
    }

    console.print(f"\nEntropy : {entropy} bits")
    console.print(
        f"Rating  : [{colors.get(rating,'white')}]{rating}[/{colors.get(rating,'white')}]"
    )

    console.print("\nTips")
    console.print("• Use longer passwords.")
    console.print("• Mix uppercase and lowercase letters.")
    console.print("• Include numbers and symbols.")
    console.print("• Avoid common words or predictable patterns.")


# =====================================================
# Main Menu
# =====================================================
while True:

    console.print(
        Panel.fit(
            "[bold cyan]PASSWORD SECURITY ANALYZER[/bold cyan]"
        )
    )

    console.print("\n1. Generate Password Hash")
    console.print("2. Password Strength Checker")
    console.print("3. Brute Force Search Space Calculator")
    console.print("4. Hash Benchmark")
    console.print("5. Salted Hash Demonstration")
    console.print("6. Password Entropy Calculator")
    console.print("7. Exit")

    choice = console.input("\nEnter Choice: ")

    if choice == "1":
        generate_password_hash()

    elif choice == "2":
        password_strength_menu()

    elif choice == "3":
        search_space_menu()

    elif choice == "4":
        benchmark_menu()

    elif choice == "5":
        salt_demo()

    elif choice == "6":
        entropy_menu()

    elif choice == "7":
        console.print(
            "\n[bold green]Thank you for using Password Security Analyzer![/bold green]"
        )
        break

    else:
        console.print("\n[bold red]Invalid Choice![/bold red]")

    input("\nPress Enter to continue...")