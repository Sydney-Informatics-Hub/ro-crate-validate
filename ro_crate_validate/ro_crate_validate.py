import argparse

from pathlib import Path

from rocrate.rocrate import ROCrate

def ro_crate_validate(crate_dir):
    crate = ROCrate(crate_dir)
    for e in crate.get_entities():
        print(e.id, e.type)


def cli():
    ap = argparse.ArgumentParser("ro-crate-validate")
    ap.add_argument(
        "--dir",
        type=Path,
        help="RO-Crate directory to check",
    )
    args = ap.parse_args()
    ro_crate_validate(args.dir)


if __name__ == "__main__":
    cli()
