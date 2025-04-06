Usage
=====

.. _installation:

Installation
------------

Raic Foundry offers both CLI and a python SDK, both of which can be installed via pip package.

Please note that the recommended python is version 3.12. And as always, working within a virtual environment is highly recommended

.. code-block:: console

   python3.12 -m venv .venv
   source .venv/bin/activate

FOR INTERNAL RAIC LABS PIP REPO
Make sure keyring and artifacts-keyring are installed to handle authenticating to the feed.
When prompted enter your AzureDevOps user id and empty for password

.. code-block:: console

   (.venv) $ python3.12 -m pip install keyring artifacts-keyring

To install the raic-foundry package:

.. code-block:: console

    (.venv) $ python3.12 -m pip install --index-url https://pkgs.dev.azure.com/synthetaic-org/RAIC-V1/_packaging/raic-python-packages/pypi/simple/ raic-foundry

and if you want to add raic-foundry via a requirements.txt you can add the internal package source to the whole virtual environment

.. code-block:: console

    printf "[global]\nindex-url=https://pkgs.dev.azure.com/synthetaic-org/RAIC-V1/_packaging/raic-python-packages/pypi/simple/" > .venv/pip.conf



Command Line Inferface
----------------------

If you are looking for a command line interface rather than using the sdk, this has now been installed.  Feel free to start crreating data sources and inference runs using the commands below.  

For further information about using the SDK please continue reading the documentation.

.. typer:: raic.foundry.cli.raic_cli.raic_commands
    :prog: raic-foundry
    :width: 120
    :preferred: svg