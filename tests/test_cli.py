import yadageschemas.validatecli
from click.testing import CliRunner
import os
import pytest

def test_validator():
    runner = CliRunner()
    result = runner.invoke(yadageschemas.validatecli.main,['workflow.yml','-t','tests/testspecs/local-helloworld'])
    assert result.exit_code == 0

    result = runner.invoke(yadageschemas.validatecli.main,['workflow.yml','-t','tests/testspecs/local-helloworld','-s'])
    assert result.exit_code == 0

def test_validator_noteven():
    runner = CliRunner()
    result = runner.invoke(yadageschemas.validatecli.main,['unknown'])
    assert result.exit_code == 1

def test_validator_invalid():
    runner = CliRunner()
    result = runner.invoke(yadageschemas.validatecli.main,['workflow.yml','-t','tests/testspecs/invalid'])
    assert result.exit_code == -1
