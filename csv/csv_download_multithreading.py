from multiprocessing import Process
import csv
import os,stat
import urllib.request
import sys
import socket

class csv_download_nultithreading(Process):
     def __init__(self):
         Process.__init__(self)