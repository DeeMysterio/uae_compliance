from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in uae_compliance/__init__.py
from uae_compliance import __version__ as version

setup(
	name="uae_compliance",
	version=version,
	description=" ERPNext App that includes regional compliance configuration for UAE",
	author="Frappe Technologies Private Limited",
	author_email="diksha@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
