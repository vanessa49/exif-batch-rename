# EXIF Batch Rename

> **Status: Archived personal utility (2023).** Preserved as part of my early automation projects; not actively maintained.

A small Python script that recursively renames image files using their EXIF `DateTimeOriginal` timestamp so large photo folders can be sorted chronologically more easily.

## Features

- recursive directory scanning;
- EXIF capture-time extraction;
- filename prefixing with capture date/time;
- support for common image formats handled by Pillow.

## Requirements

- Python 3
- Pillow

```bash
pip install Pillow
```

## Usage

1. Back up the target photo folder first.
2. Set `path_to_top_folder` in the script.
3. Run:

```bash
python exif_batch_rename.py
```

The script modifies filenames in place, so review the code and test it on a copy before applying it to an important library.

## Why keep this repository public?

It is a small example of building a tool around a real personal workflow rather than treating scripting as an abstract exercise.

## License

MIT.
