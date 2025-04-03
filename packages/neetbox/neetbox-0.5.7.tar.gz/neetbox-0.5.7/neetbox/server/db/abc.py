# -*- coding: utf-8 -*-
#
# Author: GavinGong aka VisualDust
# Github: github.com/visualDust
# Date:   20240116

import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Tuple, Union


class FetchType(str, Enum):
    ALL = "all"
    ONE = "one"
    MANY = "many"


class SortType(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


class ManageableDB(ABC):
    @abstractmethod
    def size(self):
        """get local storage usage in bytes"""
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        raise NotImplementedError()

    @abstractmethod
    def delete(self):
        """handle delete, a typical behavior is to close connection and remove files"""
        raise NotImplementedError()
