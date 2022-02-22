# Aims:
# Use crate::*; at top of each file.
# Generate mod files:
#   Fill mod files with:
#       Pub use file::*;
#       pub mod file;

import os
import glob


def process_mod(mod_dir):
    mod_path = mod_dir + "/mod.rs"
    lines = []
    if os.path.exists(mod_path):
        with open(mod_path, "r") as f:
            file_lines = f.readlines()
            for line in file_lines:
                lines.append(line.strip("\n"))

    filenames = next(os.walk(mod_dir), (None, None, []))[2]
    for file in filenames:
        if file == "mod.rs":
            continue
        file = file[:-3]  # Remove .rs
        a = f"pub use {file}::*;"
        b = f"pub mod {file};"
        if a not in lines:
            lines.insert(0, a)
        if b not in lines:
            lines.insert(0, b)

    with open(mod_path, "w") as f:
        for line in lines:
            f.write(line + "\n")

    pass


def process_file(file_path):
    lines = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            file_lines = f.readlines()
            for line in file_lines:
                lines.append(line.strip("\n"))

    my_line = "use crate::*;"
    if my_line in lines:
        lines.remove(my_line)
    lines.insert(0, my_line)

    with open(file_path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def main():
    project_dir = "C:/_C_/Home/Produce/Code/Projects/Rust/BigYoshis/LiteralPoggySource"
    target = f"{project_dir}/modules/smash/src"
    if os.path.exists(target + "/mod.rs"):
        process_mod(target)
    for root, subdirs, files in list(os.walk(target))[1:]:
        process_mod(root)
        print(root)
        for file in files:
            if file.endswith(".rs") and file != "mod.rs":
                process_file(root + "/" + file)


if __name__ == '__main__':
    main()
