#!/usr/bin/python
import sys
import audit_report

def main():
    print("Invoke scan")
    path = "./testdata/test.spdx.json"
    doc = audit_report.parseJsonFile(path)

    print(f"Number of packages: {len(doc.packages)}")
    print("== List of licenses ==")
    licenses = audit_report.get_licenses_unique(doc)

    for license in licenses:
        print(license)
    
    print("== List of packages ==")
    for package in doc.packages:
        print(package.name)

def get_help():
    """ Prints the help text for the '-p' argument """
    print("No help available")

if "-h" in sys.argv:
    print('Number of arguments:', len(sys.argv), 'arguments.')
    get_help()
    sys.exit(0)

# Check, if there are not enough arguments to run this method.
if len(sys.argv) == 0:
    print("Error: Arguments required.")
    get_help()
    sys.exit(1)
    
main()