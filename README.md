# Giosg App bindings

Helper library for Django based application for handling Giosg App trigger requests from Giosg platform.

## Changelog

### 1.0.0 (2022-10-11)
First stable release


## Publishing new version

- Finalize code changes
- Change `version` and `download_url` to match new version in `setup.py`, and push to PR
  - Remember https://semver.org/ versioning and avoid all backwards incompatible changes!
- Merge to master after review.
- Create a git release with that version
- (Download twine, `pip3 install twine`)
- Run `python3 setup.py sdist` to create source distribution
- Run `twine upload dist/*` to upload source distribution to PyPI
- Enter prompted username and password. These can be found from the `infra-shared-pwdb`, which is accessible only to the infra team. Ask a member of the infra team to give you the username and password.
