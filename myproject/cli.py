import click
import logging
import sys
import os

from myproject.utils.webcfg import config
from myproject.utils.configuration import Configuration
from myproject.backend.sample import hello


log = logging.getLogger("main")
log_format = "%(asctime)s | %(levelname)9s | %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)
CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CLICK_CONTEXT_SETTINGS)
@click.option('--configuration', '-c',
              required=False,
              default=None,
              type=str,
              help='Global configuration file, override user home folder')
def main(configuration):

    log.info("{} v{} ".format(config.name, config.get_version()))
    if configuration is None:
        filename = os.path.expanduser('~')
        configuration = os.path.join(filename, ".devops-cli", "configuration.yaml")
    global c
    c = Configuration(filename=configuration)


@main.command(context_settings=CLICK_CONTEXT_SETTINGS,
              name="version",
              help="Print build version")
def version():
    print(config.get_version())


@main.command(context_settings=CLICK_CONTEXT_SETTINGS,
              name="sample",
              help="invoke sample code")
@click.option('--name', '-n',
              required=False,
              default="You",
              type=str,
              help='Name to wave')
def sample(name):
    print(hello(name))
