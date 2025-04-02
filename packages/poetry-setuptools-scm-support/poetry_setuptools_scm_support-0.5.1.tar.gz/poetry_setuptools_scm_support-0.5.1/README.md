A Poetry plugin that integrates setuptools_scm <https://pypi.org/project/setuptools-scm/> to console

Updates pyproject.toml file version with a calculated one

The idea is to add a mechanism for managing dev builds' versions guaranteeing uniqueness of them at deploy time.

Versions are calculated taking into account the distance between current commit and last tagged one, and current commit revision hash

examples:

    poetry version-calculate
1.0.1.dev1+g1e0ede4

    poetry version-calculate date
2025.4.1.1.dev1+g1e0ede4

**Note about date format:**

Two digits year is taken by default, you can change this behaviour making a previous git tag with a different supporten format, in this case for example 

    git tag 2025.4.1
 



