# -*- coding: utf-8 -*-
"""
使用线程池实现可控数目的并发
"""
import time
from multiprocessing.pool import ThreadPool


class A(object):
    def run_monitor(self):
        clus_info = self.get_clustername()
        clus_res = list()

        pool = ThreadPool(processes=9)
        for i in clus_info:
            clus_res.append(
                pool.apply_async(
                    self.get_topo_min_info,
                    (i.get('cluster_name'), i.get('id'))
                )
            )
        pool.close()
        pool.join()

        return [res.get() for res in clus_res]

    def get_clustername(self):
        return [
            {'cluster_name': 1, 'id': 2},
            {'cluster_name': 1, 'id': 2},
            {'cluster_name': 1, 'id': 2},
            {'cluster_name': 4, 'id': 3}
        ]

    def get_topo_min_info(self, a, b):
        time.sleep(2)
        return a, b


if __name__ == '__main__':
    x = A()
    print x.run_monitor()
