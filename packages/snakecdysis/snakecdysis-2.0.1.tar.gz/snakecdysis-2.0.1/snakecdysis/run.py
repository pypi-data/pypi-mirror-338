import click
from shutil import copyfile
import re
import subprocess
import sys


def rewrite_if_bind(snakemake_other):
    """
    Function to rewrite --bind params
    It modifies click.UNPROCESSED
    """
    bind_args = list(filter(re.compile(".*--bind.*").match, snakemake_other))  # Try to select --bind
    if bind_args:
        bind_args_rewrite = f'--apptainer-args "--bind {bind_args[0].split(" ")[1]}"'
        snakemake_other_list = list(filter(lambda x: x not in [bind_args[0], "--apptainer-args"], snakemake_other))  # remove value to rewrite
        snakemake_other_list.insert(0, bind_args_rewrite)
        return snakemake_other_list
    else:
        return snakemake_other


def build_pdf(cmd_snakemake_base):
    dag_cmd_snakemake = f"{cmd_snakemake_base} --dag | dot -Tpdf > schema_pipeline_dag.pdf"
    click.secho(f"    {dag_cmd_snakemake}\n", fg='bright_blue')
    process = subprocess.run(dag_cmd_snakemake, shell=True, check=False, stdout=sys.stdout, stderr=sys.stderr)
    if int(process.returncode) >= 1:
        raise SystemExit
    rulegraph_cmd_snakemake = f"{cmd_snakemake_base} --rulegraph | dot -Tpdf > schema_pipeline_global.pdf"
    click.secho(f"    {rulegraph_cmd_snakemake}\n", fg='bright_blue')
    process = subprocess.run(rulegraph_cmd_snakemake, shell=True, check=False, stdout=sys.stdout, stderr=sys.stderr)
    if int(process.returncode) >= 1:
        raise SystemExit
    filegraph_cmd_snakemake = f"{cmd_snakemake_base} --filegraph | dot -Tpdf > schema_pipeline_files.pdf"
    click.secho(f"    {filegraph_cmd_snakemake}\n", fg='bright_blue')
    process = subprocess.run(filegraph_cmd_snakemake, shell=True, check=False, stdout=sys.stdout, stderr=sys.stderr)
    if int(process.returncode) >= 1:
        raise SystemExit


def __run(snake_installer, configfile, pdf, snakemake_other):
    """
    \b
    Run snakemake command line with mandatory parameters.
    SNAKEMAKE_OTHER: You can also pass additional Snakemake parameters
    using snakemake syntax.
    These parameters will take precedence over Snakemake ones, which were
    defined in the profile.
    See: https://snakemake.readthedocs.io/en/stable/executing/cli.html

    Example:
        rattleSNP run -c configfile.yaml --dry-run --jobs 200
        rattleSNP run -c configfile.yaml --threads 8 --dry-run
        rattleSNP run -c configfile.yaml --apptainer-args '--bind /mnt:/mnt'

    """
    if not snake_installer.user_profile_config.exists():
        click.secho(f"    Please run command line '{snake_installer.soft_name} edit_profile' before the first run of {snake_installer.soft_name} see {snake_installer.docs}", fg="red", err=True)
        exit()
    profile = snake_installer.get_active_profile
    tools = snake_installer.get_active_tools_path

    # get user arguments
    click.secho(f'    Profile Path: {profile}', fg='yellow')
    click.secho(f'    configfile file: {configfile}', fg='yellow')
    click.secho(f'    Tools Path file: {tools}', fg='yellow')

    cmd_snakemake_base = f"snakemake -s {snake_installer.snakefile} --configfile {configfile} --workflow-profile {profile} {' '.join(rewrite_if_bind(snakemake_other))}"
    click.secho(f"\n    {cmd_snakemake_base}\n", fg='bright_blue')
    process = subprocess.run(cmd_snakemake_base, shell=True, check=False, stdout=sys.stdout, stderr=sys.stderr)
    if int(process.returncode) >= 1:
        raise SystemExit(f"""ERROR when running {snake_installer.soft_name} please see logs file.
If need you can open issue on your repository {snake_installer.git_url}, 
but please provide information about your installation with command: '{snake_installer.soft_name} --install_env'""")
    if pdf:
        build_pdf(cmd_snakemake_base)
