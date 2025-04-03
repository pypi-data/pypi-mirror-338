import os
import shutil
import sys
import tempfile
import zipfile
from distutils.sysconfig import get_python_lib
from pathlib import Path

import click
import httpx


def get_python_version():
    # Get the Python version and bitness
    version_info = sys.version_info
    bitness = 64 if sys.maxsize > 2**32 else 32
    return f"{version_info.major}.{version_info.minor}.{version_info.micro}", bitness


def download_file(uri: str, output_file: str):
    # Download a file from the internet
    output_dir = Path(output_file).parent.resolve()
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    with httpx.stream("GET", uri) as response:
        if response.status_code == 302:
            uri = response.headers.get("location")
            return download_file(uri, output_file)
        else:
            response.raise_for_status()
            total_size = int(response.headers.get("content-length", 0))
            with click.progressbar(
                length=total_size, label=f"Downloading {os.path.basename(output_file)}"
            ) as bar:
                with open(output_file, "wb") as f:
                    for chunk in response.iter_bytes(chunk_size=1024):
                        f.write(chunk)
                        bar.update(len(chunk))
    return output_file


@click.command()
@click.argument("entry_script", type=click.Path(exists=True))
@click.option(
    "--project-dir",
    type=click.Path(exists=True),
    help="The project directory (optional).",
)
@click.option(
    "--exclude-dirs",
    multiple=True,
    help="Folders to exclude (optional, only valid if project directory is provided).",
)
@click.option(
    "--exclude-files",
    multiple=True,
    help="Files to exclude (optional, only valid if project directory is provided).",
)
@click.option(
    "--output-dir",
    default="dist",
    type=click.Path(),
    help="The output directory (optional, default is 'dist').",
)
@click.option(
    "--noconsole",
    is_flag=True,
    help="Run the application without a console window.",
)
@click.option(
    "--python-repo",
    default="https://www.python.org/ftp/python",
    type=str,
    help="The Python FTP repository URL (optional, default is 'https://www.python.org/ftp/python').",
)
def package_project(
    entry_script,
    project_dir,
    exclude_dirs,
    exclude_files,
    output_dir,
    noconsole,
    python_repo,
):
    """
    Package a Python project into a specified output directory.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create a temporary directory for caching files
    cache_dir = tempfile.mkdtemp()

    # Get the Python version and bitness
    python_version, bitness = get_python_version()
    click.echo(
        f"Python Environment: {python_version} (64-bit)"
        if bitness == 64
        else "Python Environment: {python_version} (32-bit)"
    )

    # Download the embeddable Python zip file
    click.echo("Downloading embeddable Python...")
    if bitness == 64:
        uri = f"{python_repo}/{python_version}/python-{python_version}-embed-amd{bitness}.zip"
    else:
        uri = f"{python_repo}/{python_version}/python-{python_version}-embed-win32.zip"
    python_zip_file = download_file(
        uri, os.path.join(cache_dir, f"python-{python_version}-embed.zip")
    )
    click.echo(f"Python downloaded to '{python_zip_file}'.")

    # Unzip the embeddable Python zip file
    click.echo("Unzipping embeddable Python...")
    shutil.unpack_archive(python_zip_file, os.path.join(output_dir, "runtime"))
    click.echo(f"Python unzipped to '{os.path.join(output_dir, 'runtime')}'.")

    # Copy the Python Site Packages to the output directory
    site_packages = get_python_lib()
    # shutil.copytree(site_packages, os.path.join(output_dir, "site-packages"))
    with click.progressbar(
        os.listdir(site_packages), label="Copying Python Site Packages"
    ) as bar:
        for item in bar:
            s = os.path.join(site_packages, item)
            d = os.path.join(output_dir, "site-packages", item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks=True)
            else:
                shutil.copy2(s, d)
    click.echo(
        f"Python Site Packages copied to '{os.path.join(output_dir, 'site-packages')}'."
    )

    # Download PyStand
    click.echo("Downloading PyStand...")
    uri = "https://github.com/skywind3000/PyStand/releases/download/1.1.5/PyStand-v1.1.5-exe.zip"
    pystand_zip_file = download_file(uri, os.path.join(cache_dir, "pystand.zip"))
    click.echo(f"PyStand downloaded to '{pystand_zip_file}'.")

    # Unzip PyStand
    click.echo("Unzipping PyStand...")
    # 根据位数和是否需要隐藏控制台，选择解压不同的文件
    if noconsole:
        file_name = f"PyStand-mingw{bitness}-GUI/PyStand.exe"
    else:
        file_name = f"PyStand-mingw{bitness}-CLI/PyStand.exe"
    # 将file_name解压到output_dir，即解压到output_dir/pystand.exe
    with zipfile.ZipFile(pystand_zip_file, "r") as zip_ref:
        zip_ref.extract(file_name, cache_dir)
        shutil.move(
            os.path.join(cache_dir, file_name),
            os.path.join(
                output_dir, os.path.basename(entry_script).replace(".py", ".exe")
            ),
        )
    click.echo(f"PyStand unzipped to '{os.path.join(output_dir, 'pystand')}'.")

    # Copy the entry script to the output directory
    entry_script_name = os.path.basename(entry_script)
    shutil.copy(entry_script, os.path.join(output_dir, entry_script_name))
    click.echo(f"Entry script '{entry_script_name}' copied to '{output_dir}'.")

    # If project directory is provided, copy its contents (excluding specified folders)
    if project_dir:
        click.echo(f"Packaging project from directory: {project_dir}")

        # Collect all files to copy
        files_to_copy = []
        for root, dirs, files in os.walk(project_dir):
            # Exclude specified directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            # Collect files to copy
            for file in files:
                if file in exclude_files:
                    continue
                src_file = os.path.join(root, file)
                relative_path = os.path.relpath(root, project_dir)
                dst_file = os.path.join(output_dir, relative_path, file)
                files_to_copy.append((src_file, dst_file))

        # Copy files with a progress bar
        with click.progressbar(files_to_copy, label="Copying files") as bar:
            for src_file, dst_file in bar:
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                shutil.copy(src_file, dst_file)

        click.echo(f"Project packaged successfully to: {output_dir}")
    else:
        click.echo("No project directory provided. Only the entry script was copied.")


if __name__ == "__main__":
    package_project()
