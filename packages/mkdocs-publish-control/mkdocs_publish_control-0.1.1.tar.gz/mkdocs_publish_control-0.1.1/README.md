# MkDocs Publish Control

A MkDocs plugin that allows you to control page visibility based on metadata. Perfect for managing draft content or private documentation within your MkDocs site.

## Features

- Control page visibility using simple metadata.
- Show/hide pages based on `hidden` metadata flag.
- Override visibility settings using environment variables.
- Works with both `mkdocs serve` and `mkdocs build`.
- Detailed logging for debugging.

## Installation

### Using Poetry

```bash
poetry add mkdocs-publish-control
```

### Using pip

```bash
pip install mkdocs-publish-control
```

## Usage

### Basic Configuration

Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - publish-control:
      show_all: false  # default behavior
```

### Controlling Page Visibility

In your markdown files, add the `hidden` metadata at the top of the file:

```markdown
---
hidden: true
---

# Your page content
```

- If `hidden: true` is set, the page will be excluded from the build
- If `hidden: false` is set or the metadata is not present, the page will be included
- The default behavior is to show pages (hidden: false)

### Showing All Pages

You can override the visibility settings in two ways:

1. Using environment variable:
```bash
MKDOCS_SHOW_ALL=true mkdocs serve
```

2. Using configuration in `mkdocs.yml`:
```yaml
plugins:
  - publish-control:
      show_all: true
```

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `enabled` | boolean | `true` | Enable or disable the plugin |
| `show_all` | boolean | `false` | Show all pages regardless of their hidden status |

## Examples

### Basic Usage

1. Create a markdown file with hidden metadata:
```markdown
---
hidden: true
---

# Draft Content
This page will not appear in the build by default.
```

2. Run mkdocs:
```bash
mkdocs serve
```

The page will be excluded from the build.

### Showing All Pages

To temporarily show all pages (including hidden ones):

```bash
MKDOCS_SHOW_ALL=true mkdocs serve
```

Or configure it permanently in `mkdocs.yml`:
```yaml
plugins:
  - publish-control:
      show_all: true
```

## Logging

The plugin provides detailed logging about which pages are being excluded. To see the logs, run mkdocs with the `--verbose` flag:

```bash
mkdocs serve --verbose
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
