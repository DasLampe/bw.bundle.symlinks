symlinks = {}
directories = {}

for path, config in node.metadata.get('symlinks', {}).items():
    symlinks[path] = {
        'target': config.get('target'),
        'owner': config.get('owner', 'root'),
        'group': config.get('group', 'root'),
    }
