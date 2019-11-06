#!/bin/bash
ARG=$1
INSTALL_PYTHON="install-python"
USER=$(whoami)
MINICONDA_PATH='/Users/'$USER'/goinfre/miniconda'
INSTALL="bleh"

if [[ "$ARG" == "$INSTALL_PYTHON" ]]
then
	if [[  -f $MINICONDA_PATH'/bin/python' ]]; then
		echo "Python is already installed, do you want to reinstall it ?"
		echo "[yes|no]"
		read INSTALL
	fi
	if [[ "$INSTALL" == 'bleh' ]]; then
		curl -s https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/goinfre/miniconda.sh > /dev/null 2>&1
		bash  /Users/$USER/goinfre/miniconda.sh -b -p $MINICONDA_PATH > /dev/null
		echo "PATH=$PATH:$MINICONDA_PATH/miniconda/bin" >> ~/.zshrc
		echo 'Python has been installed.'
	fi
	if [[ "$INSTALL" == 'yes' ]]; then
		rm -rf $MINICONDA_PATH
		echo 'Python has been removed.'
		curl -s https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/goinfre/miniconda.sh > /dev/null
		bash  /Users/$USER/goinfre/miniconda.sh -b -p $MINICONDA_PATH > /dev/null 2>&1
		echo "PATH=$PATH:$MINICONDA_PATH/miniconda/bin" >> ~/.zshrc
		echo 'Python has been installed.'
	fi
	if [[ $INSTALL == 'no' ]]; then
		echo 'exit.'
	fi
fi
