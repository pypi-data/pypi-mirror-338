# mojo_arrow_sys

A Python C extension that provides access to Apache Arrow C Data Interface streams from Mojo.

## Overview

This module provides a bridge between Python objects that implement the Arrow C Data Interface 
and the Mojo programming language. It exposes the `arrow_stream` function which:

1. Takes a Python object
2. Checks if it has an `__array_c_stream__` attribute
3. Calls that attribute to get a C data stream
4. Returns the ArrowArrayStream pointer encapsulated as a PyCapsule

## Installation

```bash
pip install mojo_arrow_sys
```

Or from source:

```bash
git clone https://github.com/mseritan/mojo_arrow_sys.git
cd mojo_arrow_sys
make install
```

## Usage

```python
import mojo_arrow_sys
import pyarrow as pa

# Create some arrow data
table = pa.table({'a': [1, 2, 3], 'b': ['foo', 'bar', 'baz']})

# Get the Arrow C stream
stream_capsule = mojo_arrow_sys.arrow_stream(table)

# Now this capsule can be passed to Mojo code that can extract the raw pointer
```

## Development

### Prerequisites

- Python 3.7+
- C compiler (gcc, clang, MSVC, etc.)
- pyarrow (for testing)

### Building

```bash
make build
```

### Testing

```bash
make test
```

## License

MIT
