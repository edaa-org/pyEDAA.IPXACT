# ==================================================================================================================== #
#              _____ ____    _        _      ___ ______  __    _    ____ _____                                         #
#  _ __  _   _| ____|  _ \  / \      / \    |_ _|  _ \ \/ /   / \  / ___|_   _|                                        #
# | '_ \| | | |  _| | | | |/ _ \    / _ \    | || |_) \  /   / _ \| |     | |                                          #
# | |_) | |_| | |___| |_| / ___ \  / ___ \ _ | ||  __//  \  / ___ \ |___  | |                                          #
# | .__/ \__, |_____|____/_/   \_\/_/   \_(_)___|_|  /_/\_\/_/   \_\____| |_|                                          #
# |_|    |___/                                                                                                         #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2024 Patrick Lehmann - Bötzingen, Germany                                                             #
# Copyright 2016-2016 Patrick Lehmann - Dresden, Germany                                                               #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""Package installer for 'An abstract SystemRDL language model'."""
from setuptools          import setup

from itertools           import chain
from pathlib             import Path
from pyTooling.Packaging import DescribePythonPackageHostedOnGitHub, DEFAULT_CLASSIFIERS

gitHubNamespace =        "edaa-org"
packageName =            "pyEDAA.IPXACT"
packageDirectory =       packageName.replace(".", "/")
packageInformationFile = Path(f"{packageDirectory}/__init__.py")

setup(**DescribePythonPackageHostedOnGitHub(
	packageName=packageName,
	description="A Document-Object-Model (DOM) for IP-XACT files.",
	gitHubNamespace=gitHubNamespace,
	sourceFileWithVersion=packageInformationFile,
	developmentStatus="alpha",
	classifiers=list(DEFAULT_CLASSIFIERS) + [
		"Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)"
	],
	dataFiles={
		packageName: [
			str(file.relative_to(Path.cwd() / "pyEDAA/IPXACT")) for file in chain(
				Path.cwd().glob("pyEDAA/IPXACT/Schema/ipxact-*/*.xsd"),
				Path.cwd().glob("pyEDAA/IPXACT/Schema/ipxact-*/README.md"),
				Path.cwd().glob("pyEDAA/IPXACT/Schema/ieee-1685-*/*.xsd"),
				Path.cwd().glob("pyEDAA/IPXACT/Schema/ieee-1685-*/README.md"),
				Path.cwd().glob("pyEDAA/IPXACT/Schema/ieee-1685-*/LICENSE"),
				Path.cwd().glob("pyEDAA/IPXACT/Schema/ieee-1685-*/NOTICE"),
				Path.cwd().glob("pyEDAA/IPXACT/Schema/*.md"),
				Path.cwd().glob("pyEDAA/IPXACT/py.typed")
			)
		],
	}
))
