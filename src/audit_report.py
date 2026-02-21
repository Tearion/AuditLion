#!/usr/bin/python
import sys
import json
from pydantic import BaseModel
from typing import List, Optional

class Package(BaseModel):
    """ Model  """
    name: str
    versionInfo: Optional[str] = None
    licenseDeclared: Optional[str] = None
    licenseConcluded: Optional[str] = None

class SPDXDocument(BaseModel):
    name: str
    packages: List[Package] = []

def parseJsonFile(inputPath):
    """ Parses the File in json format """

    if not inputPath:
        print("[ERROR] Input is null or empty.")
        sys.exit(1)
    
    print("Parsing string...")
    with open(inputPath) as f:
        raw = json.load(f)

    return SPDXDocument(**raw)

    #for package in doc.packages:
    #    print(package)

def get_licenses_unique(doc):
    licenses = set()
    for package in doc.packages:
        if package.licenseDeclared:
            licenses.add(package.licenseDeclared)

    return list(licenses)

