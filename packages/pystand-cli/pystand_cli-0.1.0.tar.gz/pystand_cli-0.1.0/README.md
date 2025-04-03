# PyStand-cli

This tool packages a Python project into a standalone executable using [PyStand](https://github.com/skywind3000/PyStand) and embeddable Python. It supports excluding specific directories and files, and provides a progress bar for file copying.

---

## Installation

1. **Install**:
   ```bash
   pip install pystand-cli
   ```

2. **Upgrade**:
   ```bash
   pip install --upgrade pystand-cli
   ```

---

## Usage

### Basic Command

```bash
pystand-cli entry_script.py [OPTIONS]
```

### Options

| Option            | Description                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------- |
| `--project-dir`   | The project directory (optional).                                                         |
| `--exclude-dirs`  | Folders to exclude (optional, can be specified multiple times).                           |
| `--exclude-files` | Files to exclude (optional, can be specified multiple times).                             |
| `--output-dir`    | The output directory (optional, default is `dist`).                                       |
| `--noconsole`     | Run the application without a console window (optional).                                  |
| `--python-repo`   | The Python FTP repository URL (optional, default is `https://www.python.org/ftp/python`). |

### Examples

1. **Package a project with an entry script**:

   ```bash
   pystand-cli entry_script.py --project-dir /path/to/project
   ```

2. **Exclude specific directories and files**:

   ```bash
   pystand-cli entry_script.py --project-dir /path/to/project --exclude-dirs node_modules --exclude-files .gitignore
   ```

3. **Run without a console window**:

   ```bash
   pystand-cli entry_script.py --project-dir /path/to/project --noconsole
   ```

4. **Custom output directory**:
   ```bash
   pystand-cli entry_script.py --project-dir /path/to/project --output-dir /path/to/output
   ```

---

## Output Structure

The output directory will contain the following structure:

```
output_dir/
├── runtime/                # Embeddable Python runtime
├── site-packages/          # Python site packages
├── main.exe                # PyStand executable
├── main.py                 # Entry script
└── ...                     # Other files and directories
```

---

## Notes

- **Embeddable Python**: The tool downloads the embeddable Python runtime from the official Python FTP repository.
- **PyStand**: PyStand is used to create a standalone executable from the entry script.
- **Exclusion**: Excluded directories and files are not copied to the output directory.
- **GUI Applications**: Use the `--noconsole` option to run the application without a console window. CLI applications should not use this option.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Please open an issue or submit a pull request.

---

## Acknowledgments

- [PyStand](https://github.com/skywind3000/PyStand) by skywind3000.
- [Click](https://click.palletsprojects.com/) for command-line interface support.
