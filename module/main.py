# -*- coding: utf-8 -*-
"""Module template.
"""
from typing import Optional


class Module():
    """Module class template.
    """

    def __init__(self, param: Optional[str]):
        """Constructor.
        """
        self.param = param

    def run(self) -> None:
        """Do something.
        """
        print(self.param)


def main(param: Optional[str]) -> None:
    """Main function.
    """
    module = Module(param)
    module.run()
