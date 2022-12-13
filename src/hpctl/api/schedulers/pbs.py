import json
import operator
import typing

import shell
import tabulate

from hpctl import utils
from hpctl.schemas.pbs import Nodes
from hpctl.api.schedulers.base import SchedulerBase

__all__ = ("PBS", "PBSFormatter")


class PBS(SchedulerBase):

    def nodes(self, server=None, name="", vnodes=False, sort="name", flags=""):
        opts = f"-s {server or self.server}"
        opts = f"{opts} -a{' -v' if vnodes else ''}"
        opts = f"{opts} -F json"
        if flags:
            opts = f"{opts} {flags}"
        cmd = f"{self._exec}/bin/pbsnodes {opts}"

        response = shell.Shell().run(cmd)
        if response.code != 0:
            raise shell.CommandError(response.errors(raw=True))

        data = json.loads(response.output(raw=True))
        nodes = Nodes(data)
        sorted_nodes = sorted(nodes, key=operator.itemgetter(sort))
        return [
            x
            for x in sorted_nodes
            if name in x["name"] and (utils.is_vnode(x["name"]) if vnodes else True)
        ]


class PBSFormatter:
    @classmethod
    def nodes(cls, data: typing.List[dict], fmt="simple"):
        def resource(node_data, resource_type):
            available = node_data["resources_available"][resource_type]
            assigned = node_data["resources_assigned"][resource_type]
            free = available - assigned
            line = f"{free}/{available}"
            if resource_type == "mem":
                line = f"{utils.human_size(free)}/{utils.human_size(available)}"
            color = utils.color_resource(available=available, free=free)
            return utils.colored_line(line=line, color=color)

        headers = [
            "name",
            "queue",
            "state",
            "cpus (f/t)",
            "gpus (f/t)",
            "mem (f/t)",
            "cpu type",
            "network",
            "comment",
        ]
        table = map(
            cls._truncate_row,
            [
                [
                    x["name"],
                    x["queue"],
                    utils.colored_line(
                        line=x["state"], color=utils.color_state(x["state"])
                    ),
                    resource(node_data=d, resource_type="cpus"),
                    resource(node_data=d, resource_type="gpus"),
                    resource(node_data=d, resource_type="mem"),
                    x["cpu_type"],
                    x["network"],
                    x["comment"],
                ]
                for x in data
            ],
        )

        return tabulate.tabulate(table, headers=headers, tablefmt=fmt)

    @classmethod
    def _truncate_row(cls, row):
        return map(cls._truncate_column, row)

    @staticmethod
    def _truncate_column(column):
        column = str(column)
        return (column[:30] + "...") if len(column) > 30 else column
