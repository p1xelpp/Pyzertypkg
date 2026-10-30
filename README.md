# Pyzertypkg

A package manager made in Python.

Pyzertypkg downloads, installs, uninstalls, and manages `.azertypkg` packages from a repository JSON file. It exists because why not.

## Features

- Download package indexes from servers
- Install packages
- Uninstall packages
- Download packages without installing them
- List available packages
- 100% powered by random ideas and questionable naming choices

## Installation

Clone the repository:

```bash
git clone https://github.com/yourname/pyzertypkg.git
cd pyzertypkg
```

Run it with:

```bash
python3 main.py
```

## Usage

### Update package list

Downloads a repository index.

```bash
python3 main.py -u
```

Default repository:

```text
https://p1xelpp.github.io/index.json
```

### List available packages

```bash
python3 main.py -lp
```

Example output:

```text
goofyahhpackage (1.0)
  this package doesnt do ANYTHING
```

### Install a package

```bash
python3 main.py -i package-name
```

Example:

```bash
python3 main.py -i goofyahhpackage
```

### Download a package without installing

```bash
python3 main.py -gp package-name
```

### Uninstall a package

```bash
python3 main.py -ui package-name
```

## Repository Format

Repositories use JSON:

```json
{
  "packages": [
    {
      "name": "goofyahhpackage",
      "version": "1.0",
      "description": "this package doesnt do ANYTHING",
      "url": "https://example.com/goofyahhpackage.azertypkg"
    }
  ]
}
```

## Package Format

`.azertypkg` files are ZIP archives.

When installing a package, Pyzertypkg extracts the archive to:

```text
ya-i-need-dis-map/installed/<package-name>
```

## File Structure

```text
ya-i-need-dis-map/
├── installed/
├── tmp/
└── repo.json
```

## Known Issues

- No dependency resolution
- No package updates
- Error handling is held together by hopes and dreams
- Code quality may vary depending on sleep levels

## Why "Pyzertypkg"?

Nobody knows.

## License

MIT License (or whatever license you choose).

---

> "Pyzertypkg doesn't have super cow powers."
(hehe i made ts readme with ai me lazy)
