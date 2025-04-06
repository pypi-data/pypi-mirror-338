.. contents:: Table of Contents
   :depth: 2
   :backlinks: entry

Requirements
============

CulebrONT requires |PythonVersions|, |graphviz|

Optional: |Apptainer| |Singularity|

CulebrONT is developed to work mostly on an HPC distributed cluster but a local, single machine, installation is also possible.

------------------------------------------------------------------------

Install CulebrONT PyPI package
===============================

First, install the CulebrONT python package with pip.

You can install the latest available version |release|

.. code-block:: bash

   python3 -m pip install culebrONT
   culebrONT --help

Optionally, you can specify the version such as :

.. code-block:: bash

   python3 -m pip install culebrONT==4.0.0
   culebrONT --help


Now, follow this documentation according to what you want, local or HPC mode.


------------------------------------------------------------------------

Steps for installation
============================

Install CulebrONT using ``culebrONT install`` command line.

.. click:: culebrONT.main:main
    :prog: culebrONT
    :commands: install_local
    :nested: full
    :hide-header:


.. code-block:: bash

    Usage: culebrONT install [OPTIONS]

      Run installation of tool for HPC cluster

    Options:
      -m, --mode [slurm|local]        Mode for installation  [default: slurm]
      -e, --env [env-modules|apptainer]
                                      Mode for tools dependencies for slurm: ['env-modules', 'apptainer'], local: ['env-modules', 'apptainer']
                                      [default: apptainer]
      --bash_completion / --no-bash_completion
                                      Allow bash completion of culebrONT commands on the bashrc file  [default: bash_completion]


    Optionally (but recommended), after installing in local, you can check the CulebrONT installation using a dataset scaled for single machine.
    See the section :ref:`Check install` for details.


Install CulebrONT in local mode by using ``culebrONT install -m local`` or in a HPC cluster using ``culebrONT install -m slurm`` (default mode) command line.


if you have installed culebrONT with cluster mode, it's possible to chose between apptainer or use module environments usually available in HPC. In local mode, only apptainer is avail.  Use the option ``-e, --env [env-modules|apptainer]``.


if tools dependencies are installed using ``Apptainer``, an image is automatically downloaded and used by the configuration files of the pipeline. Local mode install, without scheduler, is constrains to use this apptainer image.

.. warning::
   An Apptainer image is downloaded in the location of the package CulebrONT. Be careful these images need at approximately 3.5 G of free space. If installed with Pypi with the flag --user (without root), the package is installed in your HOME.

------------------------------------------------------------------------

Steps for HPC distributed cluster installation
==============================================


If you have already install culebrONT in your cluster by the command `culebrONT install -m slurm` as explained before, you need to configurate resources allocated by each soft used. CulebrONT uses any available snakemake profiles to ease cluster installation and resources management. So, please adapt a few files according to your own system architecture.

.. click:: culebrONT.main:main
    :prog: culebrONT
    :commands: install_cluster
    :nested: full
    :hide-header:

1. Adapt `profile` and `config.yaml`
---------------------------------------------

Now that CulebrONT is installed, it proposes default configuration files, but they can be modified. .

1. Adapt the pre-formatted `snakemake profil` to configure your cluster options.
See the section :ref:`1. Snakemake profiles` for details.

2. Adapt the :file:`config.yaml` file to manage cluster resources such as partition, memory and threads available for each job.
See the section :ref:`2. Adapting *config.yaml*` for further details.


2. Adapt `tools_path.yaml`
--------------------------

As CulebrONT uses many tools, you must install them using one of the two following possibilities:

1. Either through the |Apptainer| containers,

2. Or using the ``module load`` mode,

.. code-block:: bash

   culebrONT install --help
   culebrONT install --mode slurm --env modules
   # OR
   culebrONT install --mode slurm --env apptainer

If ``--env apptainer`` argument is specified, CulebrONT will download previously build Apptainer images, containing the complete environment need to run CulebrONT (tools and dependencies).

