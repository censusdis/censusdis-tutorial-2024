"""This is a quick little script to check the version of censusdis in the runtime environment."""

import censusdis


def main():
    version = censusdis.version

    if version == "Unknown":
        print("Unknown version number. Expected X.Y.Z format.")
    elif len(version.split(".")) != 3:
        print("Invalid version number. Expected X.Y.Z")
    else:
        x, y, z = version.split(".")

        if int(x) != 1 or int(y) != 1 or int(z) < 10:
            print("Invalid version number. Expected 1.1.Z for Z >= 10.")
        else:
            print(f"Valid version {version}")


if __name__ == "__main__":
    main()
