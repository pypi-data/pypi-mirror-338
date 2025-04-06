# a3consul

English | [简体中文](README_ZH.md)

`a3consul` is a simple wrapper around `py-consul` to make it easier to use.

## 1. Introduction

* Provide encapsulation for `Node Discovery`.


## 2. Usage

### Install

```shell
pip install a3consul

```

### Examples: Node Discovery

* Node

```python
from a3consul.scene_cases.node_discovery.node import Node

if __name__ == '__main__':
    node_conf = {
        "topic": "unittest",
        "node_path": "/nodes/",
        "init": {
            "host": "127.0.0.1",
            "port": 8500,
        },
        "session": {
            "ttl": 10,
        },
        "renew": {
            "sleep_seconds": 5,
            "timeout_seconds": 20,
        },
    }
    node = Node(conf=node_conf)
    node_id = node.register_node_id()
    node.start_renew_thread()
    node.close()

```

* NodeWatcher

```python
from typing import Set
from a3consul.scene_cases.node_discovery.node_watcher import NodeWatcher


class MyNodeWatcher(NodeWatcher):
    def _on_change(self, online_node_id_set: Set[str], offline_node_id_set: Set[str]):
        # do something
        pass

    def _handle_first_node_id_set(self, node_id_set: Set[str]):
        # kick or keep them or do something else
        pass


if __name__ == '__main__':
    watcher_conf = {
        "init": {
            "host": "127.0.0.1",
            "port": 8500,
        },
        "node_path": "/nodes/",
    }
    watcher = MyNodeWatcher(conf=watcher_conf)
    watcher.start()

```
