## To run the heeh.xml design script:
## - Replace <path_to_rosetta> with the path to your Rosetta/main/source/bin directory.
## - Replace <extras> with the extra options that were set when building Rosetta (usually "default" for default compilation).
## - Replace <buildtype> with your build type (e.g. "linuxgccrelease" for the Linux operating system, gcc compiler, and release-mode compilation).
<path_to_rosetta>/rosetta_scripts.<extras>.<buildtype> -parser:protocol heeh.xml -aa_composition_setup_file heeh.hydrophobic.comp @input.flags
