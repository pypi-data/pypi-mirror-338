# Release Process

This document outlines the process for creating releases of the auto-python-toolkit.

## Automated CI/CD Releases

The project is configured with GitHub Actions to automatically build and release the toolkit when a new tag is pushed.

### How to Create a New Release

1. Make sure all your changes are committed and pushed to the main branch.

2. Create and push a new tag with a version number following semantic versioning (vX.Y.Z):

```bash
# Create a tag locally
git tag v1.0.0

# Push the tag to GitHub
git push origin v1.0.0
```

3. The GitHub Actions workflow will automatically:
   - Build the toolkit
   - Create sample packages
   - Create a new GitHub Release with the tag name
   - Attach the toolkit ZIP files to the release

4. You can find the releases at: https://github.com/tkpdx01/auto-python-toolkit/releases

## Release Artifacts

Each release will include:

1. `auto-python-toolkit-X.Y.Z.zip` - The complete toolkit source code
2. Sample environment packages built during the CI process

## Manual Release Process

If you need to create a release manually:

1. Create a new release from the GitHub web interface
   - Go to https://github.com/tkpdx01/auto-python-toolkit/releases
   - Click "Draft a new release"
   - Enter a tag version (e.g., "v1.0.0")
   - Add a title and description
   - Upload the ZIP files
   - Click "Publish release"

## Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **Major version (X)**: Incompatible API changes
- **Minor version (Y)**: Add functionality in a backward-compatible manner
- **Patch version (Z)**: Backward-compatible bug fixes

## Release Notes

When creating a release, include information about:

- New features
- Bug fixes
- Breaking changes
- Dependency updates
- Supported operating systems and Python versions 