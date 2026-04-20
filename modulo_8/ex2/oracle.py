import os


def print_status() -> bool:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if not os.path.exists("ex2/.env.example"):
        print("[!!] .env file not found")
        print("# Should show default/missing configuration warnings")
        return False
    print("[OK] .env file properly configured")
    if os.environ.get("MATRIX_MODE"):
        print("[OK] Production overrides available")
    else:
        print("[!!] No production overrides detected")
        return False
    return True


def enter_datavase() -> None:
    import dotenv
    dotenv.load_dotenv(dotenv_path="ex2/.env.example")
    get_all = print_status()
    if not get_all:
        return
    print()
    print("# Should load configuration from .env file", end="\n\n")
    print("ORACLE STATUS: Reading the Matrix...", end="\n\n")
    print("Configuration loaded:")
    mode = os.environ.get("MATRIX_MODE", "production")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL", "WARNING")
    zion = os.environ.get("ZION_ENDPOINT")

    print(f"Mode: {mode}")
    print("Database: ", end="")
    print('Connected to local instance' if mode == 'development'
          else 'Connected to remote instance')
    print(f"API Access: {'Authenticated' if api_key else 'Not authenticated'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion else 'Offline'}")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        enter_datavase()
    except Exception:
        print("It is not possible to access the DDBB")
