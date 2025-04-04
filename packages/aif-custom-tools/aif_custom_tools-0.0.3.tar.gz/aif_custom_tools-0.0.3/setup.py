from setuptools import find_packages, setup

PACKAGE_NAME = "aif_custom_tools"

setup(
    name=PACKAGE_NAME,
    version="0.0.3",
    description="This is my tools package",
    packages=find_packages(),
    entry_points={
        "package_tools": ["custom_llm_tool = aif_custom_tools.tools.utils:list_package_tools"],
    },
    include_package_data=True,   # This line tells setuptools to include files from MANIFEST.in
)