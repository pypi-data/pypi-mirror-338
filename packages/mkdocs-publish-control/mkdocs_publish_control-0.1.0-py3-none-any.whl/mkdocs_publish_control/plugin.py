from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import logging
import os

log = logging.getLogger('mkdocs.plugins.publish_control')

class PublishControlPlugin(BasePlugin):
    """MkDocs plugin to control page publishing based on metadata."""

    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
        ('show_all', config_options.Type(bool, default=False)),
    )

    def on_config(self, config):
        """Called when the config is loaded."""
        # Check if MKDOCS_SHOW_ALL environment variable is set
        show_all = os.environ.get('MKDOCS_SHOW_ALL', '').lower() == 'true'
        if show_all:
            self.config['show_all'] = True
            log.info("MKDOCS_SHOW_ALL environment variable is set to true")

        log.info(f"PublishControlPlugin loaded with config: {self.config}")
        return config

    def on_files(self, files, config):
        """Called after the files are loaded, but before they are processed."""
        if self.config['show_all']:
            log.info("show_all is True, including all pages")
            return files

        # Filter out hidden pages
        for file in list(files):
            if file.src_path.endswith('.md'):
                # Read the file to check its metadata
                with open(file.abs_src_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Check for metadata block
                    if content.startswith('---'):
                        try:
                            # Extract metadata
                            metadata_end = content.find('---', 3)
                            if metadata_end != -1:
                                metadata = content[3:metadata_end]
                                # Check for hidden: true
                                if 'hidden: true' in metadata.lower():
                                    log.info(f"Excluding page {file.src_path} from build (hidden: true)")
                                    files.remove(file)
                        except Exception as e:
                            log.warning(f"Error processing metadata for {file.src_path}: {e}")

        return files
