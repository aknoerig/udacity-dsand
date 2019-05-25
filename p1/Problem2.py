import os

def find_files(suffix, path):
   """
   Find all files beneath path with file name suffix.

   Note that a path may contain further subdirectories
   and those subdirectories may also contain further subdirectories.

   There are no limits to the depth of the subdirectories can be.

   Args:
   suffix(str): suffix of the file name to be found
   path(str): path of the file system

   Returns:
      a list of paths
   """
   assert(suffix)
   assert(path)
   found_files = []

   if os.path.isfile( path ):
      if path.endswith( suffix ):
         found_files.append( path )
   elif os.path.isdir( path ):
      for child in os.listdir( path ):
         found_files.extend( find_files( suffix, os.path.join( path, child ) ) )
   return found_files

print( find_files('.c', './testdir') )
#['./testdir/subdir3/d.c', './testdir/subdir2/c.c', './testdir/subdir2/subsubdirA/b.c', './testdir/e.c', './testdir/subdir.c/a.c']

print( find_files('.h', './testdir') )
#['./testdir/subdir2/subsubdirA/b.h', './testdir/subdir1/a.h']

print( find_files('.py', './testdir') )
#[]

#print( find_files('', './testdir') )
# AssertionError

#print( find_files(None, './testdir') )
# AssertionError