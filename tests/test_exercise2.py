import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_clamp_correct_range():
    assert clamp(3, 1, 5) == 3