Adapt the file :file:``tools_path.yaml`` - in YAML (Yet Another Markup Language) - format  to indicate CulebrONT where the different tools are installed on your cluster.

See the section :ref:`3. How to configure tools_path.yaml` for details.


------------------------------------------------------------------------

Check install
==============

In order to test your install of CulebrONT, a data test called ``Data-Xoo-sub/`` is available at https://itrop.ird.fr/culebront_utilities/.

.. click:: culebrONT.main:main
    :prog: culebrONT
    :commands: test_install
    :nested: full
    :hide-header:

This dataset will be automatically downloaded by CulebrONT in the ``-d`` repertory using :

.. code-block:: bash

   culebrONT test_install -d test

Launching the (suggested, to be adapted) command line in CLUSTER mode will perform the tests:

.. code-block:: bash

   culebrONT run --configfile test/data_test_config.yaml

In local mode, type :

.. code-block:: bash

   culebrONT run -t 8 -c test/data_test_config.yaml --apptainer-args "--bind $HOME"


------------------------------------------------------------------------

Advance installation
====================


1. Snakemake profiles
---------------------

The Snakemake-profiles project is an open effort to create configuration profiles allowing to execute Snakemake in various computing environments
(job scheduling systems as Slurm, SGE, Grid middleware, or cloud computing), and available at https://github.com/Snakemake-Profiles/doc.

In order to run CulebrONT on HPC cluster, we take advantages of profiles.

Quickly, see `here <https://github.com/SouthGreenPlatform/culebrONT/blob/master/culebrONT/install_files/config.yaml>`_ an example of the Snakemake SLURM profile we used for the French national bioinformatics infrastructure at IFB.

More info about profiles can be found here https://github.com/Snakemake-Profiles/slurm#quickstart.

Preparing the profile's *config.yaml* file
******************************************

Once your basic profile is created, to finalize it, modify as necessary the ``culebrONT/culebrONT/default_profile/config.yaml`` to customize Snakemake parameters that will be used internally by CulebrONT:

.. code-block:: ini

   restart-times: 0
   jobscript: "slurm-jobscript.sh"
   cluster: "slurm-submit.py"
   cluster-status: "slurm-status.py"
   max-jobs-per-second: 1
   max-status-checks-per-second: 10
   local-cores: 1
   jobs: 200                   # edit to limit the number of jobs submitted in parallel
   latency-wait: 60000000
   use-envmodules: true        # adapt True/False for env of apptainer, but only active one possibility !
   use-apptainer: false
   rerun-incomplete: true
   printshellcmds: true


2. Adapting *config.yaml*
----------------------------------

In the ``config.yaml`` file, you can manage HPC resources, choosing partition, memory and threads to be used by default,
or specifically, for each rule/tool depending on your HPC Job Scheduler (see `there <https://snakemake.readthedocs.io/en/latest/snakefiles/configuration.html#cluster-configuration-deprecated>`_). This file generally belongs to a Snakemake profile (see above).

.. warning::
   If more memory or threads are requested, please adapt the content
   of this file before running on your cluster.

To access to the `config.yaml` file you must use

.. code-block:: bash

   culebrONT edit_profile

The edited `config.yaml` file will be save in your home `/home/USER/.config/` path.  A list of CulebrONT rules names can be found in the section :ref:`Threading rules inside culebrONT`.


.. warning::
   For some rules in the *config.yaml* as `rule_graph` or `run_get_versions`,
   we use by default wildcards, please don't remove it.


3. How to configure tools_path.yaml
-----------------------------------

.. note::
    About versions of tools, the user can choose themself what version of tools to use with modules or with apptainer.
    HOWEVER, the pipeline was validated with specific versions (check the `apptainer def <https://github.com/SouthGreenPlatform/culebrONT/blob/master/culebrONT/containers/apptainer.culebront_tools.def>`_) so it may leads to error due to parameter changes.
    :ref:`Assembly`


