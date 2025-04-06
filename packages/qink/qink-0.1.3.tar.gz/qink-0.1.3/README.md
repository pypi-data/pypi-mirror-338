<img src="./logo.jpg" />

# Qink

Qink is a powerful distributed data processing framework designed for efficiently consuming and processing partitioned data streams.

## Features

- **Partition-based Processing** 📊: Handles partitioned data sources with exceptional efficiency, improving performance metrics.
- **Parallel Processing** ⚡: Processes multiple partitions simultaneously with configurable workers per partition.
- **State Management** 🛡️: Maintains processing state with reliability, ensuring fault tolerance.
- **Checkpointing**: Saves state at regular intervals to ensure data durability.
- **Key-based Distribution**: Distributes keys to workers with consistent precision for optimized processing.

## Usage

```python
import logging
from datetime import timedelta
from qink.lib.qink import Qink
from qink.lib.qink_storage_provider import YourStorageProvider
from qink.lib.qink_source import YourDataSource

# Configure Qink
logger = logging.getLogger("qink")
storage_provider = YourStorageProvider()
workers_per_partition = 4  # Customize for optimal performance
checkpoint_interval = timedelta(minutes=5)

# Initialize and start Qink
qink = Qink(
    logger=logger,
    storage_provider=storage_provider,
    workers_per_partition=workers_per_partition,
    checkpoint_interval=checkpoint_interval
)

# Connect to your data source
qink.source(YourDataSource()).start()
```

## Testimonials

"Qink revolutionized our data pipeline efficiency." - Data Engineering Team Lead

"After implementing Qink, our processing speeds improved dramatically." - Enterprise Architect

<hr/>

Copyright 2024 Quadible

This software is the exclusive property of Quadible and is protected under copyright law. Unauthorized copying, distribution, or use of this software, in whole or in part, without express permission from Quadible is strictly prohibited.

This repository and its contents are for authorized internal use only. External sharing or modification is not permitted unless written consent is obtained from Quadible.

For inquiries about permitted usage or licensing, please contact [info@quadible.co.uk](mailto:info@quadible.co.uk).
