# __init__.py

#what this file does:
#   1. Tells Python that whole directory here should be treated as a package
#   2. Controls what is available when package is imported
#   By importing hello function in here, users can directly call hello() function


from .main import hello