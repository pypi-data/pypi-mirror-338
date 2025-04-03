import click
from shutil import rmtree, unpack_archive
from .useful_function import multiprocessing_download
from pathlib import Path
import subprocess


def __install(snake_installer, mode, env, bash_completion):
    """
    Run installation of tool for HPC cluster.

    Args:
        snake_installer: The snake installer object.
        mode (str): The mode of installation (e.g. 'slurm' or 'local').
        env (str): The environment to install (e.g. 'apptainer' or 'env-modules').
        bash_completion (bool): Whether to enable bash completion.

    Raises:
        SystemExit: if Slurm is not found on the system.
    """
    # Remove previous installation
    snake_installer.clean_home()
    # Build default profile path
    default_profile = snake_installer.get_active_profile
    # Read default profile configuration
    profile_config_txt = snake_installer.git_profile_config.open("r").read()

    try:
        # Test if install has already been run
        if isinstance(default_profile, Path) and default_profile.exists() and click.confirm(
                click.style(f'    Profile "{default_profile}" exists. Do you want to remove and continue?\n\n', fg="red"),
                default=False, abort=True):
            rmtree(default_profile, ignore_errors=True)
        default_profile = snake_installer.default_profile
        default_profile.mkdir(exist_ok=True)

        # test if mode is slurm
        if mode == 'slurm':
            print(f"install on mode {mode}")
            profile_config_txt = profile_config_txt.replace("EXECUTOR", "slurm")
            # Get default partition from the system
            command = r"""sinfo -s | grep "*" | cut -d"*" -f1 """  # used admin default partition
            default_partition = subprocess.check_output(command, shell=True).decode("utf8").strip()
            if not default_partition:  # used in case of non default partition define by admin system
                command = r"""sinfo -s | cut -d" " -f1 | sed '/PARTITION/d' | head -n 1"""
                default_partition = subprocess.check_output(command, shell=True).decode("utf8").strip()
            if not default_partition:
                click.secho("    Error: Slurm was not found on your system !!", fg="red", err=True)
                snake_installer.fail()
                raise SystemExit
            profile_config_txt = profile_config_txt.replace("PARTITION", default_partition)



        # if local mode
        elif mode == 'local':
            profile_config_txt = profile_config_txt.replace("EXECUTOR", "local")
        # if apptainer activation
        if env == 'apptainer':
            profile_config_txt = profile_config_txt.replace("DEPLOYMENT", "apptainer")
            # check if already download
            snake_installer.check_and_download_apptainer()
            git_tools_file = snake_installer.git_tools_path.open("r").read()
            snake_installer.git_tools_path.open("w").write(git_tools_file.replace("INSTALL_PATH", f"{snake_installer.install_path}"))
        else:
            profile_config_txt = profile_config_txt.replace("DEPLOYMENT", "env-modules")
        # export to add bash completion
        if bash_completion:
            snake_installer.create_bash_completion()
        default_profile.joinpath("config.yaml").open("w").write(profile_config_txt)
        click.secho(f"\n    Profile is successfully installed on {default_profile}", fg="yellow")
        click.secho(
                f"    TODO: Please run command line '{snake_installer.soft_name} edit_profile' before the first run of {snake_installer.soft_name} see {snake_installer.docs}",
                fg="cyan", err=False)

        click.secho(f"\n    Congratulations, you have successfully installed {snake_installer.soft_name} !!!\n\n", fg="green", bold=True)
        snake_installer.install_mode_file.open("w").write(mode)
        snake_installer.install_mode_file.open("a").write(f"\n{env}")
    except Exception as e:
        click.secho(f"\n    ERROR : an error was detected, please check {e}", fg="red")
        snake_installer.fail()


