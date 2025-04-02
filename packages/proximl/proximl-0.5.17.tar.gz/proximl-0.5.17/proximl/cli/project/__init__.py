import click
from proximl.cli import cli, pass_config, search_by_id_name


@cli.group()
@pass_config
def project(config):
    """proxiML project commands."""
    pass


@project.command()
@pass_config
def list(config):
    """List projects."""
    data = [
        ["ID", "NAME", "OWNER", "MINE"],
        [
            "-" * 80,
            "-" * 80,
            "-" * 80,
            "-" * 80,
        ],
    ]

    projects = config.proximl.run(config.proximl.client.projects.list())

    for project in projects:
        data.append(
            [
                project.id,
                project.name,
                project.owner_name,
                "X" if project.is_owner else "",
            ]
        )

    for row in data:
        click.echo(
            "{: >38.36} {: >30.28} {: >15.13} {: >4.4}" "".format(*row),
            file=config.stdout,
        )


@project.command()
@click.argument("name", type=click.STRING)
@pass_config
def create(config, name):
    """
    Create a project.

    Project is created with the specified NAME.
    """

    return config.proximl.run(
        config.proximl.client.projects.create(
            name=name,
        )
    )


@project.command()
@click.argument("project", type=click.STRING)
@pass_config
def remove(config, project):
    """
    Remove a project.

    PROJECT may be specified by name or ID, but ID is preferred.
    """
    projects = config.proximl.run(config.proximl.client.projects.list())

    found = search_by_id_name(project, projects)
    if None is found:
        raise click.UsageError("Cannot find specified project.")

    return config.proximl.run(found.remove())


from proximl.cli.project.secret import secret
from proximl.cli.project.credential import credential
from proximl.cli.project.data_connector import data_connector
from proximl.cli.project.datastore import datastore
from proximl.cli.project.service import service
