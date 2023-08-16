import argparse

from pathlib import Path

import json

from ro_crate_validate.exceptions import ROCrateJSONException, ROCrateException

from rocrate.rocrate import ROCrate

def load_crate(crate_dir):
    try:
        return ROCrate(crate_dir)
    except json.decoder.JSONDecodeError as e:
        raise ROCrateJSONException("ro-crate-metadata.json is not valid JSON")
    except ValueError as e:
        raise ROCrateException(e)

def check_json_ld(crate):
    pass


def check_root_entity(crate):
    pass




def ro_crate_validate(crate_dir):
    crate = load_crate(crate_dir)
    size = len(list(crate.get_entities()))
    print(f"Loaded crate with {size} entities")



def cli():
    ap = argparse.ArgumentParser("ro-crate-validate")
    ap.add_argument(
        "--dir",
        type=Path,
        help="RO-Crate directory to check",
    )
    args = ap.parse_args()
    if not args.dir.is_dir():
        raise ROCrateException(f"{args.dir} is not a directory")
    ro_crate_validate(args.dir)


if __name__ == "__main__":
    cli()