def __install_cluster(snake_installer, env, bash_completion):
    """
     Run installation of tool for HPC cluster.
     Args:
         snake_installer: The snake installer object.
         env (str): The environment to install.
         bash_completion (bool): Whether to enable bash completion.
     Raises:
         SystemExit: if Slurm is not found on the system.
     """
    # Remove previous installation (ie @julie cluster then local)
    snake_installer.clean_home()
    # Build default profile path
    default_profile = snake_installer.default_profile

    try:
        # Test if install has already been run
        if default_profile.exists() and click.confirm(
                click.style(f'    Profile "{default_profile}" exists. Do you want to remove and continue?\n\n', fg="red"),
                default=False, abort=True):
            rmtree(default_profile, ignore_errors=True)
        default_profile.mkdir(exist_ok=True)

        # Read default cluster configuration
        default_cluster = snake_installer.git_profile_config.open("r").read()
        # Get default partition from the system
        command = r"""sinfo -s | grep "*" | cut -d"*" -f1 """   # used admin default partition
        default_partition = subprocess.check_output(command, shell=True).decode("utf8").strip()
        if not default_partition:      # used in case of non default partition define by admin system
            command = r"""sinfo -s | cut -d" " -f1 | sed '/PARTITION/d' | head -n 1"""
            default_partition = subprocess.check_output(command, shell=True).decode("utf8").strip()
        if not default_partition:
            click.secho("    Error: Slurm was not found on your system !!", fg="red", err=True)
            snake_installer.fail()
            raise SystemExit
        default_cluster = default_cluster.replace("PARTITION", default_partition)

        # if apptainer activation
        if env == 'apptainer':
            default_cluster = default_cluster.replace("DEPLOYMENT", "apptainer")
            # check if already download
            snake_installer.check_and_download_apptainer()
            git_tools_file = snake_installer.git_tools_path.open("r").read()
            snake_installer.git_tools_path.open("w").write(git_tools_file.replace("INSTALL_PATH", f"{snake_installer.install_path}"))
        else:
            default_cluster = default_cluster.replace("DEPLOYMENT", "env-modules")
        # export to add bash completion
        if bash_completion:
            snake_installer.create_bash_completion()
        default_profile.joinpath("config.yaml").open("w").write(default_cluster)
        click.secho(f"\n    Profile is success install on {default_profile}", fg="yellow")
        click.secho(
                f"    TODO: Please run command line '{snake_installer.soft_name} edit_profile' before the first run of {snake_installer.soft_name} see {snake_installer.docs}",
                fg="cyan", err=False)

        click.secho(f"\n    Congratulations, you have successfully installed {snake_installer.soft_name} !!!\n\n", fg="green", bold=True)
        snake_installer.install_mode_file.open("w").write("cluster")
        snake_installer.install_mode_file.open("a").write(f"\n{env}")
    except Exception as e:
        click.secho(f"\n    ERROR : an error was detected, please check {e}", fg="red")
        snake_installer.fail()


def __install_local(snake_installer, bash_completion):
    # rm previous install (ie @julie cluster then local)
    snake_installer.clean_home()
    # add path to download
    snake_installer.install_path.joinpath("containers").mkdir(exist_ok=True, parents=True)
    try:
        snake_installer.check_and_download_apptainer()
        # export to add bash completion
        if bash_completion:
            snake_installer.create_bash_completion()
        # good install
        click.secho(f"\n    Congratulations, you have successfully installed {snake_installer.soft_name} !!!\n\n", fg="green", bold=True)
        snake_installer.install_mode_file.open("w").write("local")
        snake_installer.install_mode_file.open("a").write("\napptainer")
    except Exception as e:
        snake_installer.install_mode_file.unlink(missing_ok=True)
        click.secho(f"\n    ERROR : an error was detected, please check {e}", fg="red")
        raise SystemExit


def __test_install(snake_installer, data_dir):
    """Test_install function downloads a scaled data test, writes a configuration file adapted to it and proposes a command line already to run !!!"""
    # create dir test and configure config.yaml
    data_dir = Path(data_dir).resolve()
    click.secho(f"\n    Created data test dir {data_dir}\n", fg="yellow")
    data_dir.mkdir(parents=True, exist_ok=True)

    data_config_path = data_dir.joinpath("data_test_config.yaml")
    click.secho(f"    Created config file to run data test: {data_config_path}\n", fg="yellow")
    txt = snake_installer.git_configfile_path.open("r").read().replace("DATA_DIR", f"{data_dir}")
    data_config_path.open("w").write(txt)

    # download data
    download_zip = data_dir.joinpath(snake_installer.datatest_url_files[1])
    if not Path(download_zip.as_posix()[:-4]).exists():
        if not download_zip.exists():
            click.secho(f"    Download data test\n", fg="yellow")
            multiprocessing_download([(snake_installer.datatest_url_files[0], download_zip.as_posix())], threads=1)
        click.secho(f"    Extract archive {download_zip} to {data_dir.as_posix()}\n", fg="yellow")
        unpack_archive(download_zip.as_posix(), data_dir.as_posix())
        download_zip.unlink()

    # build command line
    click.secho(f"    Write command line to run workflow on data test:\n", fg="yellow")
    mode = snake_installer.install_mode
    cmd = f"\n    {snake_installer.soft_name} {'run' if mode == 'cluster' else 'run --local-cores 1'} --configfile {data_config_path}\n\n"
    click.secho(cmd, fg='bright_blue')
