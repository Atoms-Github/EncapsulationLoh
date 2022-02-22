# EncapsulationLoh

A small script for generating mod.rs files in a rust project, and mass-importing project files.
Aim:
 Use crate::*; at top of each file.
 Generate mod files:
   Fill mod files with:
       Pub use file::*;
       pub mod file;