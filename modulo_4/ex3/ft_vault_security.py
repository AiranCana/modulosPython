#!/usr/bin/env python3
def secure_archive(file: str, op: str, wri: str = "") -> tuple[bool, str]:
    try:
        with open(file, op) as f:
            if op == "w":
                f.write(wri)
                return True, "Content successfully written to file"
            if op == "r":
                inter = f.read()
    except FileNotFoundError:
        return False, f"[Errno 2] No such file or directory: '{file}'"
    except PermissionError:
        return False, (f"[Errno 13] Permission denied: '{file}'")
    except Exception as e:
        return False, f"Error: {e}"
    return True, inter


if __name__ == "__main__":
    print("=== Cyber Archives Security ===", end="\n\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("secure_archive", "r"), end="\n\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("secure_archive", "r"), end="\n\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("secure_archive", "r"), end="\n\n")
    s = input("Using 'secure_archive' to write previous content" +
              "to a new file:")
    print(secure_archive("secure_archive", "r", s))
