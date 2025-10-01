# Turtle Art Sketches

A small collection of Turtle graphics scripts that draw Hirst-style dot paintings, spirographs, random walks, and other experiments. This repo is designed for quick experimentation and learning with Python's `turtle` module and simple color extraction.

---

## Features

* Hirst-style dot painting using colors extracted from an image (via `colorgram.py`).
* Spirograph, random walks, dashed lines, polygons and quick shape helpers.
* Small, editable scripts intended for learning and creative exploration.

## Requirements

* Python 3.8+ (desktop environment with GUI)
* `colorgram.py` (for palette extraction)

Install dependency:

```bash
pip install colorgram.py
```

> Optional: `Pillow` can be used for faster/more advanced palette extraction and exporting images.

## Running

1. Open a terminal in the project folder.
2. Run the script you want, for example:

```bash
python hirst.py  
```

**Notes & Tips**

* `turtle` draws to a GUI window. Run these scripts on your local machine (not in headless servers).
* Speed tips: use `screen.tracer(0)` + `screen.update()` and `t.speed('fastest')` to draw instantly.
* Keep `imagenow.jpeg` (or your source image) in the same folder as the script, or update the path in code.

## Files

* `hirst.py` — Hirst-style dot painting (example).

## Contributing

Feel free to open issues or submit improvements. Suggested ideas:

* Add a script to export the drawing as PNG.
* Use Pillow + k-means for improved color palettes.
* Create a small UI to pick images, palette size, grid size and export options.

## License

MIT License — feel free to reuse and tinker.

## Author

Ashish — enjoy experimenting and iterating! 🚀


