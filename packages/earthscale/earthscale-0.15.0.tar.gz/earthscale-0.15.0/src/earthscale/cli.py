import click

from earthscale import EarthscaleClient


@click.group()
def cli() -> None:
    """Earthscale command line tool."""
    pass


@cli.command(help="Add a dataset to Earthscale using only a name and a URL.")
@click.argument("url")
@click.option(
    "-n",
    "--name",
    required=True,
    help="Name of the dataset as it will appear in Earthscale.",
)
@click.option(
    "-t",
    "--type",
    type=click.Choice(["vector", "image", "zarr", "tile_server"]),
    default="vector",
    help="Type of dataset to add. Defaults to vector.",
)
@click.option(
    "-p",
    "--proxy",
    is_flag=True,
    help="Use the proxy server for authentication.",
)
def add(
    url: str,
    name: str,
    type: str,
    proxy: bool,
) -> None:
    with EarthscaleClient(use_proxy=proxy) as client:
        try:
            if type == "vector":
                response = client.add_vector_dataset(name=name, url=url)
            elif type == "image":
                response = client.add_image_dataset(name=name, url=url)
            elif type == "zarr":
                response = client.add_zarr_dataset(name=name, url=url)
            elif type == "tile_server":
                response = client.add_tile_server_dataset(name=name, url=url)
            else:
                raise ValueError(f"Unknown dataset type: {type}")

            click.secho(
                f"Successfully added {type} dataset '{name}' with ID:"
                f" {response.dataset_id}",
                fg="green",
            )
        except Exception as e:
            click.secho(f"Failed to add dataset: {e!s}", err=True, fg="red")
            raise click.Abort() from None


@cli.command(help="Authenticate with Earthscale.")
@click.option(
    "-p",
    "--proxy",
    is_flag=True,
    help="Use the proxy server for authentication.",
)
def authenticate(proxy: bool) -> None:
    client = EarthscaleClient(use_proxy=proxy)
    # This automatically saves credentials after login
    try:
        client.login()
        click.secho("Successfully authenticated with Earthscale.", fg="green")
    except Exception as e:
        click.secho(
            f"Failed to authenticate with Earthscale: {e!s}", err=True, fg="red"
        )
        raise click.Abort() from None


if __name__ == "__main__":
    cli()
