"""Frontend of the project (Argument handling and stuff)"""

import sys
from pathlib import Path
from argparse import ArgumentParser
from maketree.core.parser import Parser, ParseError
from maketree.core.validator import Validator, ValidationError
from maketree.core.extractor import Extractor
from maketree.core.tree_writer import TreeWriter
from maketree.core.tree_builder import TreeBuilder
from maketree.core.normalizer import Normalizer
from maketree.console import Console
from maketree.utils import (
    is_valid_dirpath,
    get_existing_paths,
    print_tree,
    create_dir,
)
from typing import List, Dict


PROGRAM = "maketree"
VERSION = "1.2.0"


def main():
    args = parse_args()

    sourcefile = args.src
    dstpath = Path(args.dst)
    CREATE_DST = args.create_dst
    EXTRACT_TREE = args.extract_tree
    VERBOSE: bool = args.verbose
    OVERWRITE: bool = args.overwrite
    SKIP: bool = args.skip
    PRINT_TREE = args.graphical
    NO_COLORS = args.no_color
    NO_CONFIRM = args.no_confirm

    # Console? (is this fuc**ing Yavascript?)
    console = Console(VERBOSE, NO_COLORS)

    # Mutually Exclusive
    if OVERWRITE and SKIP:
        console.error(
            console.color_substrs(
                "Options --overwrite and --skip are mutually exlusive. ",
                ["--overwrite", "--skip"],
                "light_yellow",
            )
        )

    # Source .tree not provided?
    if not sourcefile:
        if not EXTRACT_TREE:
            console.error("the following argument is required: src")

        # Convert path into Path object
        extract_tree_path = Path(EXTRACT_TREE)

        if not extract_tree_path.exists():
            console.error(f"the following path does not exist: '{extract_tree_path}'")

        # Extract tree into a file
        extracted_tree = Extractor.extract(extract_tree_path, console=console)

        # Pass the tree into FileWriter
        filename = TreeWriter.write(extracted_tree, console)

        print(
            console.color_substrs(
                f"Tree has been extracted into '{filename}'",
                [filename],
                "light_green",
            )
        )
        sys.exit(0)

    # Convert to Path object
    sourcefile = Path(sourcefile)

    # SRC Exists?
    if not sourcefile.exists():
        console.error("source '%s' does not exist." % sourcefile)

    # SRC Tree file?
    if not sourcefile.name.endswith(".tree"):
        console.error("source '%s' is not a .tree file." % sourcefile)

    # DST Exists?
    if not dstpath.is_dir():
        if CREATE_DST:
            console.verbose("Validating '%s'..." % dstpath)
            valid = is_valid_dirpath(dstpath)
            if valid is not True:
                console.error(valid)
        else:
            console.error(
                console.color_substrs(
                    "destination path '%s' does not exist." % dstpath,
                    [dstpath],
                    "light_red",
                )
            )

    # Parse the source file
    console.verbose("Parsing %s..." % sourcefile)
    parsed_tree = Parser.parse_file(sourcefile)

    # Validate the parsed tree (Does nothing on Pass, Exits on fail)
    console.verbose("Validating parsed tree...")
    try:
        Validator.validate(parsed_tree, console=console)
    except ValidationError as e:
        print(e)
        sys.exit(1)

    # Print the graphical tree and Exit.
    if PRINT_TREE:
        print_tree(parsed_tree, root=dstpath, console=console)
        sys.exit(0)

    # Confirm before proceeding
    if not NO_CONFIRM:
        print_tree(parsed_tree, root=dstpath, console=console)
        proceed: bool = console.input_confirm(
            "Create this structure? (y/N): ", fgcolor="light_magenta"
        )
        if not proceed:
            sys.exit(0)

    console.verbose("Creating tree paths...")

    # Create paths from tree nodes
    paths: Dict[str, List[str]] = Normalizer.normalize(parsed_tree, dstpath)

    # If Overwrite and Skip both are false
    if not OVERWRITE and not SKIP:
        # Check existing paths
        console.verbose("Checking existing paths...\n")
        existing_paths = get_existing_paths(paths["files"])
        count = len(existing_paths)
        # Any path exists?
        if count:
            console.print_lines(
                existing_paths,
                "Warning: File already exists: ",
                color="light_yellow",
                force_print=False,
            )
            print()
            console.error(
                console.color_substrs(
                    f"Found {count} existing files, cannot proceed. "
                    "(try --skip or --overwrite)",
                    ["--skip", "--overwrite"],
                    "light_yellow",
                )
            )

    # Create dstpath here...
    console.verbose("Creating '%s'..." % dstpath)
    created = create_dir(dstpath)
    if created is not True:
        console.error(created)

    console.verbose("Creating tree in '%s'...\n" % dstpath)

    # Create the files and dirs finally
    build_count = TreeBuilder.build(
        paths,
        console,
        skip=SKIP,
        overwrite=OVERWRITE,
    )

    # Completion message
    built_dirs = f"{build_count[0]} directories"
    built_files = f"{build_count[1]} files"

    print(
        console.color_substrs(
            f"\n{built_dirs} and {built_files} have been created.",
            [built_dirs, built_files],
            "light_green",
        )
    )


def parse_args():
    """Parse command-line arguments and return."""

    parser = ArgumentParser(
        prog=PROGRAM,
        usage="%(prog)s [OPTIONS]",
        epilog="%s %s" % (PROGRAM.title(), VERSION),
        description="Create complex project structures effortlessly.",
    )

    parser.add_argument(
        "src",
        nargs="?",
        help="source file (with .tree extension)",
    )
    parser.add_argument(
        "dst",
        nargs="?",
        default=".",
        help="where to create the tree structure (default: %(default)s)",
    )
    parser.add_argument(
        "-cd",
        "--create-dst",
        action="store_true",
        help="create destination folder if it doesn't exist.",
    )
    parser.add_argument(
        "-et",
        "--extract-tree",
        metavar="",
        help="write directory tree into a .tree file. (takes a PATH)",
    )
    parser.add_argument(
        "-g",
        "--graphical",
        action="store_true",
        help="show source file as graphical tree and exit",
    )
    parser.add_argument(
        "-o", "--overwrite", action="store_true", help="overwrite existing files"
    )
    parser.add_argument("-s", "--skip", action="store_true", help="skip existing files")
    parser.add_argument(
        "-nc",
        "--no-color",
        action="store_true",
        help="don't use colors in output",
    )
    parser.add_argument(
        "-nC",
        "--no-confirm",
        action="store_true",
        help="don't ask for confirmation",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="enable verbose mode"
    )

    return parser.parse_args()
