from click.testing import CliRunner
import pytest
import myproject.cli as cli


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
