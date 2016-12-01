import sys
from libclang.cindex import Index, SourceLocation, Cursor, File, CursorKind, TypeKind, Config, LibclangError

def getQuickFix(diagnostic):
  # Some diagnostics have no file, e.g. "too many errors emitted, stopping now"

  if diagnostic.location.file:
    filename = diagnostic.location.file.name
  else:
    filename = ""

  if diagnostic.severity == diagnostic.Ignored:
    type = 'I'
  elif diagnostic.severity == diagnostic.Note:
    type = 'I'
  elif diagnostic.severity == diagnostic.Warning:
    type = 'W'
  elif diagnostic.severity == diagnostic.Error:
    type = 'E'
  elif diagnostic.severity == diagnostic.Fatal:
    type = 'E'
  else:
    return None

  res =  dict({ 'buf' :  filename,
    'lnum' : diagnostic.location.line,
    'col' : diagnostic.location.column,
    'text' : diagnostic.spelling,
    'type' : type})
  return res

def getQuickFixList(tu):
  return filter (None, map (getQuickFix, tu.diagnostics))

def init():
  conf = Config()

  # here we use the libclang.dylib from the vim plugin -- YouCompleteMe
  libclangPath = "."
  Config.set_library_path(libclangPath)
  conf.set_library_path(libclangPath)
  try:
    conf.get_cindex_library()
  except LibclangError as e:
    print "Error: " + str(e)

def main():
    init()
    index = Index.create()
    print sys.argv[1]
    tu = index.parse(sys.argv[1], args=['-x', 'objective-c',
                                        '-arch', 'arm64',
                                        '-fmodules',
                                        '-miphoneos-version-min=9.3',
                                        '-isysroot', '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk',
                                        ])

    print getQuickFixList(tu)

if __name__ == '__main__':
    main()
