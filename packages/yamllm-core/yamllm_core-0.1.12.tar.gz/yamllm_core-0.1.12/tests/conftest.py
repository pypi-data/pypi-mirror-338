import sys
from pathlib import Path
import pytest

# Get the project root directory
ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

@pytest.fixture
def config():
    from yamllm.config import Config
    return Config()

@pytest.fixture
def parser():
    from yamllm.parser import Parser
    return Parser()