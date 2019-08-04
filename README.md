# file-copy-check

Example script for ensure that a file copy is complete before proceeding to the next step
in a script.  Useful for processes that need to copy large files since the copy
will get sent to a buffer and won't necessarily happen before the script moves to
the next step.