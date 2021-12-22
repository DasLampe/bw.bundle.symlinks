# Symlink Bundle

Simple bundlewrap bundle to create symlinks.

Sometimes you just get in the position where you have to create some symlinks, without any further configuration ... call symlink item directly from nodes.py isn't possible yet.

## Config

```python
'metadata': {
	'symlinks': {
		'/etc/localtime': {
			'target': '/usr/share/zoneinfo/Europe/Berlin',
			'owner': 'root',
			'group': 'root',
		}
	}
}
```

Info: The `symlink` item is creating all needed directories for you!
