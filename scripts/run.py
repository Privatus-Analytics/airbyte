"""Run the manifest locally: python scripts/run.py spec|check|discover|read [--config ..] [--catalog ..] [--state ..]"""
import sys
from pathlib import Path

from airbyte_cdk.entrypoint import AirbyteEntrypoint, launch
from airbyte_cdk.sources.declarative.yaml_declarative_source import YamlDeclarativeSource

MANIFEST = str(Path(__file__).resolve().parent.parent / "manifest.yaml")

if __name__ == "__main__":
    args = sys.argv[1:]
    catalog_path = AirbyteEntrypoint.extract_catalog(args)
    config_path = AirbyteEntrypoint.extract_config(args)
    state_path = AirbyteEntrypoint.extract_state(args)
    config = YamlDeclarativeSource.read_config(config_path) if config_path else None
    catalog = YamlDeclarativeSource.read_catalog(catalog_path) if catalog_path else None
    state = YamlDeclarativeSource.read_state(state_path) if state_path else None
    source = YamlDeclarativeSource(path_to_yaml=MANIFEST, catalog=catalog, config=config, state=state)
    launch(source, args)
