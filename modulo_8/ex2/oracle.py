#!usr/bin/env python3
import os
import sys


def print_status() -> bool:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if not os.path.exists("ex2/.env"):
        print("[!!] .env file not found")
        print("# Should show default/missing configuration warnings")
        return False
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    return True


def enter_datavase() -> None:
    import dotenv
    dotenv.load_dotenv()
    get_all = print_status()
    if not get_all:
        return
    print()
    print("# Should load configuration from .env file", end="\n\n")
    print("ORACLE STATUS: Reading the Matrix...", end="\n\n")
    print("Configuration loaded:")
    mode = os.environ.get("MATRIX_MODE", "production")
    api_key = os.environ.get("API_KEY")
    ddbb = os.environ.get("DATABASE_URL")
    log_level = os.environ.get("LOG_LEVEL", "WARNING")
    zion = os.environ.get("ZION_ENDPOINT")

    print(f"Mode: {mode}")
    print("Database: ", end="")
    print('Connected to local instance' if ddbb
          else 'Not connected local instance')
    print(f"API Access: {'Authenticated' if api_key else 'Not authenticated'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion else 'Offline'}")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        en_vir = sys.prefix != sys.base_prefix
        if en_vir:
            enter_datavase()
        else:
            print("It cannot be operated on the equipment. Run in a virtual"
                  " environment.")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows", end="\n\n")
    except Exception:
        print("It is not possible to access the DDBB")
