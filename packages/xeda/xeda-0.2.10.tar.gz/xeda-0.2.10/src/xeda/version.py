from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("xeda")
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"
