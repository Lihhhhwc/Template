"""Console script for hamming."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("python-Hamming-package")
    click.echo("=" * len("python-Hamming-package"))
    click.echo("Python package hamming with MPI Evolutionary Biology branding.")


if __name__ == "__main__":
    main()  # pragma: no cover
