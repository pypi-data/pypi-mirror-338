__version__ = "0.5.7"


try:
    import urllib3

    # Show following warning only once.
    urllib3.warnings.simplefilter("default", urllib3.exceptions.SecurityWarning)

except ImportError:
    pass
