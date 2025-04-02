from setuptools import find_packages, setup

desc = (
    "Placeholder package only. Please install from source "
    "https://github.com/UKGovernmentBEIS/inspect_proxmox_sandbox. A Proxmox Sandbox "
    "Environment for Inspect."
)
setup(
    name="inspect-proxmox-sandbox",
    version="0.0.1",
    description=desc,
    long_description=desc,
    author="UK AI Safety Institute",
    packages=find_packages(),
    url="https://github.com/UKGovernmentBEIS/inspect_proxmox_sandbox",
)
