"""Console script for template."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("python-template-package")
    click.echo("=" * len("python-template-package"))
    click.echo("Python package template with MPI Evolutionary Biology branding.")


if __name__ == "__main__":
    main()  # pragma: no cover
