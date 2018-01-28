import sys

import libpyio


if __name__== "__main__":
    print("Starting the PYIO program");
    print("The number of arguments received: %d" %len(sys.argv))

    # Call init function
    libpyio.Initialize()