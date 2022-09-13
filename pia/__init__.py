__app_name__ = "pia"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    NOT_SUPPORTED_ERROR
) = range(4)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    NOT_SUPPORTED_ERROR: "command not supported error",
}
