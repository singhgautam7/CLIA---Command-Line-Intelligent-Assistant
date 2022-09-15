try:
    from . import cli
except ImportError:
    import cli


def main():
    cli.app(prog_name="clia")


if __name__ == "__main__":
    main()
