# import rich_click as click
import click
import sys
from pathlib import Path
from .snake_wrapper import SnakeInstaller
from .useful_function import __command_required_option_from_option, __replace_package_name, __add_header
from .global_variable import __dict_context_settings

from .install import __install, __test_install
from .edit_files import __edit_tools, __edit_profile, __create_config, __show_tools
from .run import __run


def main_wrapper(soft_path=None, url=None, docs=None, description_tool=None, apptainer_url_files=None, datatest_url_files=None, **kargs) -> click.Group:
    """Use to wrapped snakemake workflow

        Args:
            - soft_path (str): The path of the wrapped workflow installation.
            - url (str): URL of versioning repository (GitHub or GitLab).
            - docs (str): URL of documentation.
            - description_tool (str): The header printed on the terminal when running the program.
                Please include string values 'VERSION', 'GIT_URL', and 'DOCS', and the wrapper automatically replaces them with the correct values.
            - apptainer_url_files (list(tuple())): List of tuples with downloaded URL and install destination with INSTALL_PATH, like INSTALL_PATH/containers/Apptainer.CulebrONT_tools.sif.
            - datatest_url_files (tuple): Tuple with 2 values, first the URL of datatest, second download name.
            - snakefile (str): Path to the main Snakemake script file (default: snakefiles/snakefile).
            - snakemake_scripts (str): Path to the main Snakemake script file (default: snakefiles/snakefile).
            - default_profile (str): Path to create the cluster 'default_profile' directory (default: default_profile/).
            - git_configfile_path (str): Path to the default configfile YAML (default: install_files/configfile.yaml).
            - git_tools_path (str): Path to the default tools config YAML (default: install_files/tools_path.yaml).
            - git_profile_config (str): Path to the default profile config file (default: install_files/config.yaml).
            - tools_version_path (str): Path to the csv with soft and command to get version (default: snakemake_scripts/report_template/versions.csv).
            - slurm_mode_choice (list): List of snakemake value for option --software-deployment-method (default: ['env-modules', 'apptainer', 'conda', "env-modules, conda"]).
            - local_mode_choice (list): List of snakemake value for option --software-deployment-method (default: ['apptainer']).

        Return:
            click.Group (``click.Group``): all sub-commands of workflow deployement and run

        Exemple:
            >>> from snakecdysis import main_wrapper
            >>> from podiumASM import dico_tool
            >>> main = main_wrapper(**dico_tool)
            >>> main()
            >>> main = main_wrapper(soft_path="path/to/install",
                                    url="http://Snakecdysis.com",
                                    docs=docs, description_tool=description_tool,
                                    apptainer_url_files=[('http://nas-bgpi.myds.me/DOC/rattleSNP/Apptainer.rattleSNP_tools.sif',
                                   'INSTALL_PATH/containers/Apptainer.rattleSNP_tools.sif'),
                                  ('http://nas-bgpi.myds.me/DOC/rattleSNP/Apptainer.report.sif',
                                   'INSTALL_PATH/containers/Apptainer.report.sif')
                                    datatest_url_files=("http://nas-bgpi.myds.me/DOC/rattleSNP/data_test_rattleSNP.zip", "data_test_rattleSNP.zip")
    """

    snake_installer = SnakeInstaller(soft_path=soft_path, url=url, docs=docs, description_tool=description_tool, apptainer_url_files=apptainer_url_files, datatest_url_files=datatest_url_files, **kargs)

    # Create click group for all subcommand line
    @click.group(name=f"{snake_installer.soft_name}", context_settings=__dict_context_settings,
                 invoke_without_command=True, no_args_is_help=False)
    @click.option('--restore', '-r', is_flag=True, required=False, default=False, show_default=True,
                  help='Restore previous installation to use again "install" command')
    @click.option('--install_env', '-e', is_flag=True, required=False, default=False, show_default=True,
                  help='print Install path, Tools config, Install mode, Tools install mode, Current version, Latest version avail, Snakecdysis version')
    @click.version_option(snake_installer.version, "-v", "--version", message="%(prog)s, version %(version)s")
    @click.pass_context
    @__add_header(snake_installer=snake_installer)
    def main_command(ctx, restore, install_env):
        """"""
        if ctx.invoked_subcommand is None and restore:  # and check_privileges():
            if snake_installer.install_mode in ["local", "cluster"]:
                snake_installer.install_mode_file.unlink(missing_ok=False)
                snake_installer.clean_home()
                click.secho(
                    f"\n    Remove installation mode, now run:\n    {snake_installer.soft_name} install_local or "
                    f"install_cluster\n\n", fg="yellow")
            else:
                click.secho(
                    f"\n    No reset need, {snake_installer.soft_name} not install !!!!!\n    Please run: "
                    f"{snake_installer.soft_name} install_local or install_cluster !!!!\n\n",
                    fg="red")
        elif ctx.invoked_subcommand is None and install_env:
            click.secho(f"""{snake_installer.soft_name} information's to help debug:
    - Install path:\t\t{snake_installer.install_path}
    - Tools config file: \t{snake_installer.get_active_tools_path}
    - Active profile:   \t{snake_installer.get_active_profile}
    - Install mode is:   \t{snake_installer.install_mode}
    - Tools install mode is: \t{snake_installer.tools_mode}
    - Current version is: \t{snake_installer.version}
    - Latest version avail is: \t{snake_installer.latest_version}
    - Snakecdysis version: \t{snake_installer.snakecdysis_version}
                  """,  fg="bright_blue")

        elif ctx.invoked_subcommand is None and (not install_env or not restore):
            click.echo(ctx.get_help())
        if not snake_installer.user_profile_config.exists() and snake_installer.install_mode == "cluster":
            click.secho(
                f"\n  Please run command line '{snake_installer.soft_name} edit_profile' before the first run of {snake_installer.soft_name} see {snake_installer.docs}\n\n",
                fg="red", err=True)

    ############################################
    # Install mode subcommand
    ############################################
    def choose_env(ctx, param, value):
        """
        Set the environment based on the mode specified in ctx.params.

        Args:
            ctx (object): The context object containing parameters.
            param (str): The parameter name.
            value (str): The value to set the environment to.

        Returns:
            str: The value of the environment set.

        Raises:
            click.BadParameter: If the specified value is not in the allowed choices.
        """
        # Define choices based on the mode
        mode = ctx.params.get('mode')
        choices = snake_installer.slurm_mode_choice if mode == 'slurm' else snake_installer.local_mode_choice if mode == 'local' else set(
            snake_installer.slurm_mode_choice + snake_installer.local_mode_choice)
        # Check if value is empty or parsing is resilient
        if not value or ctx.resilient_parsing:
            return
        # Check if the value is in the allowed choices
        if value not in choices:
            raise click.BadParameter(f"Unexpected value '{value}' with --mode '{mode}', Allowed values are: {choices}")
        # Set the environment value in ctx.params
        ctx.params['env'] = value
        return value

    # GLOBAL
    @click.command("install", short_help=f'Install {snake_installer.soft_name} on HPC cluster or on local mode',
                   context_settings=__dict_context_settings, no_args_is_help=False)
    @click.option('--mode', '-m', default="slurm", type=click.Choice(['slurm', 'local'], case_sensitive=False),
                  show_default=True, help='Mode for installation')
    @click.option('--env', '-e', default="apptainer",
                  type=click.Choice(set(snake_installer.slurm_mode_choice + snake_installer.local_mode_choice), case_sensitive=False),
                  show_default=True,
                  help=f'Mode for tools dependencies for slurm: {snake_installer.slurm_mode_choice}, local: {snake_installer.local_mode_choice}',
                  callback=choose_env)
    @click.option('--bash_completion/--no-bash_completion', is_flag=True, required=False, default=True,
                  show_default=True,
                  help=f'Allow bash completion of {snake_installer.soft_name} commands on the bashrc file')
    @click.pass_context
    def install(ctx, mode, env, bash_completion):
        """Run installation of tool for HPC cluster"""
        __install(snake_installer, mode, env, bash_completion)

    # TEST INSTALL
    @click.command("test_install",
                   short_help=f'Test {snake_installer.soft_name} { snake_installer.install_mode if snake_installer.install_mode in ["slurm","local"] else "local or slurm"} mode with "data_test"',
                   context_settings=__dict_context_settings, no_args_is_help=False)
    @click.option('--data_dir', '-d', default=None,
                  type=click.Path(exists=False, file_okay=False, dir_okay=True, readable=True, resolve_path=True),
                  required=True, show_default=False,
                  help='Path to download data test and create config.yaml to run test')
    @__replace_package_name(snake_installer=snake_installer)
    def test_install(data_dir):
        """Test_install function downloads a scaled data test, writes a configuration file adapted to it and
        proposes a command line already to run !!!"""
        __test_install(snake_installer, data_dir)

    ############################################
    # Run mode subcommand
    ############################################

    @click.command("run", short_help='Run workflow',
                   context_settings=__dict_context_settings, no_args_is_help=True)
    @click.option('--configfile', '-c', type=click.Path(exists=True, file_okay=True, readable=True, resolve_path=True),
                  required=True, show_default=True, help=f'Configuration file for run tool')
    @click.option('--pdf', '-pdf', is_flag=True, required=False, default=False, show_default=True,
                  help='Run snakemake with --dag, --rulegraph and --filegraph')
    @click.argument('snakemake_other', nargs=-1, type=click.UNPROCESSED)
    @__replace_package_name(snake_installer=snake_installer)
    def run(configfile, pdf, snakemake_other):
        """
        \b
        Run snakemake command line with mandatory parameters.
        SNAKEMAKE_OTHER: You can also pass additional Snakemake parameters using snakemake syntax.
        These parameters will take precedence over Snakemake ones, which were defined in the profile.
        See: https://snakemake.readthedocs.io/en/stable/executing/cli.html
        \b
        Example:
            rattleSNP run -c configfile.yaml --dry-run --jobs 200
            rattleSNP run -c configfile.yaml --threads 8 --dry-run
            rattleSNP run -c configfile.yaml --apptainer-args '--bind /mnt:/mnt'
        """
        __run(snake_installer, configfile, pdf, snakemake_other)

    ############################################
    # EDIT CONFIG subcommand
    ############################################

    @click.command("edit_tools", short_help='Edit own tools version', no_args_is_help=False)
    @click.option('--restore', '-r', is_flag=True, required=False, default=False, show_default=True,
                  help='Restore default tools_config.yaml (from install)')
    @__replace_package_name(snake_installer=snake_installer)
    def edit_tools(restore):
        """"""
        __edit_tools(snake_installer, restore)

    @click.command("create_config", short_help='Create configfile.yaml for run', no_args_is_help=True)
    @click.option('--configfile', '-c', default=None,
                  type=click.Path(exists=False, file_okay=True, dir_okay=False, readable=True, resolve_path=True),
                  required=True, show_default=True, help='Path to create configfile.yaml')
    @__replace_package_name(snake_installer=snake_installer)
    def create_config(configyaml):
        """"""
        __create_config(snake_installer, configyaml)

    @click.command("edit_profile", short_help='Edit config.yaml use by profile', no_args_is_help=False)
    @__replace_package_name(snake_installer=snake_installer)
    def edit_profile():
        """"""
        __edit_profile(snake_installer)

    @click.command("show_tools", short_help='show tools version', no_args_is_help=False)
    @__replace_package_name(snake_installer=snake_installer)
    def show_tools():
        """"""
        __show_tools(snake_installer)


    # Hack for build docs with unspecified install
    args = str(sys.argv)
    if "sphinx" in args:
        main_command.add_command(run)
        main_command.add_command(edit_profile)
        main_command.add_command(create_config)
        main_command.add_command(edit_tools)
        main_command.add_command(install)
        main_command.add_command(test_install)
        main_command.add_command(show_tools)
    else:
        if snake_installer.install_mode == "slurm" or snake_installer.install_mode == "local":
            main_command.add_command(edit_profile)
            if snake_installer.user_profile_config.exists():
                main_command.add_command(run)
                main_command.add_command(test_install)
                main_command.add_command(create_config)
                main_command.add_command(edit_tools)
                main_command.add_command(show_tools)
        else:
            main_command.add_command(install)
    return main_command
