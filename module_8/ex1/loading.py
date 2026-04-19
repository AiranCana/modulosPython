import importlib
import importlib.metadata


def analice() -> None:
    import numpy.random as np
    from pandas import DataFrame as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    data = np.randn(1000)
    print("Processing 1000 data points...")
    df = pd(data, columns=["value"])
    print("Generating visualization...", end="\n\n")
    _, ax = plt.subplots()
    ax.hist(df["value"], bins=30, color="green", edgecolor="black")
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png", end="\n\n")


def check_version(real: str, necesari: str) -> bool:
    real_int = tuple(int(x) for x in real.split("."))
    necesari_int = tuple(int(x) for x in necesari.split("."))
    return real_int <= necesari_int


def helper(lis: list[tuple[str, str]]) -> None:
    for i in lis:
        pack, ver = i
        print(f" Need to install {pack}:")
        print(f"  pip:    pip install \"{pack}>={ver}\"")
        print(f"  poetry: poetry add  \"{pack}>={ver}\"", end="\n\n")


def requied() -> tuple[bool, list[tuple[str, str]]]:
    dir: dict[str, tuple[str, str]] = {
        "pandas":     ("2.0.0", "Data manipulation ready"),
        "numpy":      ("1.24.0", " Numerical computation ready"),
        "matplotlib": ("3.7.0", "Visualization ready")
    }
    lis = []
    valu = True
    for pack, data in dir.items():
        vers, text = data
        try:
            exist = importlib.import_module(pack)
            if exist is None:
                print(f" *!!* [MISSING] {pack} - is not intalled")
                valu = False
                lis.append((pack, vers))
            elif check_version(importlib.metadata.version(pack), vers):
                print(f" *!!* [MISSING] {pack} - is not intalled in"
                      f" version {vers}")
                valu = False
                lis.append((pack, vers))
            else:
                version = importlib.metadata.version(pack)
                print(f" [OK] {pack} ({version}) - {text}")
        except Exception:
            print(f" *!!* [MISSING] {pack} - is not intalled")
            valu = False
            lis.append((pack, vers))
    return valu, lis


def main() -> None:
    print("\nLOADING STATUS: Loading programs...", end="\n\n")
    print("Checking dependencies:")
    valu, lis = requied()
    print()
    if not valu:
        helper(lis)
        return
    else:
        try:
            analice()
        except Exception:
            print("It has not been implemented what is necessary")


if __name__ == "__main__":
    main()
    print("program closed")