To access to the `config.yaml` file you must use

.. code-block:: bash

   culebrONT edit_tools


In the ``tools_path`` file, you can find two sections: APPTAINER and ENVMODULES. In order to fill it correctly, you have 2 options:

1. Use only APPTAINER containers: in this case, fill only this section. Put the path to the built apptainer images you want to use.
Absolute paths are strongly recommended. See the section :ref:`'How to build apptainer images'<How to build apptainer images>`  for further details.

.. literalinclude:: ../../culebrONT/install_files/tools_path.yaml
   :language: YAML
   :lines: 6-8

.. warning::
   To ensure APPTAINER containers to be really used, one needs to make
   sure that the *--use-apptainer* flag is included in the snakemake command line.


2. Use only ENVMODULES: in this case, fill this section with the modules available on your cluster (here is an example):

.. literalinclude:: ../../culebrONT/install_files/tools_path.yaml
   :language: YAML
   :lines: 10-18

.. warning::
   Make sure to specify the *--use-envmodules* flag in the snakemake command
   line for ENVMODULE to be implemented.
   More details can be found here:
   https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#using-environment-modules


------------------------------------------------------------------------

And more ...
-------------

How to build Apptainer images
*******************************

You can build your own image using the available *.def* recipes from the ``culebrONT/culebrONT/containers/`` directory.

.. warning::
   Be careful, you need root access to build apptainer images

.. code-block:: bash

   cd culebrONT/culebrONT/containers/
   sudo apptainer build apptainer.culebront_tools.sif apptainer.culebront_tools.def


Threading rules inside CulebrONT
********************************

Please find here the rules names found in CulebrONT code.
It is recommended to set threads using the snakemake command when running on a single machine,
or in a cluster configuration file to manage cluster resources through the job scheduler.
This would save users a painful exploration of the snakefiles of CulebrONT.

.. code-block:: python

    run_flye
    run_canu
    run_minimap_for_miniasm
    run_miniasm
    run_minipolish
    run_raven
    convert_fastq_to_fasta
    run_smartdenovo
    run_shasta
    run_circlator
    tag_circular
    tag_circular_to_minipolish
    rotate_circular
    run_fixstart
    index_fasta_to_correction
    run_minialign_to_medaka
    run_medaka_train
    run_medaka_consensus
    run_pilon_first_round
    run_pilon
    rule run_racon
    preparing_fasta_to_quality
    run_quast
    run_busco
    run_diamond
    run_minimap2
    run_blobtools
    run_mummer
    run_assemblytics
    run_mauve
    run_bwa_mem2
    run_flagstat
    run_merqury
    run_benchmark_time
    stats_assembly
    rule_graph
    run_report_snakemake
    run_flagstats_stats
    run_busco_stats
    rule_graph
    copy_final_assemblies
    report_by_sample
    report_about_workflow
    ipynb_convert_samples_qmd
    ipynb_convert_qmd
    edit_quarto
    build_book


.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/culebront
   :target: https://www.python.org/downloads
   :alt: Python 3.12+

.. |SnakemakeVersions| image:: https://img.shields.io/badge/snakemake-%3E8.0.0-red
   :target: https://snakemake.readthedocs.io/en/v8.0.0/
   :alt: Snakemake 8

.. |graphviz| image:: https://img.shields.io/badge/graphviz-%3E%3D2.40.1-green
   :target: https://graphviz.org/
   :alt: graphviz 2.40.1+

.. |release| image:: https://img.shields.io/gitlab/v/release/diade%2Fculebront_pipeline?gitlab_url=https%3A%2F%2Fforge.ird.fr&sort=semver&display_name=release
   :target: https://forge.ird.fr/diade/culebront_pipeline/-/releases/

.. |Apptainer| image:: https://img.shields.io/badge/Apptainer->1.3.2-blue
   :target: https://sylabs.io/docs/
