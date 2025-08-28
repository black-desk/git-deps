__version__ = "0.6.0"

# Also try to get version from package metadata if available
try:
    # Try the modern importlib.metadata first (Python 3.8+)
    from importlib.metadata import version, PackageNotFoundError
    try:
        __version__ = version("git-deps")
    except PackageNotFoundError:
        pass  # Use the default version above
except ImportError:
    # Fallback for Python < 3.8
    try:
        import pkg_resources
        __version__ = pkg_resources.get_distribution("git-deps").version
    except (pkg_resources.DistributionNotFound, ImportError):
        pass  # Use the default version above
