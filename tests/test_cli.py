from click.testing import CliRunner
import pytest
import myproject.cli as cli
from myproject.utils.webcfg import Config


@pytest.mark.parametrize("cli_method, help_txt", [
    (cli.version, "Print build version"),
    (cli.sample, "invoke sample code")
])
@pytest.mark.unit
def test_cli_help(cli_method, help_txt):
    runner = CliRunner()

    result = runner.invoke(cli_method, ["-h"])
    assert result.exit_code == 0
    assert help_txt in result.output


@pytest.mark.unit
def test_cli_version():
    runner = CliRunner()

    result = runner.invoke(cli.version, [])
    assert result.exit_code == 0
    assert result.output.strip() == Config.get_version()


@pytest.mark.unit
def test_cli_sample():
    runner = CliRunner()

    result = runner.invoke(cli.sample, [])
    assert result.exit_code == 0
    assert "Hello" in result.output.strip()
