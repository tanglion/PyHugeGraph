# -*- coding:utf-8 -*-
"""
PyCharm
__init__.py.py
18/9/14 16:32 by Gaomenghan
"""
import config
from comm.hugegraph.HugeGraphClient import HugeGraphClient

hugegraph_client = HugeGraphClient(host = config.hugegraph.CONTACT_POINTS,
                                   port = config.hugegraph.PORT,
                                   graph_name = "hugegraph"
)
