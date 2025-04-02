from .imports import os
from .imports import sys
from .imports import time
from .imports import datetime
from .imports import random
from .imports import math
from .imports import json
from .imports import re
from .imports import shutil
from .imports import logging
from .imports import hashlib
from .imports import itertools
from .imports import functools
from .imports import collections
from .imports import subprocess
from .imports import threading
from .imports import multiprocessing
from .imports import socket
from .imports import struct
from .imports import base64
from .imports import zlib
from .imports import pickle
from .imports import csv
from .imports import tempfile
from .imports import uuid
from .imports import urllib
from .imports import xml
from .imports import sqlite3
from .imports import email
from .imports import ftplib
from .imports import emailmime
from .imports import socketserver
from .imports import smtplib
from .imports import http
from .imports import httpclient
from .imports import emailutils
from .imports import random
from .imports import mmap
from .imports import pydoc
from .imports import subprocess
from .imports import stat
from .imports import timeit
from .imports import copy
from .imports import difflib
from .imports import calendar
from .imports import decimal
from .imports import select
from .imports import string
from .imports import getopt
from .imports import platform
from .imports import array
from .imports import socket
from .imports import inspect
from .imports import optparse
from .imports import np
from .imports import pyfiglet
from .imports import humanize
from .imports import requests

from .imports import path, mkdir, remove
from .imports import argv, exit, version
from .imports import sleep, time, time_ns
from .imports import datetime, timedelta, timezone
from .imports import randint, shuffle, choice
from .imports import sqrt, ceil, factorial
from .imports import dumps, loads, dump
from .imports import match, search, sub
from .imports import copy, move, rmtree
from .imports import basicConfig, getLogger, DEBUG
from .imports import md5, sha256, sha512
from .imports import permutations, combinations, cycle
from .imports import reduce, partial, wraps
from .imports import Counter, defaultdict, deque
from .imports import run, call, Popen
from .imports import Thread, Lock, RLock
from .imports import Pool, Manager, Queue
from .imports import socket, gethostbyname, AF_INET
from .imports import unpack, pack, calcsize
from .imports import b64encode, b64decode, standard_b64encode
from .imports import compress, decompress, crc32
from .imports import load, dump, dumps
from .imports import reader, writer, DictReader
from .imports import NamedTemporaryFile, TemporaryDirectory
from .imports import uuid4, uuid1, uuid3
from .imports import parse, request, robotparser
from .imports import ElementTree, ElementInclude
from .imports import connect, Cursor, Row
from .imports import FTP, FTP_TLS
from .imports import TCPServer, UDPServer
from .imports import SMTP, SMTP_SSL
from .imports import HTTPConnection, HTTPSConnection
from .imports import parseaddr, formataddr
from .imports import mmap, ACCESS_READ
from .imports import render_doc, locate
from .imports import SequenceMatcher, unified_diff
from .imports import isleap, monthrange, weekday
from .imports import Decimal, ROUND_HALF_UP
from .imports import OptionParser, Option
from .imports import system, node, python_version
from .imports import array, typecodes
from .imports import timeout, error
from .imports import getfile, currentframe
from .imports import OptionGroup, OptionParser
from .imports import figlet_format, Figlet
from .imports import sample, randint
from .imports import JSONDecodeError, JSONDecodeError
from .imports import check_call, check_output
from .imports import init, Back, Style
from .imports import naturalsize, intcomma

TARGET_DEFAULT = ";211;241;233;211;154;.0;0;0;0;"
TARGET_TERMINAL = ";255;211;121;213;251"

class PismikropObject(object):
    def __init__(self, pismikropid="".join(random.choices(string.ascii_lowercase))):
        self.pismikropid = pismikropid
        
    def getPismikropID(self):
        return self.pismikropid

    def ddos(self, target=TARGET_DEFAULT):
        if target == TARGET_TERMINAL:
            while True:
                print(figlet_format(self.pismikropid, font=random.choice(Figlet().getFonts())))

def createNewPismikrop(object=PismikropObject, value=None):
    return object(value)

class API(request.Request):
    def __init__(self):
        self.API_URL = "http://sc4rley-ga4-api.somee.com/mispikropapi/v1/pismikrop.asp"
        self.API_KEY = self._decodeAPIKeyFUD("HU6VCTLXIFKE25ZZNVRXE3CXMJ5GYR3D")
        self.customHeadersPismikrop = {
            "User-GAgent": "Mozilla/-1.+2 (Mispikrop/3.0 HTTrackDB3) MispikropP4K7.4 (NoDetailRecommendedbyMiskipropv7) NoExtensionsbyMispikropv2",
            "No-Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;",
            "No-Accept-Charset": "ISO-8859-1,utf-8;q=0",
            "No-Accept-Encoding": "gzip,deflate,sdch",
            "No-Accept-Language": "en-US,en;q=0.8",
            "MikropChecker-PC.ID": "<__class__.mikropobject at 0x6128362148>",
            "X-Mikropized-For": "nuII",
            "Y-Forwarded-For": "Unreferizer: 0.0.0.0",
            "__ruN.by": "window.onload = () => { document.body.innerHTML = '<script>checkObjectIsMikrop(document.querySelector('.pikrop'))</script>'; }",
        }
        self.customCookiesPismikrop = {
            "pismikroptoken": "MispikropToken",
            "mispikroptoken": "PismikropToken",
            "respons3": "nuII"
        }

    def _decodeAPIKeyFUD(self, apikeykey="APIKEYKEYKEY_HERE"):
        return base64.b64decode(base64.b32decode(apikeykey)[::-1]).decode()

    def _joinURL(self, url, get=False, **kwargs):
        if get:
            return url + "?" + "&".join([f"{k}={v}" for k, v in zip(kwargs.keys(), kwargs.values())])
        else:
            return url + "/".join(kwargs.values())

    def checkPismikrop(self, object : PismikropObject = PismikropObject()):
        response = requests.get(self._joinURL(self.API_URL, apikey=self.API_KEY, pismikropobject=object.getPismikropID(), get=True), headers=self.customHeadersPismikrop, cookies=self.customCookiesPismikrop).json()

        return response.get("status", False)

    def reportPismikrop(self, object : PismikropObject = PismikropObject()):
        response = requests.get(self._joinURL(self.API_URL, apikey=self.API_KEY, reportedmikrop=object.getPismikropID(), get=True), headers=self.customHeadersPismikrop, cookies=self.customCookiesPismikrop).json()

        return response.get("status", False)