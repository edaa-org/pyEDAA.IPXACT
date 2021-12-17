# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#              ___ ______  __    _    ____ _____ 
#  _ __  _   _|_ _|  _ \ \/ /   / \  / ___|_   _|
# | '_ \| | | || || |_) \  /   / _ \| |     | |  
# | |_) | |_| || ||  __//  \  / ___ \ |___  | |  
# | .__/ \__, |___|_|  /_/\_\/_/   \_\____| |_|  
# |_|    |___/                                   
# =============================================================================
# Authors:						Patrick Lehmann
#
# Python module:	    A Document-Object-Model (DOM) for IP-XACT files.
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
#
from pathlib             import Path
from pyTooling.Packaging import DescribePythonPackageHostedOnGitHub

gitHubNamespace =        "edaa-org"
packageName =            "pyEDAA.IPXACT"
packageDirectory =       packageName.replace(".", "/")
packageInformationFile = Path(f"{packageDirectory}/__init__.py")

DescribePythonPackageHostedOnGitHub(
	packageName=packageName,
	description="A Document-Object-Model (DOM) for IP-XACT files.",
	gitHubNamespace=gitHubNamespace,
	sourceFileWithVersion=packageInformationFile,
	developmentStatus="pre-alpha",
	classifiers=[
		"Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
	]
)
