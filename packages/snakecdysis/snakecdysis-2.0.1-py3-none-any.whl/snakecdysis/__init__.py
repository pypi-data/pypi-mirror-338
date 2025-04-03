from .snake_wrapper import SnakEcdysis, SnakeInstaller
from .cli_wrapper import main_wrapper
from .useful_function import *
from ._version import version as __version__
from ._version import version_tuple

__doc__ = """
Are you looking for a simplified installation process for your Snakemake workflows, including the various Python packages and the multitude of tools used by your pipelines? 

Would you like to simplify the use of your workflows with user-friendly commands and subcommands that even non-bioinformatician users can easy use? Look no further - Snakecdysis is the solution for you!

"""


dico_tool = {
        "soft_path":  Path(__file__).resolve().parent.joinpath("templates", "PKGNAME"),
        "url": "https://forge.ird.fr/phim/sravel/snakecdysis",
        "docs": "https://snakecdysis.readthedocs.io/en/latest/index.html",
        "description_tool": """ 
    Welcome to Snakecdysis version: VERSION! Created on January 2022
    @author: Sebastien Ravel (CIRAD),
    @email: sebastien.ravel@cirad.fr
    Please cite our github: GIT_URL
    Licencied under CeCill-C (http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html)
    and MIT Intellectual property belongs to CIRAD and authors.
    Documentation avail at: DOCS""",
        "apptainer_url_files": [('http://nas-bgpi.myds.me/DOC/rattleSNP/Singularity.rattleSNP_tools.sif',
                                   'INSTALL_PATH/containers/Singularity.rattleSNP_tools.sif'),
                                  ],
        "datatest_url_files": (
            "http://nas-bgpi.myds.me/DOC/rattleSNP/data_test_rattleSNP.zip", "data_test_rattleSNP.zip"),
    "snakemake_scripts": Path(__file__).resolve().parent.joinpath("templates", "PKGNAME", "snakemake_scripts")
    }